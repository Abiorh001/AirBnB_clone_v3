#!/usr/bin/python3

"""flask main application script"""

from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from os import getenv
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def clean_up(exception=None):
    """close current session on database"""
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """handles 404 error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)
