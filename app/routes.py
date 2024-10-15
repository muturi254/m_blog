from urllib.parse import urlsplit
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
import sqlalchemy as sa 

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

# views
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {"username": "peter"}
    title = "home"
    posts = [
        {
            "author": {"username": "John Doe"},
            "body": "Once a man is a man is a man"
        },
        {
            "author": {"username": "Jane Kimani"},
            "body": "for the beauty on beauts"
        }
    ]
    return render_template('index.html', title=title, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid credentials")
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        print("test", login_user(user, remember=form.remember_me.data))
        next_page = request.args.get('next')

        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for('index')

        print("no user", user, next_page)

        return redirect('index')

    return render_template('login.html', title='Sign in', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username = form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("congratulations, you are noe a registered user")
        return redirect(url_for('login'))

    return render_template('register.html', form=form, title="Register")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
