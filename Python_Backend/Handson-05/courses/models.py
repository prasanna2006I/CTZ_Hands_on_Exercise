from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Department(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )


class Course(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    code = db.Column(
        db.String(20),
        nullable=False
    )

    credits = db.Column(
        db.Integer,
        nullable=False
    )

    department_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "department.id"
        )
    )

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "credits": self.credits
        }

class Student(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )


class Enrollment(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "student.id"
        )
    )
    course_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "course.id"
        )
    )