from bottle import route, run
#http://localhost:8068/....<route>

@route("/")
def get_index():
    return("home page!")

@route("/hello")
def get_hello():
    return("hello!")

@route("/hello/<name>")
def get_hello(name="world"):
    return(f"Hello, {name}!")

run(host="localhost", port=8068)