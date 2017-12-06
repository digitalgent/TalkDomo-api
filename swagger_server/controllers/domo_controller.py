import connexion
from flask import jsonify
from swagger_server.models.domo import Domo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.__init__ import db
from swagger_server.models.domo import Domo

def add_voice_command(id):
    """
    STT
    Domo interprets incoming voice command
    :param id: Add new voice command
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_all_users(id):
    """
    User list
    Returns all users
    :param id: ID of Domo
    :type id: int

    :rtype: Domo
    """
    domo = db.query(Domo).filter_by(id=id).first()


    return jsonify(domo.users)

def get_domo_by_id(id):
    """
    Find Domo by ID
    Returns a single Domo
    :param id: ID of domo to return
    :type id: int

    :rtype: Domo
    """
    domo = db.query(Domo).filter_by(id=id).first()

    return jsonify(domo), 200, {'Access-Control-Allow-Origin': '*'}

def add_domo(body=None):
    """
    Add a new domo
    Add domo
    :param body: Add Domo
    :type body: dict | bytes

    :rtype: Domo
    """
    params = connexion.request.get_json()

    # return jsonify(params)
    domo = Domo(
        name=params['name'],
        datetime=params['datetime'],
        timezone=params['timezone'],
        # voice=params['voice'],
        emotion=params['emotion']
    )

    db.add(domo)
    db.commit()

    return jsonify(domo)

def delete_domo(username, api_key=None):
    """
    Delete a domo
    Deletes a domo
    :param id: id to delete
    :type id: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    user = db.query(Domo).filter_by(id=id).first()

    db.delete(domo)
    db.commit()
    return True
