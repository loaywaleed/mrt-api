"""
app routes
"""

from flask import Flask, Blueprint, jsonify


views = Blueprint("views", __name__)


@views.route("/voltage", strict_slashes=False, methods=["GET"])
def voltage():
    # socketio.emit('voltage', {'data': '12 V'})
    print("message sent")
    return jsonify({"data": "12 V"})
