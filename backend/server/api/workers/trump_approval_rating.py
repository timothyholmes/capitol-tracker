from resource.poll_list import parse_poll_list
import requests
import os


def post():
    path = "trump_approval_rating"
    r = requests.get(
        "https://projects.fivethirtyeight.com/trump-approval-data/approval_polllist.csv"
    )

    payload = []
    for poll_list_node in parse_poll_list(r.text):
        payload.append(
            {
                "measurement": path,
                "tags": {"stance": "approve"},
                "fields": {"percentage": poll_list_node["adjusted_approve"]},
                "time": poll_list_node["createddate"],
            }
        )

        payload.append(
            {
                "measurement": path,
                "tags": {"stance": "disapprove"},
                "fields": {"percentage": poll_list_node["adjusted_disapprove"]},
                "time": poll_list_node["createddate"],
            }
        )

    batch_url = "http://{host}:{port}/v1/data-node".format(
        host=os.environ.get("API_HOST"), port=os.environ.get("API_PORT")
    )

    requests.post(batch_url, json=payload)

    return "", 204
