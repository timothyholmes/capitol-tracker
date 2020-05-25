# Capitol Tracker

Python + React playground with FiveThirtyEight data sets.

https://data.fivethirtyeight.com/

### Running influxdb

```
docker run -p 8086:8086 \
      -v $PWD/influxdb.conf:/etc/influxdb/influxdb.conf:ro \
      --name influxdb \
      -e INFLUXDB_ADMIN_USER='root' \
      -e INFLUXDB_ADMIN_PASSWORD='password' \
      influxdb -config /etc/influxdb/influxdb.conf
```