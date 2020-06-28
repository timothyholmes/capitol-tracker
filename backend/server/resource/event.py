from models.search import Search
from resource.data_node import create_data_node_batch

event_measurement = "event"

event_type_enum = dict(
    [
        ("start", 0),
        ("stop", 1),
        ("occurred", 2),
        (0.0, "start"),
        (1.0, "stop"),
        (2.0, "occurred"),
    ]
)


def add(payload, is_candidate):
    def add_measurement(dic):
        dic["measurement"] = event_measurement
        dic["fields"]["lifecycle"] = event_type_enum.get(
            dic.get("fields").get("lifecycle")
        )

        if is_candidate:
            dic["tags"]["candidate"] = 1
        else:
            dic["tags"]["candidate"] = 0

        return dic

    nodes = list(map(add_measurement, payload))

    create_data_node_batch(nodes)

    return payload


def find(fields, tags):
    search = Search(
        measurement="event",
        time={"start": "1770-06-19T20:07:36.356Z"},
        fields=fields,
        tags=tags,
    )

    tables = search.get()

    result = dict()

    for table in tables:
        for record in table.records:
            lifecycle_enum = dict([(1.0, "stop"), (0.0, "start")])

            if record.values["_value"] == 2.0:
                event = {}

                event["name"] = record.values["name"].replace("_", " ")
                event["effect"] = record.values["effect"].replace("_", " ")
                event["time"] = record.values["_time"]

                if "event_id" in record.values:
                    event["event_id"] = record.values["event_id"]

                result[record.values["name"]] = event
            elif record.values["_value"] < 2.0:
                event = {}

                if record.values["name"] in result:
                    event = result.get(record.values["name"])

                event["name"] = record.values["name"].replace("_", " ")
                event["effect"] = record.values["effect"].replace("_", " ")

                if not "time" in event:
                    event["time"] = {}

                event["time"][
                    lifecycle_enum.get(record.values["_value"])
                ] = record.values["_time"]

                result[record.values["name"]] = event

    return list(result.values())


def promote(event_ids):
    search = Search(
        measurement="event",
        time={"start": "1770-06-19T20:07:36.356Z"},
        fields={},
        tags={"event_id": event_ids},
    )

    tables = search.get()

    result = dict()

    for table in tables:
        for record in table.records:
            if record.values["_value"] == 2.0:
                event = {}

                event["tags"] = {
                    "name": record.values["name"].replace("_", " "),
                    "effect": record.values["effect"].replace("_", " "),
                }

                event["fields"] = {
                    record.values["_field"]: event_type_enum.get(
                        record.values["_value"]
                    )
                }

                print(record.values["_value"])

                event["time"] = record.values["_time"].strftime("%m/%d/%Y")

                if "event_id" in record.values:
                    event["tags"]["event_id"] = record.values["event_id"]

                result[record.values["name"]] = event
            elif record.values["_value"] < 2.0:
                event = {}

                if record.values["name"] in result:
                    event = result.get(record.values["name"])

                event["tags"] = {
                    "name": record.values["name".replace("_", " ")],
                    "effect": record.values["effect"].replace("_", " "),
                }

                event["fields"] = {
                    record.values["_field"]: event_type_enum.get(
                        record.values["_value"]
                    )
                }

                if not "time" in event:
                    event["time"] = {}

                event["time"][
                    event_type_enum.get(record.values["_value"])
                ] = record.values["_time"].strftime("%m/%d/%Y")

                result[record.values["name"]] = event

    print(list(result.values()))

    return add(list(result.values()), False)
