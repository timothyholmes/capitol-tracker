from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS
from models.data_node import DataNode
import os

host = os.environ.get("INFLUXDB_HOST")
token = os.environ.get("INFLUXDB_TOKEN")
org = os.environ.get("INFLUXDB_ORG")
bucket = os.environ.get("INFLUXDB_BUCKET")


class Search(DataNode):
    """Model for Search"""

    def get(self):
        client = InfluxDBClient(url=host, token=token, org=org)
        query_api = client.query_api()

        def format_filter_statement(k_v_pair):
            return 'filter(fn: (r) => r[{key}] == "{value}")'.format(
                key=k_v_pair[0], value=k_v_pair[0]
            )

        query = 'from(bucket: "capitol_tracker") |> range(start: {start}) |> filter(fn: (r) => r["_measurement"] == "{measurement}")'.format(
            start=self.time["start"], measurement=self.measurement
        )

        if self.tags:
            query = "{base_query} |> {tag_filter}".format(
                base_query=query,
                tag_filter=" |> ".join(
                    list(map(format_filter_statement, self.tags.items()))
                ),
            )

        tables = query_api.query(query)

        return tables
