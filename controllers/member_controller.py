from datetime import date, timedelta
from flask import Blueprint, render_template, request, redirect
import repositories.member_repository as member_repository
from models.member import Member

member_blueprint = Blueprint("members", __name__)


@member_blueprint.route('/members')
def members():
    all_members = member_repository.select_all()
    return render_template('/members/index.html', title="Members", members=all_members)


@member_blueprint.route('/members/<id>')
def show_member(id):
    member_found = member_repository.select(id)
    bookings = attendance_repository.select_by_member(member_found)
    classes_found = member_repository.classes(member_found)
    return render_template(
        'members/show.html', 
        title=f"Member #{member_found.id} - {member_found.first_name} {member_found.last_name}", 
        member=member_found, 
        classes=classes_found
    )


@member_blueprint.route('/members/new')
def new_member():
    sixteen_today_date = str(date.today() - timedelta(16*365.25))
    return render_template('/members/new.html', title="Add new member", date=sixteen_today_date)


@member_blueprint.route('/members/create', methods=['POST'])
def create_member():
    member = Member(
        request.form['first_name'],
        request.form['last_name'],
        request.form['date_of_birth']
    )
    member_repository.save(member)
    return redirect('/members')

@member_blueprint.route('/members/<id>/edit')
def edit_member(id):
    sixteen_today_date = str(date.today() - timedelta(16*365.25))
    member = member_repository.select(id)
    return render_template('members/edit.html', title=f"Edit member #{id}", member = member, date=sixteen_today_date)

@member_blueprint.route('/members/<id>', methods = ['POST'])
def update_member(id):
    updated_member = Member(
        request.form['first_name'],
        request.form['last_name'],
        request.form['date_of_birth'],
        request.form['membership'],
        id
    )
    member_repository.update(updated_member)
    return redirect(f'/members/{id}')

@member_blueprint.route('/members/<id>/delete', methods = ['POST'])
def destroy_member(id):
    member_repository.delete(id)
    return redirect('/members')