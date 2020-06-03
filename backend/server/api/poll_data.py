from flask import request, jsonify
from resource.data_node import find


def search():
    measurements = request.args.get("measurements")

    return jsonify(find(measurements.split(",")))
