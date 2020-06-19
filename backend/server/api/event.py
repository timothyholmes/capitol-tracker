from flask import jsonify, request
from resource.data_node import create_data_node_batch
from resource.event import find

event_candidate_measurement = "event_candidate"
event_measurement = "event"

event_type_enum = dict([("start", 0), ("stop", 1), ("occurred", 2)])


def add_event(payload, candidate):
    def add_measurement(dic):
        dic["measurement"] = event_measurement
        dic.get("fields")["lifecycle"] = event_type_enum.get(
            dic.get("fields").get("lifecycle")
        )
        if candidate:
            dic.get("tags")["candidate"] = 1
        return dic

    nodes = list(map(add_measurement, payload))

    create_data_node_batch(nodes)

    return jsonify(payload)


def post():
    return add_event(request.get_json(), False)


def post_candidate():
    return add_event(request.get_json(), True)


def get():
    return jsonify(find({}, {candidate: 0}))


def get_candidate():
    return jsonify(find({}, {}))


def promote_candidate():

    return ""
