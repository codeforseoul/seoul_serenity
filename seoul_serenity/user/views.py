# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for
from flask.ext.login import login_required

from seoul_serenity.user.models import User, User_project
from seoul_serenity.project.models import Project

blueprint = Blueprint("user", __name__, url_prefix='/users',
                        static_folder="../static")


# TODO 서영태 : Pagination 적용 (MUST)
@blueprint.route("/")
@login_required
def members():
	users = User.query.all()
	return render_template("users/members.html", users=users)

@blueprint.route("/<int:user_id>")
@login_required
def member(user_id):
	user = User.query.filter_by(id=user_id).first_or_404()
	projects = []
	user_projects = User_project.query.filter_by(u_id=user.id)
	for user_project in user_projects:
		project = Project.get_by_id(user_project.p_id)
		projects.append(project)
	return render_template("users/member.html", user=user, projects=projects)


@blueprint.route("/assign/<int:user_id>")
def assign(user_id):
	projects = Project.query.all()
	return render_template("users/assign.html", projects=projects, user_id=user_id)

@blueprint.route("/<int:user_id>/assign/<int:project_id>", methods=['GET', 'POST'])
def assigned(user_id, project_id):
	find_assign = User_project.query.filter_by(u_id=user_id, p_id=project_id).first()
	if find_assign is None:
		new_assign = User_project.create(u_id=user_id, p_id=project_id)	
	return redirect(url_for("user.member", user_id=user_id))
