from flask import request, jsonify
from resource.data_node import create_data_node_batch
from resource.poll import find, find_measurements


def post():
    payload = request.get_json()

    create_data_node_batch(payload)

    return jsonify(payload)


def search():
    return jsonify(find())


def get_measurements():
    return jsonify(find_measurements())
