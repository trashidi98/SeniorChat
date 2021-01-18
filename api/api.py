from typing import List
import flask
import sqlite3
from flask import request, jsonify, Flask, abort, Response
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import helpers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["DEBUG"] = True
db = SQLAlchemy(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# MODELS:
class User(db.Model):
    __tablename__ = "users"
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id_,
            'name': self.name,
            'email': self.email,

        }

    def __repr__(self):
        return '<User %r %r>' % (self.name, self.email)


class Group(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    @property
    def serialize(self): return {'id': self.id_, 'name': self.name}


class UserToGroup(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)

@app.route('/api/v1/tmproom', methods=['GET'])
def tmp_room():
    email, name = request.headers.get('email'), request.headers.get('email')
    email = email if emai
    token_jwt = helpers.video_access_token(roomId="tmpRoom", username=email)
    return jsonify({'token': token_jwt.decode('utf-8')})



@app.route('/api/v1/text', methods=['POST'])
def send_text():
    try:
        email, name = request.headers.get('email'), request.headers.get('email')
        user = User.query.filter_by(email=email).all()[0]
    except IndexError:
        abort(404) # user doesn't exist
    body: str = request.json.get('body')
    phoneTo = request.json.get('number_to_send_to')
    helpers.send_sms(phoneTo, name + '\n' + body)
    return jsonify({})

@app.route('/api/v1/user/room_id', methods=['POST'])
def get_access_token():
    try:
        email, name = request.headers.get('email'), request.headers.get('email')
        user = User.query.filter_by(email=email).all()[0]
    except IndexError:
        abort(404) # user doesn't exist
    room_id: str = request.json.get('room_id')
    name = user.name
    token_jwt = helpers.video_access_token(roomId=room_id, username=name)
    return jsonify({'token': token_jwt.decode('utf-8')})

    

# Display contents on login
@app.route('/api/v1/contact_groups', methods=['GET'])
def displayContacts():
    breakpoint()
    try:
        email, name = request.headers.get('email'), request.headers.get('name')
        user = User.query.filter_by(email=email).all()[0]
    except IndexError:
        abort(404) # user doesn't exist    # Find all groups which user is a member of
    group_ids = [mapping.group_id for mapping in UserToGroup.query.filter_by(
        user_id=user.id_).all()]
    groups: List[Group] = [Group.query.filter_by(
        id_=group_id).first() for group_id in group_ids]
    return jsonify(json_list=[group.serialize for group in groups])


# Adds a contact (Pass in group_id, contacts)
@app.route('/api/v1/contact_group', methods=['POST'])
def addContact():
    try:
        email, name = request.headers.get('email'), request.headers.get('email')
        user = User.query.filter_by(email=email).all()[0]
    except IndexError:
        abort(404) # user doesn't exist

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
    except IndexError: # Invalid Email
        abort(404)
    return jsonify({})


# Delete contact
@app.route('/api/v1/contact_group', methods=['DELETE'])
def delContact():
    try:
        email, name = request.headers.get('email'), request.headers.get('email')
        user = User.query.filter_by(email=email).all()[0]
    except IndexError:
        abort(404) # user doesn't exist    
    group_id = request.json.get('group_id')
    Group.query.filter_by(id_=group_id).delete()
    UserToGroup.query.filter_by(group_id=group_id).delete() # Also delete all mappings to the group
    db.session.commit()
    return jsonify({})


@app.route('/api/v1/login', methods=['POST'])
@cross_origin()
def login():
    email = request.json.get('email')
    name = request.json.get('name')

    users = db.session.query(User).filter_by(email=email).all()
    user: User = None
    if len(users == 0):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
    else:
        user = users[0]

    response.headers['Access-Control-Allow-Origin'] = '*'
    return jsonify({})

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

@app.after_request
def no_cors(response):
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
