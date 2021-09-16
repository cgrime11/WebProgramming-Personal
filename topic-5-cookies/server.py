from bottle import route, run, template, get, post, request, response
#http://localhost:8068/....<route>

current_user= None

@get("/")
def get_index():
    return("home page!")

@get("/hello")
@get("/hello/<name>")
def get_hello(name=None):
    current_user=request.get_cookie("username", default="world")
    if name==None:
        name=current_user
    if name== None:
        name="world"
    return template("hello.tpl", name=current_user, extra=None)

@get("/greet")
def get_greet():
    return("hello!")

@get("/greet/<name>")
def get_hello(name="world"):
    return template("hello.tpl", name="Bob", extra="Happy Birthday!!!")

@get("/login")
def get_login():
    return template("login", message="")

@post("/login")
def post_login():
    print(request.forms.get('username'))
    print(request.forms.get('password'))
    username=request.forms.get('username')
    password=request.forms['password']
    if password != "magic":
        return template("login", message="bad password")
    current_user=username
    response.set_cookie("username", username)
    return template("hello.tpl", name=username, extra="Happy Birthday!!!")


run(host="localhost", port=8068)