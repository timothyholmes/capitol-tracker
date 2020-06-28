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

        def format_list_filter(key):
            def format_list_filter_value(value):
                return 'r["{key}"] == "{value}"'.format(key=key, value=value)

            return format_list_filter_value

        def format_filter_statement(k_v_pair):
            if type(k_v_pair[1]) is list:
                return "filter(fn: (r) => {or_statement})".format(
                    or_statement=" or ".join(
                        list(map(format_list_filter(k_v_pair[0]), k_v_pair[1]))
                    )
                )

            return 'filter(fn: (r) => r["{key}"] == "{value}")'.format(
                key=k_v_pair[0], value=k_v_pair[1]
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

        print(query)

        tables = query_api.query(query)

        return tables
