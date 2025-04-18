from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flaskCRUD.models import StudentModel

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
print("psycopg2 is installed successfully!")



app = Flask(__name__, template_folder='flaskCRUD/templates')
# Initialize Flask app and SQLAlchemy


# MySQL Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:T5Y3BCHRAreDlVaFqX8OvAQcZcVuwbRE@dpg-cvmejo3e5dus73f2f8bg-a.oregon-postgres.render.com/student_nj09'
print("Database connected successfully!")

  # Update this string with your credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# Initialize the database
db = SQLAlchemy(app)


def create_tables():
    with app.app_context():
        db.create_all()
        print("Tables created successfully (if not existed before)!")
        return "Tables created successfully (if not existed before)!"

# Define StudentModel class to interact with the 'student' table
class StudentModel(db.Model):
    __tablename__ = 'student'  # Ensure this matches the name of your table in MySQL

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    hobbies = db.Column(db.String(), nullable=True)
    country = db.Column(db.String(80), nullable=False)

    def __init__(self, first_name, last_name, email, password, gender, hobbies, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.gender = gender
        self.hobbies = hobbies
        self.country = country
    

    def __repr__(self):
        return f"<Student(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"

# Routes for creating, displaying, updating, and deleting students
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Collect data from the form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobbies = ",".join(request.form.getlist('hobbies'))  # Hobbies as comma-separated string
        country = request.form['country']

        # Create a new student instance
        student = StudentModel(first_name=first_name, last_name=last_name, email=email, 
                               password=password, gender=gender, hobbies=hobbies, country=country)

        # Add and commit the new student to the database
        db.session.add(student)
        db.session.commit()

        # Redirect to the list of students after saving
        return redirect('/')

    return render_template('createpage.html')

@app.route('/')

def RetrieveList():
    #create student table if not exists
    create_tables()
    # Fetch all students from the database
    students = StudentModel.query.all()
    return render_template('datalist.html', students=students)



@app.route('/<int:id>')
def RetrieveStudent(id):
    # Fetch a specific student based on the ID
    student = StudentModel.query.get(id)
    if student:
        return render_template('data.html', student=student)
    return f"Student with ID = {id} does not exist."


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def update(id):
    # Fetch the student to edit
    student = StudentModel.query.get(id)
    if request.method == 'POST':
        if student:
            # Update the student details
            student.first_name = request.form['first_name']
            student.last_name = request.form['last_name']
            student.email = request.form['email']
            student.password = request.form['password']
            student.gender = request.form['gender']
            student.hobbies = ",".join(request.form.getlist('hobbies'))
            student.country = request.form['country']

            # Commit the changes to the database
            db.session.commit()
            return redirect('/')

    return render_template('update.html', student=student)


@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    # Fetch the student to delete
    student = StudentModel.query.get(id)
    if request.method == 'POST':
        if student:
            # Delete the student from the database
            db.session.delete(student)
            db.session.commit()
            return redirect('/')

    return render_template('delete.html')




# Run the application
if __name__ == '__main__':
    app.run()
