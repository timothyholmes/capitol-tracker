from models.search import Search


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
                    event["event_id"] = record.values["event_id"].replace("_", " ")

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
