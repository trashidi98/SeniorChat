import flask
import sqlite3
from flask import request, jsonify, Flask, abort
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
    roomId = db.Column(db.String(80))

    def __init__(self, username, email): 
        self.username = username 
        self.email = email

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

# Display contents on login
@app.route('/api/v1/contacts', methods=['GET'])
def displayContacts():
    user_id = int(request.headers.get('user_id'))
    if len(User.query.filter_by(id_=user_id).all()) == 0:
        abort(404)
    contact_ids = [mapping.second_user_id for mapping in ContactMapping.query.filter_by(first_user_id=user_id).all()]
    contacts: List[User] = [User.query.filter_by(id_=contact_id).first() for contact_id in contact_ids]
    return jsonify(json_list=[contact.serialize for contact in contacts])


# Adds a contact
@app.route('/api/v1/contact', methods=['POST'])
def addContact():
    user_id = int(request.headers.get('user_id'))
    friend_user_name = request.json.get('friend_user_name')
    try:
        friend_user: User = User.query.filter_by(username=friend_user_name).all()[0]
        mapping = ContactMapping(first_user_id=user_id, second_user_id=friend_user.id_)
        db.session.add(mapping)
        db.session.commit()
    except IndexError: # if there are no users with given email
        abort(404)
    return jsonify({})


# Delete contact 
@app.route('/api/v1/contact', methods=['DELETE'])
def delContact():
    user_id = int(request.headers.get('user_id'))
    friend_user_name = request.json.get('friend_user_name')
    try:
        friend_user: User = User.query.filter_by(username=friend_user_name).all()[0]
        ContactMapping.query.filter_by(first_user_id=user_id, second_user_id=friend_user.id_).delete()
        db.session.commit()
        return jsonify({})
    except IndexError:
        abort(404)



# Create a room 
@app.route('/api/v1/user/room_id', methods=['POST'])
def createRoom(): 
    user_id = int(request.headers.get('user_id'))
    room_id = request.json.get('room_id')
    user: User = User.query.filter_by(id_=user_id).all()[0]
    user.roomId = room_id
    db.session.commit()
    return jsonify({})

# Join a room #TODO: When we setup twilio, this should probably return the access token for the room.
@app.route('/api/v1/user/room_id', methods=['GET'])
def joinRoom():
    user_id = int(request.headers.get('user_id'))
    host_user_name = request.json.get('host_user_name')
    host: User = User.query.filter_by(username=host_user_name)
    return jsonify({'roomId': host.roomId})


@app.route('/api/v1/login', methods=['POST'])
def login():  
    auth_token = str(request.headers.get('auth_token'))
    email = str(request.headers.get('email'))
    username = str(request.json.get('username'))

    user = db.session.query(User).filter_by(email=email).first()

    if user is None: 
        user = User(username, email)
        db.session.add(user)
        db.session.commit()
        return user.id

    return user.id



    # TODO queryParams vs headers 
    # authtok is header
    # everything else is a queryParam 

    # TODO look at Firebase documentation for what fields inside auth token are available 
    
    # TODO
    # Parse out email and username (FirstName LastName from AuthToken) from auth token  
    # because that information is needed in every one of these functions it should be broken out into its own function 
    # i.e. AUTHTOKEN CONTAINS (email, username) this should be parsed by a function and passed to whoever needs it 



@app.route('/', methods=['GET'])
def home():
    return "<h1>This site is a prototype API</h1>"


if __name__ == "__main__":
    app.run()


