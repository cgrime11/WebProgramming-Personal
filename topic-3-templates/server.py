from bottle import route, run, template
#http://localhost:8068/....<route>

@route("/")
def get_index():
    return("home page!")

@route("/hello")
def get_hello():
    return("hello!")

@route("/hello/<name>")
def get_hello(name="world"):
    return template("hello.tpl", name="Bob", extra=None)

@route("/greet")
def get_greet():
    return("hello!")

@route("/greet/<name>")
def get_hello(name="world"):
    return template("hello.tpl", name="Bob", extra="Happy Birthday!!!")


run(host="localhost", port=8068)