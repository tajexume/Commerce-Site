# Standard library imports
import os

# Third-party imports
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_mysqldb import MySQL
from flask_login import *
from dotenv import load_dotenv

# Local imports
from users.User import User
from forms.forms import LoginForm
from utilities.utility import is_safe_url

# Load environment variables
load_dotenv()

# Create application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Create MySQL instance
sql = MySQL(app)

# MySQL Configurations
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
app.config["MYSQL_PORT"] = int(os.environ.get("MYSQL_PORT"))

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email="", password=""):

    return User(email=email, password=password)


@app.route("/")
@app.route("/home/")
@login_required
def homepage():
    return render_template("Homepage.html", username=request.values.get('username'))


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        cur = sql.connection.cursor()
        res = cur.execute("SELECT email, password FROM user WHERE email=%s AND \
         password=%s", (form.email.data, form.password.data))

        if res > 0:
            row = cur.fetchone()
            email = row[0]
            password = row[1]
            user = load_user(email, password)
            login_user(user)
            flash("Login Successful")
            next = request.args.get('next')
        else:
            flash("Invalid username or password")
            return redirect(url_for('login', error="Invalid username or password"))

        if not is_safe_url(next):
            return abort(400)

        return redirect(next or url_for('homepage', username=user.username))
    return render_template("Login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
