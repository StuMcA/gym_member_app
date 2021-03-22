from flask import Flask, redirect, request, render_template, Blueprint
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
from models.gym_class import GymClass
from models.member import Member

gym_class_blueprint = Blueprint("gym_class", __name__)

@gym_class_blueprint.route('/classes')
def classes():
    gym_classes = gym_class_repository.select_all()
    return render_template('/gym_classes/index.html', title="Classes", classes=gym_classes)

@gym_class_blueprint.route('/classes/<id>')
def gym_class(id):
    gym_class = gym_class_repository.select(id)
    members = member_repository.select_all()
    attendees = gym_class_repository.members(gym_class)
    return render_template('/gym_classes/show.html', title=f"{gym_class.class_type} with {gym_class.instructor}", gym_class=gym_class, members=members, attendees=attendees)

@gym_class_blueprint.route('/classes/<id>/addmember')
def add_member(id):
    gym_class = gym_class_repository.select(id)
    attendee = member_repository.select(request.form["id"])
    gym_class_repository.add_member(gym_class, attendee)

    return redirect('/classes/<id>')

@gym_class_blueprint.route('/classes/<id>/edit')
def edit_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('/gym_classes/edit.html', title="Edit class", gym_class=gym_class)

@gym_class_blueprint.route('/classes/<id>', methods=['POST'])
def update_class(id):
    updated_class = GymClass(
        request.form['class_type'],
        request.form['instructor'],
        request.form['date'],
        request.form['time'],
        request.form['duration'],
        request.form['location'],
        request.form['capacity']
    )
    gym_class_repository.update(updated_class)
    return redirect(f'classes/{id}')

# New class
@gym_class_blueprint.route('/classes/new')
def new_class():
    return render_template('/gym_classes/new.html', title="Add new class")

# Create class
@gym_class_blueprint.route('/classes/create', methods = ['POST'])
def create_class():
    new_gym_class = GymClass(
         request.form['class_type'],
        request.form['instructor'],
        request.form['date'],
        request.form['time'],
        request.form['duration'],
        request.form['location'],
        request.form['capacity']
    )
    gym_class_repository.save(new_gym_class)
    return redirect('/classes')
    
# Delete class
@gym_class_blueprint.route('/classes/<id>/delete', methods=['POST'])
def destroy_class(id):
    gym_class_repository.delete(id)
    return redirect('/classes')