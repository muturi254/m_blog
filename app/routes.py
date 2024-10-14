from flask import render_template

from app import app

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