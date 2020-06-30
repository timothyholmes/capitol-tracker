from resource.poll_list import parse_poll_list
import requests
import os


def post():
    r = requests.get(
        "https://projects.fivethirtyeight.com/generic-ballot-data/generic_polllist.csv"
    )

    payload = []
    for poll_list_node in parse_poll_list(r.text):
        payload.append(
            {
                "measurement": "congressional_outlook",
                "tags": {"stance": "congressional_outlook.democrat"},
                "fields": {"percentage": poll_list_node["adjusted_dem"]},
                "time": poll_list_node["createddate"],
            }
        )

        payload.append(
            {
                "measurement": "congressional_outlook",
                "tags": {"stance": "congressional_outlook.republican"},
                "fields": {"percentage": poll_list_node["adjusted_rep"]},
                "time": poll_list_node["createddate"],
            }
        )

    batch_url = "http://{host}:{port}/v1/poll".format(
        host=os.environ.get("API_HOST"), port=os.environ.get("API_PORT")
    )

    requests.post(batch_url, json=payload)

    return "", 204
