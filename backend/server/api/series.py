from flask import jsonify
from resource.data_node import find_series


def search():
    return jsonify(find_series())
