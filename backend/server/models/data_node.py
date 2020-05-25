from influxdb import InfluxDBClient


class DataNode:
    """Model for Data Node"""

    measurement = ""
    tags = ""
    fields = ""
    timestamp = ""

    def __init__(self, measurement, tags, fields, timestamp):
        self.measurement = measurement
        self.tags = tags
        self.fields = fields
        self.timestamp = timestamp

    def serialize(self):
        return {
            "measurement": self.measurement,
            "tags": self.tags,
            "fields": self.fields,
            "timestamp": self.timestamp,
        }

    def create(self):
        client = InfluxDBClient(
            "localhost", 8086, "root", "password", "capitol_tracker"
        )

        client.write_points([self.serialize()])

        return True
