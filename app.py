from flask import Flask, request, url_for,render_template, redirect
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
    remind = {}
    if(request.is_json):
        remind = json.loads(request.data)
        remind['startTime'] =  datetime.datetime.strptime(remind['startTime'], '%Y-%m-%d %H:%M:%S.%f')
        remind['endTime'] =  datetime.datetime.strptime(remind['endTime'], '%Y-%m-%d %H:%M:%S.%f')
        reminder = Reminder(**remind)
        db.session.add(reminder)
        db.session.commit() 
        return json.loads(request.data)
    else:
        print(request.form['text'])
        print(request.form['startDate'])
        print(request.form['endDate'])
        remind['reminderText'] = request.form['text']
        remind['startTime'] = datetime.datetime.strptime(request.form['startDate'], '%Y-%m-%dT%H:%M')
        remind['endTime'] = datetime.datetime.strptime(request.form['endDate'], '%Y-%m-%dT%H:%M')
        remind['isActive'] = True if (request.form['isActive'] == 'True') else False
        print(remind['isActive'])
        reminder = Reminder(**remind)
        db.session.add(reminder)
        db.session.commit() 
        return redirect(url_for('getReminders'))
        
        


@app.get('/addReminder')
def addReminderform():
    return render_template('reminderForm.html')


@app.delete('/deleteReminder/<int:id>')
def deleteReminder(id):
    try:
        reminder = Reminder.query.filter_by(id=id).first()
        db.session.delete(reminder)
        db.session.commit()
    except Exception:
        print(Exception)
    finally:
        return f'Deleted id: {reminder}'
