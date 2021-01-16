import flask

from flask import request, jsonify 

app = flask.Flask(__name__)
app.config["DEBUG"] = True



# Display contents on login
@app.route('/api/v1/contacts', methods=['GET'])
def home():
    return "<h1>This site is a prototype API</h1>"



# Adds a contact
@app.route('/api/v1/contact', methods=['POST'])
def addContact(): 
	pass

# Delete contact 
@app.route('/api/v1/contact' methods=['DELETE'])
def delContact():
	pass


# Create a room 
@app.route('/api/v1/user/room_id', methods=['POST'])
def createRoom(): 
	pass


# Join a room 
@app.route('/api/v1/user/room_id', methods=['GET'])
def joinRoom():


@app.route('/api/v1/login', methods=['POST'])
def login():  





if __name__ == "__main__":
    app.run()