from flask import Flask, redirect, request, render_template, Blueprint
import repositories.gym_class_repository as gym_class_repository

gym_class_blueprint = Blueprint("gym_class", __name__)

@gym_class_blueprint.route('/classes')
def classes():
    gym_classes = gym_class_repository.select_all()
    return render_template('gym_classes/index.html', title="Classes", classes=gym_classes)