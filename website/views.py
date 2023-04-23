from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, User
from . import db
import json
import UVLight
import ServoMotor
import StepperMotor
import time

#LOCKER DECLARATIONS
#locker_amount = 1 + 4
#d = {}
#for lockerid in range(1,locker_amount):
#    d["lockerid{0}".format(lockerid)] = None
status1 = False
status2 = False
status3 = False
status4 = False
lockerid1 = None
lockerid2 = None
lockerid3 = None
lockerid4 = None

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    global status1
    global status2
    global status3
    global status4
    #if lockerid1 != None and lockerid2 != None:
        #status1=True
        #status2=True
        #return render_template("home.html", user=current_user, status1=status1, status2=status2)
    if lockerid1 != None:
        status1 = True
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)
    if lockerid2 != None:
        status2 = True
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)
    if lockerid3 != None:
        status3 = True
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)
    if lockerid4 != None:
        status4 = True
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)
    else:
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)

@views.route("/OpenButton")
def OpenButton():
    StepperMotor.c_lock()
    time.sleep(1)
    ServoMotor.ServoMotorClose()
    return render_template("locker1.html", user=current_user)

@views.route("/CloseButton")
def CloseButton():
    ServoMotor.ServoMotorOpen()
    time.sleep(0.5)
    StepperMotor.o_lock()
    time.sleep(1)
    UVLight.lightsOn()
    return render_template("locker1.html", user=current_user)

@views.route('/mylocker')
@login_required
def mylocker():
    x = current_user.lockernum
    y = str(x)
    if (current_user.lockernum != None):
        return render_template("locker" + y + ".html", user=current_user)
    else:
        flash('You have no registered locker.', category='error')
        return render_template("home.html", user=current_user)
    #return render_template("home.html", user=current_user)

@views.route('/locker1')
def locker1():
    global status1
    global status2
    global status3
    global status4
    if current_user.lockernum == 1 or current_user.lockernum == None:   #checks if user has locker registered already
        if lockerid1 == None or lockerid1 == current_user.id:
            if lockerid1 == None:                                   #this is just to have an initial welcome message at registration
                flash('You have registered Locker 1.', category='success')
                return redirect(url_for('views.templock1'))
            else:                                                   #no welcome message because user is returning to registered locker
                return redirect(url_for('views.templock1'))
        else:
            flash('Locker 1 is unavailable. Please select an available locker.', category='error')
            return render_template("home.html", user=current_user, status1=True, status2=status2, status3=status3, status4=status4)
    else:
        flash('You already have a registered locker.', category='error')
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)
    
@views.route('/templock1')
def templock1():
    global lockerid1
    lockerid1 = current_user.id
    user = User.query.get(current_user.id)
    user.lockernum = 1
    db.session.commit()
    return render_template("locker1.html", user=current_user)

@views.route('/templock1close')
def templock1close():
    global lockerid1
    global status1
    lockerid1 = None
    status1 = False
    user = User.query.get(current_user.id)
    user.lockernum = None
    db.session.commit()
    flash('You are now unregistered from Locker 1.', category='success')
    #return render_template("home.html", user=current_user)
    return redirect(url_for('views.home'))

@views.route('/locker2')
def locker2():
    global status1
    global status2
    global status3
    global status4
    if current_user.lockernum == 2 or current_user.lockernum == None:
        if lockerid2 == None or lockerid2 == current_user.id:
            if lockerid2 == None:                                   #this is just to have an initial welcome message at registration
                flash('You have registered Locker 2.', category='success')
                return redirect(url_for('views.templock2'))
            else:                                                   #no welcome message because user is returning to registered locker
                return redirect(url_for('views.templock2'))
        else:
            flash('Locker 2 is unavailable. Please select an available locker.', category='error')
            return render_template("home.html", user=current_user, status1=status1, status2=True, status3=status3, status4=status4)
    else:
        flash('You already have a registered locker.', category='error')
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)

@views.route('/templock2')
def templock2():
    global lockerid2
    lockerid2 = current_user.id
    user = User.query.get(current_user.id)
    user.lockernum = 2
    db.session.commit()
    return render_template("locker2.html", user=current_user)

@views.route('/templock2close')
def templock2close():
    global lockerid2
    global status2
    lockerid2 = None
    status2 = False
    user = User.query.get(current_user.id)
    user.lockernum = None
    db.session.commit()
    flash('You are now unregistered from Locker 2.', category='success')
    return redirect(url_for('views.home'))

@views.route('/locker3')
def locker3():
    global status1
    global status2
    global status3
    global status4
    if current_user.lockernum == 3 or current_user.lockernum == None:
        if lockerid3 == None or lockerid3 == current_user.id:
            if lockerid3 == None:                                   #this is just to have an initial welcome message at registration
                flash('You have registered Locker 3.', category='success')
                return redirect(url_for('views.templock3'))
            else:                                                   #no welcome message because user is returning to registered locker
                return redirect(url_for('views.templock3'))
        else:
            flash('Locker 3 is unavailable. Please select an available locker.', category='error')
            return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=True, status4=status4)
    else:
        flash('You already have a registered locker.', category='error')
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)

@views.route('/templock3')
def templock3():
    global lockerid3
    lockerid3 = current_user.id
    user = User.query.get(current_user.id)
    user.lockernum = 3
    db.session.commit()
    return render_template("locker3.html", user=current_user)

@views.route('/templock3close')
def templock3close():
    global lockerid3
    global status3
    lockerid3 = None
    status3 = False
    user = User.query.get(current_user.id)
    user.lockernum = None
    db.session.commit()
    flash('You are now unregistered from Locker 3.', category='success')
    return redirect(url_for('views.home'))

@views.route('/locker4')
def locker4():
    global status1
    global status2
    global status3
    global status4
    if current_user.lockernum == 4 or current_user.lockernum == None:
        if lockerid4 == None or lockerid4 == current_user.id:
            if lockerid4 == None:                                   #this is just to have an initial welcome message at registration
                flash('You have registered Locker 4.', category='success')
                return redirect(url_for('views.templock4'))
            else:                                                   #no welcome message because user is returning to registered locker
                return redirect(url_for('views.templock4'))
        else:
            flash('Locker 4 is unavailable. Please select an available locker.', category='error')
            return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=True)
    else:
        flash('You already have a registered locker.', category='error')
        return render_template("home.html", user=current_user, status1=status1, status2=status2, status3=status3, status4=status4)

@views.route('/templock4')
def templock4():
    global lockerid4
    lockerid4 = current_user.id
    user = User.query.get(current_user.id)
    user.lockernum = 4
    db.session.commit()
    return render_template("locker4.html", user=current_user)

@views.route('/templock4close')
def templock4close():
    global lockerid4
    global status4
    lockerid4 = None
    status4 = False
    user = User.query.get(current_user.id)
    user.lockernum = None
    db.session.commit()
    flash('You are now unregistered from Locker 4.', category='success')
    return redirect(url_for('views.home'))

@views.route('/AboutUs')
def AboutUs():
    return render_template("AboutUs.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})