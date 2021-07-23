from models import Reminder
import datetime

def addTestReminder(db):
        test = Reminder(reminderText ='This is a Test Reminder',
        startTime = datetime.datetime.now(),
        endTime = datetime.datetime.now())
        db.session.add(test)
        db.session.commit() 