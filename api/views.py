"""
app routes
"""

from flask import jsonify, request
from . import views, events
from .events import update_voltage_range_current, update_speed_rpm, update_blinkers_temperature


@views.route("/voltage_current_range", strict_slashes=False, methods=["POST"])
def voltage_current_range():
    """
    Receives voltage, current, and range and updates them on the dashboard
    """
    data = request.json
    update_voltage_range_current(data)
    return jsonify(data)


# Tbd
@views.route("/speed_rpm_distance", strict_slashes=False, methods=["POST"])
def speed():
    """
    Receives speed, calculates rpm, then update both on the dashboard
    """
    data = request.json
    update_speed_rpm_distance(data)
    return jsonify(data)


@views.route("/blinkers_temperature", strict_slashes=False, methods=["POST"])
def post_voltage():
    data = request.json
    update_blinkers_temperature(data)
    return jsonify(data)


@views.route("/gps", strict_slashes=False, methods=["POST"])
def gps_travelled_email():
    """"
    """
    data = request.json
    update_gps(data)
    return jsonify(data)
