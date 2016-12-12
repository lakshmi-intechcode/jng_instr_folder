from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/<name>')
def hello_name(name):
    return 'Hello ' + name + '.'

@app.route('/create/<user>')
def create_user(user):
	return "You have just created the user " + user

if __name__ == "__main__":
    app.run(debug=True)
