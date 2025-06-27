from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_folder="static")
app.secret_key = "your_secret_key_here"

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(150))
    name = db.Column(db.String(150))
    phone = db.Column(db.String(15))
    date = db.Column(db.String(20))
    persons = db.Column(db.Integer)
    arrival_time = db.Column(db.String(10))
    activities = db.Column(db.String(300))

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        if User.query.filter_by(name=name).first():
            return "User already exists!"
        db.session.add(User(name=name, password=password))
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        user = User.query.filter_by(name=name, password=password).first()
        if user:
            session["user"] = name
            return redirect(url_for("user_dashboard"))
        return "Invalid credentials!"
    return render_template("login.html")

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        if name == "admin" and password == "admin":
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        return "Invalid admin credentials!"
    return render_template("admin_login.html")

@app.route("/book", methods=["GET", "POST"])
def book():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        date = request.form["date"]
        persons = request.form["persons"]
        arrival_time = request.form["arrival_time"]
        activities = request.form.getlist("activities")
        booking = Booking(
            user=session["user"],
            name=name,
            phone=phone,
            date=date,
            persons=persons,
            arrival_time=arrival_time,
            activities=", ".join(activities)
        )
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for("user_dashboard"))

    return render_template("booking.html")

@app.route("/user-dashboard")
def user_dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    bookings = Booking.query.filter_by(user=session["user"]).all()
    return render_template("user_dashboard.html", bookings=bookings, username=session["user"])

@app.route("/admin-dashboard")
def admin_dashboard():
    if "admin" not in session:
        return redirect(url_for("admin_login"))
    bookings = Booking.query.all()
    return render_template("admin_dashboard.html", bookings=bookings)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=8000)
