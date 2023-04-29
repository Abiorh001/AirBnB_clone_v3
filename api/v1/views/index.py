#!/usr/bin/python3

"""index for flask app using blueprint"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    """function that return status of an api response"""

    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def obj_stats():
    """function to return each object inside the models"""

    my_dict = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    return jsonify(my_dict)
