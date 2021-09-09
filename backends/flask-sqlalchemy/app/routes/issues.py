from flask import Blueprint, g, request, jsonify, current_app
from werkzeug.exceptions import NotFound

from ..models import Repo, Issue, User
from .helpers import session

bp = Blueprint(
    "routes.issues",
    __name__,
    url_prefix="/orgs/<int:org_id>/repos/<int:repo_id>/issues",
)

import code


@bp.route("", methods=["GET"])
@session
def index(org_id, repo_id):
    repo = g.session.query(Repo).filter_by(id=repo_id).one()
    current_app.oso.authorize(g.current_user, "list_issues", repo)
    return jsonify([issue.repr() for issue in repo.issues])


@bp.route("", methods=["POST"])
@session
def create(org_id, repo_id):
    payload = request.get_json(force=True)
    repo = g.session.query(Repo).filter_by(id=repo_id).one_or_none()
    current_app.oso.authorize(g.current_user, "create_issues", repo)
    issue = Issue(title=payload["title"], repo_id=repo.id)
    g.session.add(issue)
    g.session.commit()
    return issue.repr(), 201


@bp.route("/<int:issue_id>", methods=["GET"])
@session
def show(org_id, repo_id, issue_id):
    issue = g.session.query(Issue).filter_by(id=issue_id).one_or_none()
    current_app.oso.authorize(g.current_user, "read", issue)
    return issue.repr()
