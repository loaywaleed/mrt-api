"""
app routes
"""

from flask import jsonify, request
from . import views, events
from .events import update_voltage_range_current, update_speed


@views.route("/voltage_current_range", strict_slashes=False, methods=["POST"])
def voltage_current_range():
    """
    Receives voltage, current, and range and updates them on the dashboard
    """
    data = request.json
    update_voltage_range_current(data)
    return jsonify(data)


# Tbd
@views.route("/speed", strict_slashes=False, methods=["POST"])
def speed():
    """
    Receives speed, calculates rpm, then update both on the dashboard
    """
    data = request.json
    update_speed(int(data.get('speed')))
    return jsonify(data)


@views.route("/gps_travelled", strict_slashes=False, methods=["POST"])
def gps_travelled_email():
    """"
    """
    data = request.json
    update_voltage(int(data.get('voltage')))
    return jsonify(data)


@views.route("/blinkers_temperates", strict_slashes=False, methods=["POST"])
def post_voltage():
    data = request.json
    update_voltage(int(data.get('voltage')))
    return jsonify(data)
