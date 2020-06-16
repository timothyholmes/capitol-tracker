from models.data_node import DataNode


def find(measurement):
    data = DataNode.get_events(measurement)

    return list(data)
