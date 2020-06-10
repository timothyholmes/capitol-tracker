# Capitol Tracker

[![Build Status](https://travis-ci.com/timothyholmes/capitol-tracker.svg?branch=master)](https://travis-ci.com/timothyholmes/capitol-tracker)

Identifying trends in american politics with time series data.

https://data.fivethirtyeight.com/

## Cloud

The app is deployed on AWS.

API: http://api.capitol-tracker.tech/
UI: http://ui.capitol-tracker.tech/

## Development Setup

[Contribution steps](https://github.com/timothyholmes/capitol-tracker/wiki/Contribution-Model).

### Required Tools

- [pyenv](https://github.com/pyenv/pyenv)
```
brew update
brew install pyenv
```
- [poetry](https://python-poetry.org/)
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
- [Docker](https://www.docker.com/)
- Node + npm (install with [nvm](https://github.com/nvm-sh/nvm))
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```

### Running influx

The database is influxdb cloud, for running locally [see the wiki.](https://github.com/timothyholmes/capitol-tracker/wiki/Running-Influx-Cloud)

### Backend

For more information on the required start up env vars, see the [running influx guide]((https://github.com/timothyholmes/capitol-tracker/wiki/Running-Influx-Cloud)).

Run server:
```
cd ./backend/

poetry install

INFLUXDB_HOST=http://localhost:9999 \
INFLUXDB_TOKEN=iLaNVEgsozy00H0k32eKFS5cmLIgJ1As2QCsH7NrsVV7IfWoe8f_ptxzeXyHAJ7jefusivlyGLnnhhYXvCJy-Q== \
INFLUXDB_ORG=05d3ddc654a5d000 \
INFLUXDB_BUCKET=05d3de9089e5d000 \
API_PORT=5000 \
API_HOST=localhost \
poetry run python server/main.py
```

Run tests and formatter:
```
poetry run ptw --beforerun "black ./server"
```

OpenAPI documentation is found at http://localhost:5000/v1/ui/.

`POST` the `/workers/*` routes in the UI to seed influx with poll data.

### Frontend

```
cd ./frontend/
npm install
npm start
```

You can override which API the frontend points to with env vars. The default is http://localhost:5000.
```
REACT_APP_API_PROTOCOL=http \
REACT_APP_API_HOST=localhost \
REACT_APP_API_PORT=5000 \
npm start
```