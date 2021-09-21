from bottle import route, run, template, get, post, request, response, redirect, os
#http://localhost:8068/....<route>
import json, random, string

def random_id():
    characters= string.ascii_lowercase+string.digits
    return ''.join(random.choices(characters, k=16))

def load_session(request):
    os.makedirs("session", exist_ok=True)
    session_id=request.get_cookie("session_id", default=None)
    try:
        if session_id==None:
            raise Exception("No session id cookie found")
        session_file=f"session/{session_id}.session"
        with open(session_file, 'r') as f:
            session=json.load(f)
    except Exception as e:
        print(e)
        session_id=random_id()
        session={
            "session_id":session_id
        }
        session_file=f"session/{session_id}.session"
        with open(session_file, 'w') as f:
                session=json.dump(session, f)
                response.set_cookie("session_id", session_id)
        return session

def save_session(session, response):
    os.makedirs("sessions", exist_ok=True)
    session_id=session['session_id']
    session_file=f"session/{session_id}.session"
    with open(session_file, 'w') as f:
        session=json.dump(session, f)
        response.set_cookie("session_id", session_id)
    return session

@get("/")
@get("/hello")
def get_hello(name=None):
    session=load_session(request)
    session_id = session['session_id']
    if 'username' in session:
        username= session['username']
    else:
        username= 'complete stranger'
    save_session(session, response)
    return template("hello.tpl", name=username, extra=None)
    
@get("/login")
def get_login():
    session=load_session(request)
    save_session(response)
    return template("login", message="")

@post("/login")
def post_login():
    session=load_session(request)
    session_id=request.get_cookie("session_id", default="123456")
    #username=request.forms.get('username')
    #password=request.forms['password']
    #if password != "magic":
        #save_session(response)
        #redirect("/login")
        #return template("login", message="bad password")
    response.set_cookie("session_id", session_id)
    save_session(session, response)
    redirect("/hello")

run(host="localhost", port=8068)