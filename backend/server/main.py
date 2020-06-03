from flask_cors import CORS
import os
import connexion

if __name__ == "__main__":
    app = connexion.FlaskApp(
        __name__, port=os.environ.get("API_PORT"), specification_dir="openapi/"
    )

    CORS(app.app)

    swagger_url = "http://{host}:{port}/v1".format(
        host=os.environ.get("API_HOST"), port=os.environ.get("API_PORT")
    )

    # CORS(app)
    app.add_api(
        "specs.yaml",
        arguments={
            "title": "Capitol Tracker Python API",
            "servers": [{"url": swagger_url}],
        },
    )
    app.run(debug=True, host="0.0.0.0")
