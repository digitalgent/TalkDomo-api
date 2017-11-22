import connexion
from swagger_server.models.domo import Domo
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


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
    return 'do some magic!'


def get_domo_by_id(id):
    """
    Find Domo by ID
    Returns a single Domo
    :param id: ID of domo to return
    :type id: int

    :rtype: Domo
    """
    return 'do some magic!'
