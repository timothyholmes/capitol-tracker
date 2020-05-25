from influxdb import InfluxDBClient


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

    def create(self):
        client = InfluxDBClient(
            "localhost", 8086, "root", "password", "capitol_tracker"
        )

        client.write_points([self.serialize()])

        return True

    @staticmethod
    def search():
        client = InfluxDBClient(
            "localhost", 8086, "root", "password", "capitol_tracker"
        )

        result = client.query("select * from congressional_outlook;")

        return result

    @staticmethod
    def get_measurements():
        client = InfluxDBClient(
            "localhost", 8086, "root", "password", "capitol_tracker"
        )

        result = client.get_list_measurements()

        return result

    @staticmethod
    def get_series():
        client = InfluxDBClient(
            "localhost", 8086, "root", "password", "capitol_tracker"
        )

        result = client.get_list_series()

        return result
