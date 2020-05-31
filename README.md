# Capitol Tracker

[![Build Status](https://travis-ci.com/timothyholmes/capitol-tracker.svg?branch=master)](https://travis-ci.com/timothyholmes/capitol-tracker)

Python + React playground with FiveThirtyEight data sets.

https://data.fivethirtyeight.com/

## Pre req

### Create Network

Need to automate

```
docker network create capitol-network
```

### Running influxdb

```
docker run -p 8086:8086 \
      -v $PWD/influxdb.conf:/etc/influxdb/influxdb.conf:ro \
      --name influxdb \
      --network capitol-network \
      -e INFLUXDB_ADMIN_USER='root' \
      -e INFLUXDB_ADMIN_PASSWORD='password' \
      influxdb -config /etc/influxdb/influxdb.conf
```

## Build + Run

```
docker build . -t capitol-tracker
```

```
docker run --net capitol-network -p 5000:5000 capitol-tracker
```