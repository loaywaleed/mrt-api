"""
app routes
"""

from flask import jsonify, request
from . import views, events
from .events import update_voltage_current_soc, update_speed_rpm_distance, update_blinkers_temperature, update_gps


@views.route("/voltage_current_soc", strict_slashes=False, methods=["POST"])
def voltage_current_range():
    """
    Receives voltage, current, and soc and updates them on the dashboard
    """
    data = request.json
    update_voltage_current_soc(data)
    return jsonify(data)


# Tbd
@views.route("/speed", strict_slashes=False, methods=["POST"])
def speed():
    """
    Receives speed, then update both on the dashboard
    """
    data = request.json
    update_speed_rpm_distance_soc(data)
    return jsonify(data)


@views.route("/blinkers_temperature", strict_slashes=False, methods=["POST"])
def post_voltage():
    """
    Receives blinkers and temperature then update both on the dashboard
    """
    data = request.json
    update_blinkers_temperature(data)
    return jsonify(data)


@views.route("/gps", strict_slashes=False, methods=["POST"])
def gps_travelled_email():
    """
    Receives GPS data and updates them on the dashboard
    """
    data = request.json
    update_gps(data)
    return jsonify(data)
