from flask import jsonify, request
from resource.data_node import create_data_node_batch
from resource.event import find, promote, add


def post():
    return jsonify(add(request.get_json(), False))


def post_candidate():
    return jsonify(add(request.get_json(), True))


def get():
    return jsonify(find({}, {"candidate": 0}))


def get_candidate():
    return jsonify(find({}, {"candidate": 1}))


def promote_candidate():
    return jsonify(promote(request.get_json()))
