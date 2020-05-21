import csv
import os
from models.poll_list_node import PollListNode


def parse_poll_list():
    csvfile = open("./assets/pollList.csv", newline="")

    try:
        csv_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        head, *tail = csv_reader
        poll_list = map(lambda x: PollListNode(*x), tail)

        return poll_list
    finally:
        csvfile.close()
