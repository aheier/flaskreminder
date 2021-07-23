from flask import Flask, request, url_for,render_template
from flask.templating import render_template
from models import *
from tests import *
import json
import os


app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbdir/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

def create_tables():
    db.create_all()

@app.route('/')
def home():
    # addTestReminder(db)
    text = ''
    for reminder in Reminder.query.all():
        text += '<h1>%s</h1>' % reminder.reminderText
    return "<h1>Hello, From Flask!</h1>" + text

@app.get('/reminders')
def getReminders():
    reminders = Reminder.query.all()
    return render_template('Table.html',reminders = reminders)

@app.post('/addReminder')
def addReminder():
    remind = json.loads(request.data)
    remind['startTime'] =  datetime.datetime.strptime(remind['startTime'], '%Y-%m-%d %H:%M:%S.%f')
    remind['endTime'] =  datetime.datetime.strptime(remind['endTime'], '%Y-%m-%d %H:%M:%S.%f')
    reminder = Reminder(**remind)
    db.session.add(reminder)
    db.session.commit() 
    return json.loads(request.data)
