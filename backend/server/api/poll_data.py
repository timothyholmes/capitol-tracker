from flask import request, jsonify
from resource.data_node import find


def search():
    return jsonify(find())
