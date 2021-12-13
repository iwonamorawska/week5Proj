from app import app
from flask import render_template
@app.route('/')
def home_page():
    return render_template('index.html', my_title="this is the home page")

@app.route('/about')
def AboutStore():
    return render_template('about.html')
@app.route('/testing')  
def test():
     return 'This is a test'