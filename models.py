from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reminderText = db.Column(db.String(200), nullable=False)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=True)
    isActive = db.Column(db.Boolean, default=True)

    # def __init__(self, id, reminder, start, end, active):
    #     self.id

    def __repr__(self):
        return '<Reminder %s>' % self.reminderText
