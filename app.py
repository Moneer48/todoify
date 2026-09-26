from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import re
from helpers import login_required

app = Flask(__name__)
app.secret_key = "secret"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///todoify.db")



@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

time_zones = []

for i in range(-12, 13):
    time_zones.append(i)



@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":

        if not request.form.get("username") or not request.form.get("password"):
            flash("Must Provide a Username and Password", "danger")
            return render_template("welcome.html")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )


        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("User Not Found or Password is Incorrect", "danger")
            return render_template("login.html")

        session["user_id"] = rows[0]["id"]


        return redirect("/")


    else:
        return render_template("login.html")

@app.route("/")
def index():
    if "user_id" in session:
        rows_pen = db.execute("SELECT * FROM info WHERE user_id = ? AND status = '0' ", session["user_id"] )
        rows_comp = db.execute("SELECT * FROM info WHERE user_id = ? AND status = '1' ", session["user_id"] )
        users = db.execute("SELECT * FROM users WHERE id = ? ", session["user_id"] )
        gmt = db.execute("SELECT time_zone FROM users WHERE id = ?", session["user_id"])[0]["time_zone"]
        return render_template("index.html", rows_pen=rows_pen, rows_comp=rows_comp, users=users, gmt=gmt)
    else:
        return render_template("welcome.html")

@app.route("/complete/<int:task_id>", methods=["POST"])
@login_required
def complete(task_id):
    db.execute("UPDATE info SET status = 1 WHERE user_id = ? AND task_id = ?", session["user_id"], task_id)
    return redirect("/")
@app.route("/incomplete/<int:task_id>", methods=["POST"])
@login_required
def incomplete(task_id):
    db.execute("UPDATE info SET status = 0 WHERE user_id = ? AND task_id = ?", session["user_id"], task_id)
    return redirect("/")

@app.route("/delete/<int:task_id>", methods=["POST"])
@login_required
def delete(task_id):
    db.execute("DELETE FROM info WHERE user_id = ? AND task_id = ?", session["user_id"], task_id)

    return redirect("/")

@app.route("/star/<int:task_id>", methods=["POST"])
@login_required
def star(task_id):
    db.execute("UPDATE info SET starred = 1 WHERE user_id = ? AND task_id = ?", session["user_id"], task_id)
    return redirect("/")

@app.route("/unstar/<int:task_id>", methods=["POST"])
@login_required
def unstar(task_id):
    db.execute("UPDATE info SET starred = 0 WHERE user_id = ? AND task_id = ?", session["user_id"], task_id)
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("sign-up.html")

    else:
        name = request.form.get("name").strip()
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        confirmation = request.form.get("confirmation").strip()
        time_zone = int(request.form.get("timezone"))

        if name and len(name) > 30:
            flash("Full name can only be 30 characters or less", "danger")
            return render_template("sign-up.html")

        if name and not re.match(r'^[A-Za-z\s]+$', name):
            flash("Full name can only contain letters and/or spaces", "danger")
            return render_template("sign-up.html")

        # At least one letter and one number where length should be greater than 4, else warn the user.
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z0-9]+$', username) or len(username) < 4:
            flash("Username should include at least 4 characters (Letters and/or numbers ONLY)", "danger")
            return render_template("sign-up.html")

        if not username or not password:
            flash("Provide Username and Password", "danger")
            return render_template("sign-up.html")

        elif password != confirmation:
            flash("Passwords do not match", "danger")
            return render_template("sign-up.html")

        elif time_zone not in time_zones:
            flash("Invalid Time Zone", "danger")
            return render_template("sign-up.html")

        elif db.execute("SELECT * FROM users WHERE username = ?", username):
            flash("Username already exists. Try to login", "info")
            return render_template("login.html")

        hash_pass = generate_password_hash(password)

        db.execute("INSERT INTO users(name, username, hash, time_zone) VALUES (?, ?, ?, ?)", name, username, hash_pass, time_zone)
        rows = db.execute("SELECT * FROM users WHERE hash = ?", hash_pass)
        session["user_id"] = rows[0]["id"]

        return redirect("/")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        title = request.form.get("title")
        description = request.form.get("description")
        due_date = request.form.get("due_date")
        due_time = request.form.get("due_time")

        if not description:
            flash("Provide a Description", "danger")
            return render_template("add.html")

        if not due_date:
            flash("Due date is required", "danger")
            return render_template("add.html")

        if not due_time:
            flash("Due time is required", "danger")
            return render_template("add.html")

        time_zone = db.execute("SELECT time_zone FROM users WHERE id = ?", session["user_id"])[0]["time_zone"]

        local_date = db.execute("SELECT DATETIME('now', ? || ' hours') AS local_time", time_zone)[0]["local_time"]

        db.execute("INSERT INTO info (user_id, title, description, date, due_date, due_time) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], title, description, local_date, due_date, due_time)

        return redirect("/")

@app.route("/change-password", methods=["POST", "GET"])
@login_required
def change():
    if request.method == "GET":
        return render_template("change.html")
    else:
        old_pass = request.form.get("old_password").strip()
        new_pass = request.form.get("password").strip()
        confirmation = request.form.get("confirmation").strip()

        if not old_pass or not new_pass or not confirmation:
            flash("Provide full information", "danger")
            return render_template("change.html")
        elif new_pass != confirmation:
            flash("New and Confirmation passwords do not match", "danger")
            return render_template("change.html")
        elif not check_password_hash(db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]["hash"], old_pass):
            flash("Current Password is incorrect", "danger")
            return render_template("change.html")
        elif new_pass == old_pass:
            flash("You did not change your password. Please choose a new password different than your current one", "danger")
            return render_template("change.html")
        new_hash = generate_password_hash(new_pass)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, session["user_id"])
        return redirect("/")

@app.route("/delete-account", methods=["POST", "GET"])
@login_required
def delete_acc():
    if request.method == "GET":
        username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
        return render_template("delete.html", username=username)
    else:
        password = request.form.get("password").strip()
        confirmation = request.form.get("confirmation").strip()

        if password != confirmation:
            flash("New and Confirmation passwords do not match", "danger")
            return render_template("delete.html")
        elif not check_password_hash(db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]["hash"], password):
            flash("Password is incorrect", "danger")
            return render_template("delete.html")
        db.execute("DELETE FROM users WHERE id = ?", session["user_id"])
        db.execute("DELETE FROM info WHERE user_id = ?", session["user_id"])

        session.clear()

        return redirect("/")

@app.route("/star")
@login_required
def starred():

    rows_star = db.execute("SELECT * FROM info WHERE user_id = ? AND starred = 1", session["user_id"] )

    users = db.execute("SELECT * FROM users WHERE id = ? ", session["user_id"] )
    gmt = db.execute("SELECT time_zone FROM users WHERE id = ?", session["user_id"])[0]["time_zone"]

    return render_template("star.html", rows_star=rows_star, users=users, gmt=gmt)

@app.route("/time-zone", methods=["GET", "POST"])
@login_required
def time_zone():
    if request.method == "GET":
        return render_template("timezone.html")
    else:
        time_zone = int(request.form.get("timezone"))
        if time_zone not in time_zones:
            flash("Invalid Time Zone", "danger")
            return render_template("timezone.html")

        db.execute("UPDATE users SET time_zone = ? WHERE id = ?", time_zone, session["user_id"])
        return redirect("/")
