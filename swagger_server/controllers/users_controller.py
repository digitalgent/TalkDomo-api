import connexion
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_user(body=None):
    """
    Add a new user
    Make a new account(username, name, face, password)
    :param body: Add new account to access Domo
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())
    return 'do some magic... ?'


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
    return 'do some magic!'


def get_user_by_username(username):
    """
    Find user by username
    Returns a single username
    :param username: Username of user to return
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def update_user(username):
    """
    Update an existing user
    Edit an existing account
    :param username: User that needs to be edited
    :type username: str

    :rtype: User
    """
    return 'do some magic!'
