from flask import Flask, render_template
from controllers.member_controller import member_blueprint
from controllers.gym_class_controller import gym_class_blueprint
from controllers.attendance_controller import attendance_blueprint
from controllers.instructor_controller import instructor_blueprint

app =Flask(__name__)
app.secret_key = 'lkajdsfbl3498'

app.register_blueprint(member_blueprint)
app.register_blueprint(gym_class_blueprint)
app.register_blueprint(attendance_blueprint)
app.register_blueprint(instructor_blueprint)

@app.route('/')
def index():
    return render_template('index.html', title="Welcome")

if __name__ == '__main__':
    app.run(debug=True)