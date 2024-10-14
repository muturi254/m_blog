from flask import flash, redirect, render_template

from app import app
from app.forms import LoginForm

# views
@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title=title, user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data
        ))

        return redirect('/index')
    return render_template('login.html', form=form)