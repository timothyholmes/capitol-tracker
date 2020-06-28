from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
from models.data_node import DataNode
import os

host = os.environ.get("INFLUXDB_HOST")
token = os.environ.get("INFLUXDB_TOKEN")
org = os.environ.get("INFLUXDB_ORG")
bucket = os.environ.get("INFLUXDB_BUCKET")


class Poll(DataNode):
    """Model for Data Node"""

    def __init__(self, measurement, tags, fields, time):
        self.measurement = measurement
        self.tags = tags
        self.fields = fields
        self.time = time

    def serialize(self):
        return {
            "measurement": self.measurement,
            "tags": self.tags,
            "fields": self.fields,
            "time": self.time,
        }

    @staticmethod
    def search():
        client = InfluxDBClient(url=host, token=token, org=org)
        query_api = client.query_api()

        tables = query_api.query(
            'from(bucket: "capitol_tracker") |> filter(fn: (r) => r["_measurement"] != "event_candidate") |> filter(fn: (r) => r["_measurement"] != "event") |> range(start: 1700-01-01T00:01:00Z)'
        )

        result = []
        for table in tables:
            for record in table.records:
                poll_node = {}

                poll_node["stance"] = record.values["stance"]
                poll_node[record.values["_field"]] = record.values["_value"]
                poll_node["time"] = record.values["_time"]

                result.append(poll_node)

        return result

    @staticmethod
    def get_events(measurement):
        client = InfluxDBClient(url=host, token=token, org=org)
        query_api = client.query_api()

        tables = query_api.query(
            'from(bucket: "capitol_tracker") |> range(start: 1700-01-01T00:01:00Z) |> filter(fn: (r) => r["_measurement"] == "event")'
        )

        result = dict()
        # {'result': '_result', 'table': 2, '_start': datetime.datetime(1883, 7, 20, 2, 28, 48, 249303, tzinfo=datetime.timezone.utc), '_stop': datetime.datetime(2020, 6, 11, 2, 28, 48, 249303, tzinfo=datetime.timezone.utc), '_time': datetime.datetime(2016, 12, 5, 0, 0, tzinfo=datetime.timezone.utc), '_value': 2.0, '_field': 'lifecycle', '_measurement': 'event_candidate', 'effect': 'Gained_a_degree', 'name': 'Graduation'}
        for table in tables:
            for record in table.records:
                print(record.values)

                lifecycle_enum = dict([(1.0, "stop"), (0.0, "start")])

                if record.values["_value"] == 2.0:
                    event = {}

                    event["name"] = record.values["name"].replace("_", " ")
                    event["effect"] = record.values["effect"].replace("_", " ")
                    event["time"] = record.values["_time"]

                    if "event_id" in record.values:
                        event["event_id"] = record.values["event_id"].replace("_", " ")

                    result[record.values["name"]] = event
                elif record.values["_value"] < 2.0:
                    event = {}

                    if record.values["name"] in result:
                        event = result.get(record.values["name"])

                    event["name"] = record.values["name"].replace("_", " ")
                    event["effect"] = record.values["effect"].replace("_", " ")

                    if not "time" in event:
                        event["time"] = {}

                    event["time"][
                        lifecycle_enum.get(record.values["_value"])
                    ] = record.values["_time"]

                    result[record.values["name"]] = event

        return result.values()
