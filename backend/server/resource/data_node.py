import csv
import os
from models.data_node import DataNode


def create_data_node(
    measurement, tags, fields, time,
):
    data_node = DataNode(measurement, tags, fields, time)

    data_node.create()

    return True


def search(measurement):
    rs = DataNode.search()

    measurements = list(DataNode.get_measurements())
    print(measurements)

    api_response = list(rs.get_points(measurement="trump_approval_rating"))

    return api_response


def find_measurements():
    rs = DataNode.get_measurements()

    return rs


def find_series():
    rs = DataNode.get_series()

    return rs
