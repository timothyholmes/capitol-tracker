import flask
from flask import request, jsonify
import csv


class PolllistNode:
    """Model for Polllist Data Node"""

    subgroup = ""
    modeldate = ""
    startdate = ""
    enddate = ""
    pollster = ""
    grade = ""
    samplesize = ""
    population = ""
    weight = ""
    influence = ""
    dem = ""
    rep = ""
    adjusted_dem = ""
    adjusted_rep = ""
    multiversions = ""
    tracking = ""
    url = ""
    poll_id = ""
    question_id = ""
    createddate = ""
    timestamp = ""

    def __init__(
        self,
        subgroup,
        modeldate,
        startdate,
        enddate,
        pollster,
        grade,
        samplesize,
        population,
        weight,
        influence,
        dem,
        rep,
        adjusted_dem,
        adjusted_rep,
        multiversions,
        tracking,
        url,
        poll_id,
        question_id,
        createddate,
        timestamp,
    ):
        self.subgroup = subgroup
        self.modeldate = modeldate
        self.startdate = startdate
        self.enddate = enddate
        self.pollster = pollster
        self.grade = grade
        self.samplesize = samplesize
        self.population = population
        self.weight = weight
        self.influence = influence
        self.dem = dem
        self.rep = rep
        self.adjusted_dem = adjusted_dem
        self.adjusted_rep = adjusted_rep
        self.multiversions = multiversions
        self.tracking = tracking
        self.url = url
        self.poll_id = poll_id
        self.question_id = question_id
        self.createddate = createddate
        self.timestamp = timestamp

    def serialize(self):
        return {
            "subgroup": self.subgroup,
            "modeldate": self.modeldate,
            "startdate": self.startdate,
            "enddate": self.enddate,
            "pollster": self.pollster,
            "grade": self.grade,
            "samplesize": self.samplesize,
            "population": self.population,
            "weight": self.weight,
            "influence": self.influence,
            "dem": self.dem,
            "rep": self.rep,
            "adjusted_dem": self.adjusted_dem,
            "adjusted_rep": self.adjusted_rep,
            "multiversions": self.multiversions,
            "tracking": self.tracking,
            "url": self.url,
            "poll_id": self.poll_id,
            "question_id": self.question_id,
            "createddate": self.createddate,
            "timestamp": self.timestamp,
        }


poll_list = []
with open(
    "./assets/congress-generic-ballot/generic_polllist.csv", newline=""
) as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
    line_count = 0
    for row in spamreader:
        if line_count == 0:
            line_count += 1
        else:
            node = PolllistNode(*row)
            poll_list.append(node)
            line_count += 1


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# A route to return all of the available entries in our catalog.
@app.route("/api/v1/resources/congress-outlook", methods=["GET"])
def congress_outlook():
    return jsonify(poll_list=[e.serialize() for e in poll_list])


app.run()
