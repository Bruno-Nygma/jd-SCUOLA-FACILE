from flask import Flask
from flask_cors import CORS
from controller.student_controller import student_bp
from controller.docente_controller import docente_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(student_bp)
app.register_blueprint(docente_bp)

@app.route("/")
def home():
    return "Scuola semplice full-stack: v1.0"


if __name__ == "__main__":
    app.run(debug = True)