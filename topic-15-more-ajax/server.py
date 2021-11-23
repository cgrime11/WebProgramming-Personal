import os 
import json
from bottle import run, template, default_app
from bottle import get, post 
from bottle import debug
from bottle import request, response, redirect

from sessions import load_session, save_session
from profiles import load_profile, save_profile
from passwords import encode_password, verify_password
import requests

def weather_info(zip):
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip},US&appid=c2451003d701ce487c3b210829edbc73")
    if result.status_code != 200:
        return None
    return result.json()

def logged_in(session):
    # return 'username' in session and session['username'] != 'guest'
    return session.get('username', 'guest') != 'guest'

@get('/')
@get('/hello')
def get_hello(name=None):
    # get the current session
    session = load_session(request)

    # if not logged in, redirect to someplace
    if not logged_in(session):
        redirect("/login")

    # get the username from session
    username = session.get('username', 'guest')

    # get the profile
    profile = load_profile(username)
    favcolor = profile.get('favcolor', 'not known')

    # save the session 
    print('saving loaded session',session)
    save_session(session, response)

    # get the weather
    weather = weather_info("44281")

    #return the requested web page
    return template('hello', name=username, color=favcolor, weather=weather)

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

    if verify_password(password, profile.get('encoding',':')):
        print("logged in")

        # save user in the session
        session['username'] = username

        # save profile for the user
        profile['favcolor'] = favcolor
        save_profile(profile)

        # save session
        save_session(session, response)
        redirect('/hello')

    else:
        print("not logged in")
        save_session(session, response)
        redirect('/login')

@get('/ajax')
def get_ajax():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('ajax', message='')

@get('/example_text')
def get_example_text():
    return """
Twas bryllyg, and ye slythy toves
Did gyre and gymble in ye wabe:
All mimsy were ye borogoves;
And ye mome raths outgrabe.
"""

@get('/other_text')
def get_other_text():
    return """
<h2>The Night Before Christmas</h2>
Twas the night before <em>Christmas</em><br/>
and all through the house<br/>
not a creature was stirring<br/>
not even a mouse.
"""

@get('/hello_ajax')
def get_hello_ajax():
    session = load_session(request)
    session['username'] = 'guest'
    save_session(session, response)
    return template('hello_ajax', message='')

@get('/weather_text')
def get_weather_text():
    # get the weather
    weather_text = str(weather_info("44281"))
    return weather_text

@get('/weather_json')
def get_weather_json():
    # get the weather
    weather_json = weather_info("44281")
    print(weather_json)
    return weather_json

debug(True)
run(host='localhost', port=8068, reloader=True)
