"""
app routes
"""

from flask import jsonify, request
from . import views, events
from .events import update_voltage


@views.route("/voltage", strict_slashes=False, methods=["POST"])
def post_voltage():
    data = request.json
    update_voltage(int(data.get('voltage')))
    return jsonify(data)
