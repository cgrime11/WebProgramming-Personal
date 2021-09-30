from bottle import run, template, default_app
from bottle import get, post 
from bottle import debug
from bottle import request, response, redirect

from sessions import load_session, save_session

#####

import os , codecs, random
import json


import hashlib, codecs, os, random

passwords={

}

def bytes_to_str(b):
    s=str(codecs.encode(b, "hex"), "utf-8")
    assert type(s) is str
    return s

def str_to_bytes(s):
    b=codecs.decode(bytes(s, "utf-8"), "hex")
    assert type(b) is bytes
    return b

def encode_password(password):
    salt=os.urandom(32)
    key= hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    salt= bytes_to_str(salt)
    key= bytes_to_str(key)
    return f'{salt}:{key}'

def verify_password(password, encoding):
    salt, saved_key = encoding.split(':')
    salt= str_to_bytes(salt)
    password_key= hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    password_key= bytes_to_str(password_key)
    return saved_key == password_key

def new_profile(username, password):
    profile = {
        'username' : username,
        'password' : password
    }
    os.makedirs('data/profiles', exist_ok=True)
    with open(f'data/profiles/{username}.profile','w') as f:
        json.dump(profile, f)
    return profile

def load_profile(username):
    try:
        os.makedirs('data/profiles', exist_ok=True)
        with open(f'data/profiles/{username}.profile','r') as f:
            profile = json.load(f)
    except Exception as e:
        print(f'Profile error:{e}')
        profile = {}
    print('loaded profile = ',profile)
    return profile

def save_profile(profile):
    if 'username' not in profile:
        return
    username = profile['username']
    if username == 'guest':
        return
    os.makedirs('data/profiles', exist_ok=True)
    with open(f'data/profiles/{username}.profile','w') as f:
        json.dump(profile, f)
    
#####

def not_logged_in(session):
    if 'username' not in session:
        return True
    if session['username'] == 'guest':
        return True

def logged_in(session):
    return 'username' in session and session['username'] != 'guest'

@get('/')
@get('/hello')
def get_hello(name=None):
    # get the current session
    session = load_session(request)

    # if not logged in, redirect to someplace
    if not_logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', 'guest')

    # get the profile
    profile = load_profile(username)
    favcolor = profile.get('favcolor', 'not known')

    # save the session 
    print('saving loaded session',session)
    save_session(session, response)

    #return the requested web page
    return template('hello', name=username, color=favcolor)

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
    profile['password'] = encode_password(password)
    profile['encoding'] = encode_password(password)
    session['username'] = username

    # ssave the session
    save_profile(profile)
    save_session(session, response)

    #assume signup includes login
    redirect('/hello')

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
    favcolor = request.forms['favcolor']

    # get the profile for username
    profile = load_profile(username)
    print("loaded profile",profile)
    print('password',password)
    if not verify_password(password, profile.get('encoding','')):
        save_session(session, response)
        redirect('/login')

    print("logged in")

    # save user in the session
    session['username'] = username

    # get profile for the user
    profile['favcolor'] = favcolor

    save_profile(profile)
    save_session(session, response)
    redirect('/hello')

debug(True)
run(host='localhost', port=8068, reloader=True)
