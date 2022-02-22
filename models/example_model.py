from .db import db

class Example(db.Model):
    __tablename__ = 'examples'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'title': self.title}
