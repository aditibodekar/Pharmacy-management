from flask import Blueprint, jsonify

report_bp = Blueprint("report", __name__)

@report_bp.route("/reports")
def reports():
    return jsonify({"message": "Report route working"})