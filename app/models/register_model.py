from app.extensions import db
class Student(db.Model):
    __tablename__ = "students"

    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password=db.Column(db.Text(),nullable=False)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "email": self.email,
        }       
          
