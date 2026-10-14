
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///vgc.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

@app.route("/")
@login_required
def index():
    students = db.execute("SELECT * FROM students WHERE user_id = ? ORDER BY id DESC", session["user_id"])
    return render_template("dashboard.html", students=students)

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        # TODO: your login logic (same as Finance)
        username = request.form.get("username")
        password = request.form.get("password")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
            return render_template("apology.html", message="invalid username/password")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return render_template("apology.html", message="must provide username/password")
        hash_pw = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_pw)
        except:
            return render_template("apology.html", message="username taken")
        return redirect("/login")
    return render_template("register.html")

@app.route("/add", methods=["POST"])
@login_required
def add():
    name = request.form.get("name")
    country = request.form.get("country")
    course = request.form.get("course")
    status = request.form.get("status")
    if name and country:
        db.execute("INSERT INTO students (user_id, name, country, course, status) VALUES (?, ?, ?, ?, ?)",
                   session["user_id"], name, country, course, status)
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
