import csv
import os
from models.data_node import DataNode
import calendar
import time


def convert_to_nanoseconds(seconds):
    return int("{seconds}000000000".format(seconds=seconds))


def create_data_node_batch(payload):
    for dic in payload:
        dic["time"] = convert_to_nanoseconds(
            calendar.timegm(time.strptime(dic["time"], "%m/%d/%Y"))
        )

    DataNode.create_batch(payload)

    return True


def find():
    print("in resource find")

    rs = DataNode.search()

    api_response = rs

    return api_response
