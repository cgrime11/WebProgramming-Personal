import os 
import json
from bottle import run, template, default_app
from bottle import get, post 
from bottle import debug
from bottle import request, response, redirect

from sessions import load_session, save_session
from profiles import load_profile, save_profile
from passwords import encode_password, verify_password

import dataset


def logged_in(session):
    # return 'username' in session and session['username'] != 'guest'
    return session.get('username', 'guest') != 'guest'

@get('/')
@get('/index')
def get_index(name=None):
    # get the current session
    session = load_session(request)

    # if not logged in, redirect to someplace
    if not logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', 'guest')

    # load the items
    db = dataset.connect('sqlite:///database.db')
    notes = db['notes']
    items = [dict(item) for item in notes.find(user=username)]
    print(list(items))

    # save the session 
    print('saving loaded session',session)
    save_session(session, response)

    #return the requested web page
    return template('index', name=username, items=items)

@get('/signup')
def get_login():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('signup', message='')

@post('/signup')
def post_signup():
    # load the session
    session = load_session(request)

    # get the form information
    username = request.forms['username']
    password = request.forms['password']
    password_again = request.forms['password_again']

    # get the profile if there is one
    profile = load_profile(username)
    print('signup starting ',profile)

    # see if it's an established profile
    if 'username' in profile:
        print("ALREADY A CUSTOMER")
        save_session(session, response)
        redirect('/signup')

    # save the profile
    profile['username'] = username
    profile['encoding'] = encode_password(password)
    save_profile(profile)

    # save_session
    session['username'] = username
    save_session(session, response)

    # assume signup includes implicit login
    redirect('/index')

@get('/login')
def get_login():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('login', message='')

@post('/login')
def post_login():
    # load the session
    session = load_session(request)

    # get the form information
    username = request.forms['username']
    password = request.forms['password']

    # get the profile for username
    profile = load_profile(username)
    print("loaded profile",profile)
    print('password',password)

    if verify_password(password, profile.get('encoding',':')):
        print("logged in")

        # save user in the session
        session['username'] = username

        # save profile for the user
        profile['favcolor'] = 'blue'
        save_profile(profile)

        # save session
        save_session(session, response)
        redirect('/index')

    else:
        print("not logged in")
        save_session(session, response)
        redirect('/login')

@get('/create')
def get_create():
    session = load_session(request)
    # if not logged in, redirect to someplace
    if not logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', 'guest')

    save_session(session, response)
    return template('create', name=username)

@post('/create')
def post_create():
    # load the session
    session = load_session(request)

    # if not logged in, redirect to someplace
    if not logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', 'guest')

    # get the form information
    note = request.forms['note']

    # Store the new note
    print("the new note is ", note)
    item = {
        "user":username, 
        "note":note
    }
    db = dataset.connect('sqlite:///database.db')
    notes = db['notes']
    notes.insert(item)

    # save session
    save_session(session, response)
    redirect('/index')

@get('/edit/<id>')
def get_edit(id):
    session = load_session(request)
    # if not logged in, redirect to someplace
    if not logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', None)

    # load the items
    db = dataset.connect('sqlite:///database.db')
    notes = db['notes']
    items = [dict(item) for item in notes.find(id=id, user=username)]
    if len(items) != 1:
        print("we have a problem")
        redirect("/login")
    print(items[0])
    note = items[0]['note']

    # display the edit page
    save_session(session, response)
    return template('edit', name=username, id=id, value=note)

@post('/edit/<id>')
def post_edit(id):
    # load the session
    session = load_session(request)

    # if not logged in, redirect to someplace
    if not logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', None)

    # get the form information
    note = request.forms['note']

    # Store the new note
    print("the updated note is ", note)
    item = {
        'id':id,
        "user":username, 
        "note":note
    }
    db = dataset.connect('sqlite:///database.db')
    notes = db['notes']
    notes.update(item,['id','user'])

    # save session
    save_session(session, response)
    redirect('/index')

@get('/delete/<id>')
#@get('/delete')
def get_delete(id): #=None):
    # load the session
    session = load_session(request)

    # if not logged in, redirect to someplace
    if not logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', None)

    #if not id:
    #    id = request.params.get('id',None)

    if not id:
        redirect('/index')

    print("delete ID = ",id)
    db = dataset.connect('sqlite:///database.db')
    notes = db['notes']
    notes.delete(user=username, id=id)

    # save session
    save_session(session, response)
    redirect('/index')

debug(True)
run(host='localhost', port=8068, reloader=True)
