from flask import jsonify, request
from resource.data_node import create_data_node_batch
from resource.event import find, promote, add


def post():
    return jsonify(add(request.get_json(), False))


def post_candidate():
    return jsonify(add(request.get_json(), True))


def get():
    return jsonify(
        find(
            request.args.get("event_id"),
            request.args.get("name"),
            request.args.get("effect"),
            request.args.get("namespace"),
            False,
            request.args.get("start"),
            request.args.get("end"),
        )
    )


def get_candidate():
    return jsonify(
        find(
            request.args.get("event_id"),
            request.args.get("name"),
            request.args.get("effect"),
            request.args.get("namespace"),
            True,
            request.args.get("start"),
            request.args.get("end"),
        )
    )


def promote_candidate():
    return jsonify(promote(request.get_json()))
