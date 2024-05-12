"""
app routes
"""

from flask import Flask, Blueprint, jsonify, request


views = Blueprint("views", __name__)


@views.route("/voltage", strict_slashes=False, methods=["GET"])
def get_voltage():
    return jsonify({"data": "12 V"})


@views.route("/voltage", strict_slashes=False, methods=["POST"])
def post_voltage():
    # socketio.emit('voltage', {'data': '12 V'})
    data = request.json
    print("message sent")
    return jsonify(data)
