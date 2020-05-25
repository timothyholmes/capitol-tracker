import csv
import os
from models.data_node import DataNode


def create_data_node(
    measurement, tags, fields, timestamp,
):
    data_node = DataNode(
        measurement=measurement, tags=tags, fields=fields, timestamp=timestamp,
    )

    data_node.create()

    return True
