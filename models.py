from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = "student"

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
        # Return a more comprehensive string with all columns
        return f"{f"ID: {self.id}, "
                f"First Name: {self.first_name}, "
                f"Last Name: {self.last_name}, "
                f"Email: {self.email}, "
                f"Password: {self.password}, "
                f"Gender: {self.gender}, "
                f"Hobbies: {self.hobbies}, "
                f"Country: {self.country}"}"

    # @staticmethod
    # def email_exists(email):
    #     # Check if the email already exists in the database
    #    return db.session.query(StudentModel).filter_by(email=email).first() is not None