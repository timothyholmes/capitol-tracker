import flask
import requests
from flask import jsonify
from resource.poll_list import parse_poll_list

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/api/v1/resources/congress-outlook", methods=["GET"])
def congress_outlook():
    return jsonify(poll_list=[e.serialize() for e in parse_poll_list()])


@app.route("/api/v1/resources/download", methods=["GET"])
def download_file():
    r = requests.get(
        "https://projects.fivethirtyeight.com/generic-ballot-data/generic_polllist.csv"
    )
    file = open("assets/pollList.csv", "w")
    file.write(r.text)
    file.close()
    return "", 201


app.run()
