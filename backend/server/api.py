import flask
import requests
import math
from flask import jsonify, request
from flask_cors import CORS
from resource.poll_list import parse_poll_list
from resource.data_node import create_data_node, search, find_measurements, find_series

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route("/v1/data-node", methods=["PUT"])
def put_data_node():
    if request.method == "PUT":
        payload = request.get_json()

        create_data_node(
            payload["measurement"], payload["tags"], payload["fields"], payload["time"],
        )

        return jsonify(payload)


@app.route("/v1/data-node/batch", methods=["PUT"])
def put_data_node_batch():
    if request.method == "PUT":
        payload = request.get_json()

        for node in payload:
            create_data_node(
                node["measurement"], node["tags"], node["fields"], node["time"],
            )

        return jsonify(payload)


@app.route("/v1/measurements", methods=["GET"])
def get_measurements():
    if request.method == "GET":
        return jsonify(find_measurements())


@app.route("/v1/series", methods=["GET"])
def get_series():
    if request.method == "GET":
        return {"hello": "world"}
        # return jsonify(find_series())


@app.route("/v1/resources/congress-outlook", methods=["PUT", "GET"])
def congress_outlook():
    if request.method == "PUT":
        r = requests.get(
            "https://projects.fivethirtyeight.com/generic-ballot-data/generic_polllist.csv"
        )
        file = open("assets/pollList.csv", "w")
        file.write(r.text)
        file.close()

        payload = []
        for poll_list_node in parse_poll_list():
            payload.append(
                {
                    "measurement": "congressional_outlook",
                    "tags": {"party": "democrat"},
                    "fields": {"percentage": poll_list_node.adjusted_dem},
                    "time": poll_list_node.createddate,
                }
            )

            payload.append(
                {
                    "measurement": "congressional_outlook",
                    "tags": {"party": "republican"},
                    "fields": {"percentage": poll_list_node.adjusted_rep},
                    "time": poll_list_node.createddate,
                }
            )

        requests.put("http://localhost:5000/v1/data-node/batch", json=payload)

        return "", 201
    elif request.method == "GET":
        response = search()

        return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
