from flask import jsonify, request
from resource.data_node import create_data_node_batch


def post():
    payload = request.get_json()

    create_data_node_batch(payload)

    return jsonify(payload)
