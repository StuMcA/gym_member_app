from flask import Blueprint, render_template, request, redirect
import repositories.member_repository as member_repository

member_blueprint = Blueprint("members", __name__)

@member_blueprint.route('/members')
def members():
    all_members = member_repository.select_all()
    return render_template('/members/index.html', title="Members", members=all_members)

@member_blueprint.route('/members/new')
def new_member():
    return render_template('/members/new.html', title="Add new member")

@member_blueprint.route('members/create', methods=['POST'])
def create_member():
    member = Member(
        request.form['first_name'],
        request.form['last_name'],
        request.form['date_of_birth']
    )
    member_repository.save(member)
    return redirect('/members')