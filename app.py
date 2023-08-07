from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import abort, redirect, url_for
from flask import make_response
from markupsafe import escape

app = Flask(__name__)

# 日本語のASCII化とキーのソートを無効
app.config["JSON_AS_ASCII"] = False
app.config["JSON_SORT_KEYS"] = False

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

@app.route("/login")
@app.get("/login")
def login():
    return show_the_login_form()

@app.post("/login")
def login_post():
    if valid_login(request.form.get("username"),
                   request.form.get("password")):
        return do_the_login(request.form.get("username"))
    else:
        error = "Invalid username/password"
        return login_error(error)

@app.route("/user/<username>/")
def profile(username):
    return jsonify({
        "id": "001",
        "username": username
    })

@app.route("/error/<int:code>")
def error_page(code):
    abort(code)
    
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template("error.html", code=404), 404)
    resp.headers["X-Something"] = "A Value"
    return resp

with app.test_request_context("/hello", method="POST"):
    print(url_for("index"))
    print(url_for("hello", name="test_name"))
    print(url_for("login"))
    print(url_for("profile", username="John Doe"))
    
    assert request.path == "/hello"
    assert request.method == "POST"

def valid_login(username, password):
    if username == None or password == None:
        return False
    return True

def show_the_login_form():
    return render_template("login.html")

def do_the_login(username):
    return f"POST /login \n logged in {username}"

def login_error(error):
    return f"{error}"



# @app.route("/hello")
# def hello():
#     return "Hello, World!"

# @app.route("/user/<username>")
# def show_user_profile(username):
#     # ~~/user/temp_username -> Result: User temp_username
#     return f"User {escape(username)}"

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     # ~~/post/123 -> Result: Post 123
#     return f"Post {post_id}"

# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#     # ~~/path/hoge/fuga -> Result: Subpath hoge/fuga
#     return f"Subpath {escape(subpath)}"

# @app.route("/projects/")
# def projects():
#     # 末尾のスラッシュなし`/perojects`にアクセスすると、`/projects/`にリダイレクトされる
#     return "The project page"

# @app.route("/about")
# def about():
#     # 末尾にスラッシュを追加して`/about/`にアクセスすると、Not Found404エラーになる
#     return "The about page"