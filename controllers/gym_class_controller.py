from flask import Flask, redirect, request, render_template, Blueprint
import repositories.gym_class_repository as gym_class_repository
from models.gym_class import GymClass

gym_class_blueprint = Blueprint("gym_class", __name__)

@gym_class_blueprint.route('/classes')
def classes():
    gym_classes = gym_class_repository.select_all()
    return render_template('/gym_classes/index.html', title="Classes", classes=gym_classes)

@gym_class_blueprint.route('/classes/<id>')
def gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('/gym_classes/show.html', title=f"{gym_class.class_type} with {gym_class.instructor}", gym_class=gym_class)

# Edit classes
@gym_class_blueprint.route('/classes/<id>/edit')
def edit_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('/classes/edit.html', title="Edit class", gym_class=gym_class)

# Update classes
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
    return render_template('/classes/new.html', title="Add new class")

# Create class


# Delete class