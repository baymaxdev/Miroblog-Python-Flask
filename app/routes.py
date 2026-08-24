from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/home')
def home():
    return "Welcome to the Home Page!"
    
@app.route('/boom')
def boom()
    return "Boom! You Have Exploded"