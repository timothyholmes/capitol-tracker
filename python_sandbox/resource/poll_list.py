import csv
import os
from models.poll_list_node import PollListNode


def parse_poll_list():
    csvfile = open("./assets/pollList.csv", newline="")

    try:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        head, *tail = spamreader
        poll_list = map(lambda x: PollListNode(*x), tail)

        return poll_list
    finally:
        csvfile.close()
