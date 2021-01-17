import flask
import sqlite3

from flask import request, jsonify 

app = flask.Flask(__name__)
app.config["DEBUG"] = True



# Display contents on login
@app.route('/api/v1/contacts', methods=['GET'])
def displayContacts():
    return "<h1>This site is a prototype API</h1>"


# Adds a contact
@app.route('/api/v1/contact', methods=['POST'])
def addContact(): 
    args = request.args

# Delete contact 
@app.route('/api/v1/contact', methods=['DELETE'])
def delContact():
	args = request.args


# Create a room 
@app.route('/api/v1/user/room_id', methods=['POST'])
def createRoom(): 
	args = request.args


# Join a room 
@app.route('/api/v1/user/room_id', methods=['GET'])
def joinRoom():
    args = request.args


@app.route('/api/v1/login', methods=['POST'])
def login():  
    pass

@app.route('/', methods=['GET'])
def home():
    return "<h1>This site is a prototype API</h1>"


conn = sqlite3.connect('data.db')




if __name__ == "__main__":
    app.run()


