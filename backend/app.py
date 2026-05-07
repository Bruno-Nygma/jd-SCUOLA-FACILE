from flask import Flask

from controller.student_controller import student_bp
from controller.teacher_controller import teacher_bp
# from controller.course_controller import corso_bp

app = Flask(__name__)

app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)
# app.register_blueprint(corso_bp)

# La 5000 è la default
if __name__ == "__main__":
    app.run(debug=True, port=5000)