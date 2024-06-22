"""
app routes
"""

from flask import jsonify, request
from . import views, events
from .events import update_voltage_range_current


@views.route("/voltage_current_range", strict_slashes=False, methods=["POST"])
def voltage_current_range():
    """
    Receives voltage, current, and range and updates them ont the screen
    """
    data = request.json
    print(data)
    update_voltage_range_current(data)
    return jsonify(data)



# Tbd
@views.route("/speed", strict_slashes=False, methods=["POST"])
def speed():
    data = request.json
    update_voltage(int(data.get('voltage')))
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
