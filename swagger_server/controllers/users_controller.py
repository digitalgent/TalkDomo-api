import connexion
from flask import jsonify
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.__init__ import db
from swagger_server.models.user import User

def add_user(body=None):
    """
    Add a new user
    Make a new account(username, name, face, password)
    :param body: Add new account to access Domo
    :type body: dict | bytes

    :rtype: User
    """
    params = connexion.request.get_json()

    user = User(
        email=params['email'],
        first_name=params['firstName'],
        last_name=params['lastName'],
        password=params['password'],
        username=params['username'],
        face=params['face']
    )

    db.add(user)
    db.commit()

    return jsonify(user)

    # if connexion.request.is_json:
    #     body = User.from_dict(connexion.request.get_json())
    # return 'do some magic... ?'


def delete_user(username, api_key=None):
    """
    Delete a user
    Deletes a user
    :param username: Username to delete
    :type username: str
    :param api_key:
    :type api_key: str

    :rtype: None
    """

    user = db.query(User).filter_by(username=username).first()
    db.delete(user)
    db.commit()
    return True

def get_user_by_username(username):
    """
    Find user by username
    Returns a single username
    :param username: Username of user to return
    :type username: str

    :rtype: User
    """
    user = db.query(User).filter_by(username=username).first()

    return jsonify(user)


def update_user(username):
    """
    Update an existing user
    Edit an existing account
    :param username: User that needs to be edited
    :type username: str

    :rtype: User
    """
    user = db.query(User).filter_by(username=username).first()

    params = connexion.request.get_json()

    user.first_name = params['firstName']
    user.last_name = params['lastName']
    user.email = params['email']
    user.password = params['password']
    # user.update(
    #     email=params['email'],
    #     first_name=params['firstName'],
    #     last_name=params['lastName'],
    #     password=params['password'],
    #     username=params['username'],
    #     face=params['face']
    # )

    # db.update(user)
    db.commit()
    return jsonify(user)
