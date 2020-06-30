from pymongo import MongoClient
from models.event import Event


class EventSearch(Event):
    """Model for Event Search"""

    def get(self):
        db = self.connection.capitol_tracker

        results = list()

        query = dict()

        if self.namespace:
            query["namespace"] = self.namespace

        query["candidate"] = self.candidate

        for event in db.events.find(query):
            results.append(
                Event(
                    self.connection,
                    event["event_id"],
                    event["name"],
                    event["effect"],
                    event["namespace"],
                    event["candidate"],
                    event["start"],
                    event["end"],
                )
            )

        return results

    def getAndUpdate(self):
        db = self.connection.capitol_tracker

        results = list()

        query = {
            "event_id": {"$in": self.event_id},
        }

        update = {"$set": {"candidate": False}}

        db.events.update(query, update)

        return True
