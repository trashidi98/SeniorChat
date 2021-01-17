import flask
import sqlite3
from flask import request, jsonify 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["DEBUG"] = True
db = SQLAlchemy(app)

# MODELS:
class User(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    roomId = db.Column(db.Integer)

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id_,
           'username': self.username,
           'email': self.email,

       }

    def __repr__(self):
        return '<User %r %r>' % (self.username, self.email)

class ContactMapping(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    first_user_id = db.Column(db.Integer)
    second_user_id = db.Column(db.Integer)

    def __repr__(self):
        return ('<ContactMapping> %r -> %r' % (self.first_user_id, self.second_user_id))
    

# Display contents on login
@app.route('/api/v1/contacts', methods=['GET'])
def displayContacts():
    user_id = int(request.headers.get('user_id'))
    contact_ids = [mapping.second_user_id for mapping in ContactMapping.query.filter_by(first_user_id=user_id).all()]
    contacts: List[User] = [User.query.filter_by(id_=contact_id).first() for contact_id in contact_ids]
    return jsonify(json_list=[contact.serialize for contact in contacts])




# Adds a contact
@app.route('/api/v1/contact', methods=['POST'])
def addContact():
    breakpoint()
    user_id = int(request.headers.get('user_id'))
    friend_email = request.json.get('friend_email')
    try:
        friend_user: User = User.query.filter_by(email=friend_email).all()[0]
        mapping = ContactMapping(first_user_id=user_id, second_user_id=friend_user.id_)
        db.session.add(mapping)
        db.session.commit()
    except IndexError: # if there are no users with given email
        pass
    return jsonify({})


# Delete contact 
@app.route('/api/v1/contact', methods=['DELETE'])
def delContact():
    user_id = int(request.headers.get('user_id'))
    friend_email = request.json.get('friend_user_name')
    friend_user: User = User.query.filter_by(email=friend_email).all()[0]
    ContactMapping(first_user_id=user_id, second_user_id=friend_user.id_).delete()
    db.session.commit()
    return jsonify({})



# Create a room 
@app.route('/api/v1/user/room_id', methods=['POST'])
def createRoom(): 
    user_id = int(request.headers.get('user_id'))
    room_id = request.json.get('room_id')


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


if __name__ == "__main__":
    app.run()


