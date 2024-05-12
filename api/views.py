"""
app routes
"""

from flask import jsonify, request
from . import views, events
from .events import update_voltage


@views.route("/voltage", strict_slashes=False, methods=["GET"])
def get_voltage():
    return jsonify({"data": "12 V"})


@views.route("/voltage", strict_slashes=False, methods=["POST"])
def post_voltage():
    update_voltage()
    data = request.json
    print("message sent")
    return jsonify(data)
