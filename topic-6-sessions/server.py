from bottle import route, run, template, get, post, request, response
#http://localhost:8068/....<route>

session_id= "abc"

@get("/")
def get_index():
    return("home page!")

@get("/hello")
@get("/hello/<name>")
def get_hello():
    session= request.get_cookie("session_id", "abc")
    response.set_cookie("session_id", session_id)
    return template("hello.tpl", name=session_id, extra=None)

@get("/greet")
def get_greet():
    return("hello!")

@get("/greet/<name>")
def get_hello(name="world"):
    return template("hello.tpl", name="Bob", extra="Happy Birthday!!!")

@get("/login")
def get_login():
    session= request.get_cookie("session_id", "abc")
    response.set_cookie("session_id", session_id)
    return template("login", message="")

@post("/login")
def post_login():
    session= request.get_cookie("session_id", "abc")
    global currnet_user
    print(request.forms.get('username'))
    print(request.forms.get('password'))
    username=request.forms.get('username')
    password=request.forms['password']
    if password != "magic":
        return template("login", message="bad password")
    current_user=username
    response.set_cookie("session_id", session_id)
    return template("hello.tpl", name=session_id, extra="Happy Birthday!!!")


run(host="localhost", port=8068)