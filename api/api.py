from typing import List
import flask
import sqlite3
from flask import request, jsonify, Flask, abort
from flask_sqlalchemy import SQLAlchemy
import helpers

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


class Group(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    @property
    def serialize(self): return {'id': self.id_, 'name': self.name}


class UserToGroup(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)

@app.route('/api/v1/text', methods=['POST'])
def send_text():
    user_id = int(request.headers.get('user_id'))
    if len(User.query.filter_by(id_=user_id).all()) == 0:
        abort(404)
    body: str = request.json.get('body')
    username = User.query.get(user_id).username
    phoneTo = request.json.get('phoneTo')
    helpers.send_sms(phoneTo, username + '\n' + body)
    return jsonify({})

@app.route('/api/v1/user/room_id', methods=['POST'])
def get_access_token():
    user_id = int(request.headers.get('user_id'))
    if len(User.query.filter_by(id_=user_id).all()) == 0:
        abort(404)
    room_id: str = request.json.get('room_id')
    username = User.query.get(user_id).username
    token_jwt = helpers.video_access_token(roomId=room_id, username=username)
    # this doesn't match other returns because token returns a byte-object. This is okay.
    return jsonify({'token': token_jwt.decode('utf-8')})

    

# Display contents on login
@app.route('/api/v1/contact_groups', methods=['GET'])
def displayContacts():
    # Make sure user_id exists
    user_id = int(request.headers.get('user_id'))
    if len(User.query.filter_by(id_=user_id).all()) == 0:
        abort(404)
    # Find all groups which user is a member of
    group_ids = [mapping.group_id for mapping in UserToGroup.query.filter_by(
        user_id=user_id).all()]
    groups: List[Group] = [Group.query.filter_by(
        id_=group_id).first() for group_id in group_ids]
    return jsonify(json_list=[group.serialize for group in groups])


# Adds a contact (Pass in group_id, contacts)
@app.route('/api/v1/contact_group', methods=['POST'])
def addContact():
    user_id = int(request.headers.get('user_id'))
    emails = request.json.get('contacts')
    group_id = int(request.json.get('group_id'))
    try:
        group = Group.query.get(group_id)
        users = [User.query.filter_by(email=email).all()[0] for email in emails]
        # add users to group mapping
        for user in users:
            mapping = UserToGroup(user_id=user.id_, group_id=group_id)
            # if mapping doesn't already exist, dont add it
            userAlreadyInGroup = len(UserToGroup.query.filter_by(user_id=user.id_, group_id=group_id).all()) != 0
            if (not userAlreadyInGroup):
                print("Adding ", user, "To ", group)
                db.session.add(mapping)
        db.session.commit()
    except IndexError:
        abort(404)
    return jsonify({})


# Delete contact
@app.route('/api/v1/contact_group', methods=['DELETE'])
def delContact():
    user_id = int(request.headers.get('user_id'))
    group_id = request.json.get('group_id')
    Group.query.filter_by(id_=group_id).delete()
    UserToGroup.query.filter_by(group_id=group_id).delete() # Also delete all mappings to the group
    db.session.commit()
    return jsonify({})

# # Create a room (REPLACED BY get_access_token)
# @app.route('/api/v1/user/room_id', methods=['POST'])
# def createRoom():
#     user_id = int(request.headers.get('user_id'))
#     room_id = request.json.get('room_id')
#     user: User = User.query.filter_by(id_=user_id).all()[0]
#     user.roomId = room_id
#     db.session.commit()
#     return jsonify({})

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
    app.run(host= '0.0.0.0')
