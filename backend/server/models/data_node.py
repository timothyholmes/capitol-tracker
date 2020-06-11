from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
import os

host = os.environ.get("INFLUXDB_HOST")
token = os.environ.get("INFLUXDB_TOKEN")
org = os.environ.get("INFLUXDB_ORG")
bucket = os.environ.get("INFLUXDB_BUCKET")


class DataNode:
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
            'from(bucket: "capitol_tracker")|> range(start:-1200000h)'
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
    def create_batch(batch):
        def to_line_protocol(source):
            measurement = source["measurement"]
            time = source["time"]
            tagset = []
            fieldset = []

            for key, value in source["fields"].items():
                fieldset.append(
                    "{key}={value}".format(key=key, value=str(value).replace(" ", "_"))
                )

            for key, value in source["tags"].items():
                tagset.append(
                    "{key}={value}".format(key=key, value=str(value).replace(" ", "_"))
                )

            return "{measurement},{tagset} {fieldset} {time}".format(
                measurement=measurement,
                tagset=",".join(tagset),
                fieldset=",".join(fieldset),
                time=time,
            ).encode()

        client = InfluxDBClient(url=host, token=token)
        write_client = client.write_api(write_options=SYNCHRONOUS)

        print("Writing to {bucket} in {org}".format(bucket=bucket, org=org))

        data = list(map(to_line_protocol, batch))

        response = write_client.write(bucket, org, data)

        return True
