import connexion
from swagger_server.models.apps import Apps
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_alarm(id):
    """
    Add a new Alarm
    Add a new alarm
    :param id: Add new Alarm
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def add_authorized_user(username):
    """
    Add a new authorized user
    Add a new authorized user
    :param username: authorized username
    :type username: str

    :rtype: User
    """
    return 'do some magic!'


def add_light(id):
    """
    Add a new light
    Add a new light to be remote controlled
    :param id: Add new Light
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def delete_alarm(id, api_key=None):
    """
    Delete a alarm
    
    :param id: Alarm id to delete
    :type id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def delete_authorized_user(username, api_key=None):
    """
    Delete an authorized user
    
    :param username: Username to delete
    :type username: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def delete_light(id, api_key=None):
    """
    Delete a light
    
    :param id: Light id to delete
    :type id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_alarm_by_id(id):
    """
    Find alarm by ID
    Returns a single alarm
    :param id: ID of Alarm
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def get_all_alarms(id):
    """
    Alarms list
    Returns all alarms
    :param id: ID of Domo
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def get_all_apps(id):
    """
    Find all apps on Domo
    Returns all apps
    :param id: ID of Domo
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def get_all_ligths(id):
    """
    Lights list
    Returns all lights
    :param id: ID of Light
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def get_authorized_users(id):
    """
    Users list with access to security
    Returns all authorized users
    :param id: ID of App
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def get_light_by_id(id):
    """
    Find light by ID
    Returns a single light
    :param id: ID of Light
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def get_weather(id):
    """
    Weather Forecast
    weather forecast and advice for how to dress
    :param id: ID of App(weather)
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def update_alarm(id):
    """
    Update an existing alarm
    Edit an existing alarm
    :param id: Alarm that needs to be edited
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'


def update_light(id):
    """
    Update an existing light
    Edit an existing light
    :param id: Light that needs to be edited
    :type id: int

    :rtype: Apps
    """
    return 'do some magic!'
