# this is just a mock file before we setup a data-base & api.
import flask
from flask import request
from flask import Flask, jsonify, abort, request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

USERS = [
    {'username': 'saif', 'email': 'example@example.com'},
    {'username': 'someone', 'email': 'someone@example.com'},
    {'username': 'someone2', 'email': 'someone@example.com'},
    {'username': 'someone3', 'email': 'someone@example.com'},

]

USER_MAPPINGS = {0: [1], 1: [0, 1], 2: [1, 0], 3: [1,2,0]}


@app.route('/contacts', methods=['GET'])
def get_contacts():
    user_id = int(request.headers.get('user_id'))
    contact_ids = USER_MAPPINGS.get(user_id)
    return {i: USERS[i] for i in contact_ids}

if __name__ == "__main__":
    app.run()
