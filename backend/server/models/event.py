from pymongo import MongoClient


class Event:
    """Model for Event"""

    def __init__(
        self, connection, event_id, name, effect, namespace, candidate, start, end
    ):
        self.connection = connection
        self.event_id = event_id
        self.name = name
        self.effect = effect
        self.namespace = namespace
        self.candidate = candidate
        self.start = start
        self.end = end

    def serialize(self):
        return {
            "event_id": self.event_id,
            "name": self.name,
            "effect": self.effect,
            "namespace": self.namespace,
            "candidate": self.candidate,
            "start": self.start,
            "end": self.end,
        }

    def write(self):
        db = self.connection.capitol_tracker

        collection = db.events

        collection.insert_one(self.serialize())

        return self.event_id
