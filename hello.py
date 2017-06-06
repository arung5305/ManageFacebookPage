from flask import Flask, url_for, render_template
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, Wodrld!'

@app.route('/manage')
def getManagePage():
    return render_template('manage.html')

@app.route('/check')
def getCheckPage():
    return render_template('check.html')

@app.route('/route1')
def hello_worldone():
    return 'You are in route 1'

@app.route('/route2')
def hello_route2():
    return render_template('test01.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User is %s' % username
with app.test_request_context():
	url_for('static', filename='style.css')


app.run(debug=True)
