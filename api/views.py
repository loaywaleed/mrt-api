"""
app routes
"""

from flask import jsonify, request
from . import views, events
from .events import update_voltage_current_soc_temp, update_speed_rpm_distance, update_blinkers, update_range_available


@views.route("/voltage_current_soc_temp", strict_slashes=False, methods=["POST"])
def voltage_current_soc():
    """
    Receives voltage, current, and soc and updates them on the dashboard
    """
    data = request.json
    update_voltage_current_soc_temp(data)
    return jsonify(data)


@views.route("/range", strict_slashes=False, methods=["POST"])
def range_available():
    """
    Receives voltage, current, and soc and updates them on the dashboard
    """
    data = request.json
    update_range_available(data)
    return jsonify(data)


@views.route("/speed_rpm_distance", strict_slashes=False, methods=["POST"])
def speed_rpm_distance():
    """
    Receives speed, rpm, distance then update both on the dashboard
    """
    data = request.json
    update_speed_rpm_distance(data)
    return jsonify(data)


@views.route("/blinkers", strict_slashes=False, methods=["POST"])
def blinkers_temperature():
    """
    Receives blinkers and temperature then update both on the dashboard
    """
    data = request.json
    update_blinkers(data)
    return jsonify(data)


# @views.route("/gps", strict_slashes=False, methods=["POST"])
# def gps_travelled_email():
#     """
#     Receives GPS data and updates them on the dashboard
#     """
#     data = request.json
#     update_gps(data)
#     return jsonify(data)
