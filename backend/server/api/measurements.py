from flask import jsonify
from resource.data_node import find_measurements


def search():
    return jsonify(find_measurements())
