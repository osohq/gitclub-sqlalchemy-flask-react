from flask import Blueprint, g, jsonify, current_app

from ..models import User, Repo
from .helpers import session, distinct

bp = Blueprint("routes.users", __name__, url_prefix="/users")


@bp.route("/<int:user_id>", methods=["GET"])
@session
def show(user_id):
    user = g.session.query(User).filter_by(id=user_id).one_or_none()
    current_app.oso.authorize(g.current_user, "read_profile", user)
    return user.repr()


@bp.route("/<int:user_id>/repos", methods=["GET"])
@session
def index(user_id):
    user = g.session.query(User).filter_by(id=user_id).one_or_none()
    current_app.oso.authorize(g.current_user, "read_profile", user)
    repos = current_app.oso.authorized_resources(g.current_user, "read", Repo)
    return jsonify(distinct([repo.repr() for repo in repos]))
