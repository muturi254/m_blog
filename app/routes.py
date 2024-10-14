from app import app

# views
@app.route('/')
@app.route('/index')
def index():
    return "Hello world"