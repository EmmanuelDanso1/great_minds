from db import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description}
