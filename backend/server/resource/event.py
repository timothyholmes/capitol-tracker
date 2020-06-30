from models.event_search import EventSearch
from resource.data_node import create_data_node_batch
from models.event import Event
from pymongo import MongoClient
import uuid
import os

host = os.environ.get("MONGO_HOST")
user = os.environ.get("MONGO_USER")
password = os.environ.get("MONGO_PASSWORD")

mongo_string = "mongodb+srv://{user}:{password}@{host}/capitol_tracker?retryWrites=true&w=majority".format(
    user=user, password=password, host=host
)


def add(payload, is_candidate):
    dic = payload
    candidate = False
    event_id = uuid.uuid4()

    if is_candidate:
        candidate = True

    client = MongoClient(mongo_string)

    event = Event(
        client,
        str(event_id),
        payload["name"],
        payload["effect"],
        payload["namespace"],
        candidate,
        payload["start"],
        payload["end"],
    )

    return event.write()


def find(event_id, name, effect, namespace, candidate, start, end):
    client = MongoClient(mongo_string)

    search = EventSearch(
        client, event_id, name, effect, namespace, candidate, start, end
    )

    results = search.get()

    return list(map(lambda result: result.serialize(), results))


def promote(event_ids):
    client = MongoClient(mongo_string)

    search = EventSearch(client, event_ids, False, False, False, True, False, False)

    search.getAndUpdate()

    return True
