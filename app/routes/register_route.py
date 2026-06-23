from flask import Blueprint

from app.controllers import register_controller as ctrl

register_bp = Blueprint("register", __name__, url_prefix="/auth/register")


@register_bp.route("", methods=["POST"])
def create_student():
    return ctrl.create_student()

