# this is just a mock file before we setup a data-base & api.
import flask
from flask import request
from flask import Flask, jsonify, abort, request
from typing import List, Dict


app = flask.Flask(__name__)
app.config["DEBUG"] = True

class User:
    """ THIS IS JUST FOR MOCK PURPOSE. """
    def __init__(self, username: str, email:str, id_: int, roomId=None):
        self.username = username
        self.email = email
        self.id_ = id_
        self.roomId = roomId
    
    def as_dict(self):
        return self.__dict__

USERS: List[User] = [
    User('saif', 'example@s.com', 0),
    User('a', 'example1@s.com', 1),
    User('b', 'example2@s.com', 2),
]

USER_MAPPINGS: Dict[int, List[int]] = {0: set([1]), 1: set([0, 1]), 2: set([1, 0]), 3: set([1,2,0])}


@app.route('/contacts', methods=['GET'])
def get_contacts():
    user_id = int(request.headers.get('user_id'))
    contact_ids = USER_MAPPINGS.get(user_id)
    return {i: USERS[i].as_dict() for i in contact_ids}

@app.route('/contacts', methods=['POST'])
def add_contact():
    user_id = int(request.headers.get('user_id'))
    friend_name = request.json.get('friend_user_name')
    friend_id = [user for user in USERS if user.username == friend_name][0].id_
    USER_MAPPINGS[user_id].append(friend_id)

@app.route('/contacts', methods=['DELETE'])
def delete_contact():
    user_id = int(request.headers.get('user_id'))
    friend_name = request.json.get('friend_user_name')
    friend_id = [user for user in USERS if user.username == friend_name][0].id_
    contacts = USER_MAPPINGS[user_id]
    contacts.remove(friend_id)

@app.route('/user/room_id', methods=['POST'])
def create_room():
    user_id = int(request.headers.get('user_id'))
    room_id = request.json.get('room_id')
    user = USERS[user_id]
    user.roomId = room_id

@app.route('/user/room_id', methods=['GET'])
def join_room():
    """ Gets host's roomId"""
    user_id = int(request.headers.get('user_id'))
    host_name = request.json.get('host_user_name')
    host_user = [user for user in USERS if user.username == host_name][0]
    return host_user.roomId

if __name__ == "__main__":
    app.run()
