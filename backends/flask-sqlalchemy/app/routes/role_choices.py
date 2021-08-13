from flask import Blueprint, current_app, jsonify

from ..models import Org, Repo

bp = Blueprint("routes.role_choices", __name__)


@bp.route("/org_role_choices", methods=["GET"])
def org_roles():
    return jsonify(current_app.oso.policy.roles.for_resource(Org))


@bp.route("/repo_role_choices", methods=["GET"])
def repo_roles():
    return jsonify(current_app.oso.policy.roles.for_resource(Repo))
