from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialize db
db = SQLAlchemy(app)
# initialize ma
ma = Marshmallow(app)


#
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    classs = db.Column(db.String(20), unique=True)
    subject = db.Column(db.String(30), primaey_key=True, )
    uniform_color = db.Column(db.String(20), unique=True)


def __init__(self, name, classs, subject, uniform_color):
    self.name = name
    self.classs = classs
    self.subject = subject
    self.uniform_color = uniform_color


# schema
class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'classs', 'subject', 'uniform_color')


#

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# create a student
@app.route('/school', methods=['POST'])
def add_student():
    name = request.json['name']
    classs = request.json['classs']
    subject = request.json['subject']
    uniform_color = request.json['uniform_color']

    new_student = Student(name=name, classs=classs, subject=subject, uniform_color=uniform_color)
    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)


# Get all student details

@app.route('/school', methods=['GET'])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)


# Get single student details


@app.route('/school/<id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    return student_schema.jsonify(student)


# update a student
@app.route('/school/<id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)

    name = request.json['name']
    classs = request.json['classs']
    subject = request.json['subject']
    uniform_color = request.json['uniform_color']

    student.name = name
    student.classs = classs
    student.subject = subject
    student.uniform_color = uniform_color

    db.session.commit()

    return student_schema.jsonify(student)


# Delete Student details

@app.route('/school/<id>', methods=['DELETE'])
def delete_students(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return student_schema.jsonify(student)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
