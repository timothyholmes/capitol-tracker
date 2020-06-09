# Capitol Tracker

[![Build Status](https://travis-ci.com/timothyholmes/capitol-tracker.svg?branch=master)](https://travis-ci.com/timothyholmes/capitol-tracker)

Identifying trends in american politics with time series data.

https://data.fivethirtyeight.com/

## Docker

```
docker-compose up --build
```

## Development

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

```
docker-compose up influxdb rabbit
```

### Backend

Run server:
```
cd ./backend/
poetry install
API_HOST=localhost API_PORT=5000 INFLUXDB_HOST=localhost poetry run python server/main.py
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
API_HOST=localhost API_PORT=5000 INFLUXDB_HOST=localhost poetry run python server/main.py
```