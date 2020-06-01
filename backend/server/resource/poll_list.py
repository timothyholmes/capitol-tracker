import csv
import os
from models.poll_list_node import PollListNodeFactory


def parse_poll_list(csvfile):
    head, *tail = csvfile.split("\n")

    factory = PollListNodeFactory(head.split(","))

    poll_list = map(
        lambda x: factory.create_node(x),
        filter(lambda x: factory.is_valid_node(x), map(lambda x: x.split(","), tail)),
    )

    return poll_list
