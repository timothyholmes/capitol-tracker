import csv
import os
from models.data_node import DataNode


def create_data_node(
    measurement, tags, fields, time,
):
    data_node = DataNode(measurement, tags, fields, time)

    data_node.create()

    return True


def search():
    rs = DataNode.search()

    api_response = list(rs.get_points(measurement="congressional_outlook"))

    return api_response
