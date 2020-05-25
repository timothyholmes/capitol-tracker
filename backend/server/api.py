import flask
import requests
import math
from flask import jsonify, request
from flask_cors import CORS
from resource.poll_list import parse_poll_list
from resource.data_node import create_data_node

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route("/v1/data-node", methods=["PUT"])
def put_data_node():
    if request.method == "PUT":
        payload = request.get_json()

        print(payload)

        create_data_node(
            payload["measurement"],
            payload["tags"],
            payload["fields"],
            payload["timestamp"],
        )

        return jsonify(payload)


@app.route("/v1/data-node/batch", methods=["PUT"])
def put_data_node_batch():
    if request.method == "PUT":
        payload = request.get_json()

        for node in payload:
            create_data_node(
                node["measurement"], node["tags"], node["fields"], node["timestamp"],
            )

        return jsonify(payload)


@app.route("/v1/resources/congress-outlook", methods=["PUT", "GET"])
def congress_outlook():
    if request.method == "PUT":
        # r = requests.get(
        #     "https://projects.fivethirtyeight.com/generic-ballot-data/generic_polllist.csv"
        # )
        # file = open("assets/pollList.csv", "w")
        # file.write(r.text)
        # file.close()

        payload = []
        for poll_list_node in parse_poll_list():
            payload.append(
                {
                    "measurement": "congressional_outlook",
                    "tags": {"party": "democrat"},
                    "fields": {"percentage": poll_list_node.adjusted_dem},
                    "timestamp": poll_list_node.createddate,
                }
            )

            payload.append(
                {
                    "measurement": "congressional_outlook",
                    "tags": {"party": "republican"},
                    "fields": {"percentage": poll_list_node.adjusted_rep},
                    "timestamp": poll_list_node.createddate,
                }
            )

        print(payload[0])
        requests.put("http://localhost:5000/v1/data-node", data=jsonify(payload[0]))

        return "", 201
    elif request.method == "GET":
        return jsonify(poll_list=[e.serialize() for e in parse_poll_list()])


app.run()
