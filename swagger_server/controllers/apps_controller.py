import connexion
from flask import jsonify
from swagger_server.models.apps import Apps
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.__init__ import db
from swagger_server.models.apps import Apps


def add_alarm(id):
    """
    Add a new Alarm
    Add a new alarm
    :param id: Add new Alarm
    :type id: int

    :rtype: Apps
    """
    params = connexion.request.get_json()

    alarm = Alarm(
        id=params['id'],
    )

    db.add(alarm)
    db.commit()

    return jsonify(alarm)


def add_authorized_user(username):
    """
    Add a new authorized user
    Add a new authorized user
    :param username: authorized username
    :type username: str

    :rtype: User
    """
    params = connexion.request.get_json()

    user = User(
        username=params['username'],
    )

    db.add(user)
    db.commit()

    return jsonify(user)


def add_light(id):
    """
    Add a new light
    Add a new light to be remote controlled
    :param id: Add new Light
    :type id: int

    :rtype: Apps
    """
    params = connexion.request.get_json()

    light = Light(
        id=params['id'],
    )

    db.add(light)
    db.commit()

    return jsonify(light)


def delete_alarm(id, api_key=None):
    """
    Delete a alarm

    :param id: Alarm id to delete
    :type id: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    user = db.query(Alarm).filter_by(id=id).first()

    db.delete(alarm)
    db.commit()


def delete_authorized_user(username, api_key=None):
    """
    Delete an authorized user

    :param username: Username to delete
    :type username: str
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    user = db.query(User).filter_by(username=username).first()

    db.delete(user)
    db.commit()


def delete_light(id, api_key=None):
    """
    Delete a light

    :param id: Light id to delete
    :type id: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    user = db.query(Light).filter_by(id=id).first()

    db.delete(light)
    db.commit()


def get_alarm_by_id(id):
    """
    Find alarm by ID
    Returns a single alarm
    :param id: ID of Alarm
    :type id: int

    :rtype: Apps
    """
    alarm = db.query(Alarm).filter_by(id=id).first()

    return jsonify(alarm)


def get_all_alarms(id):
    """
    Alarms list
    Returns all alarms
    :param id: ID of Domo
    :type id: int

    :rtype: Apps
    """
    alarm = db.query(Alarm).all()

    return jsonify(alarm)


def get_all_apps(id):
    """
    Find all apps on Domo
    Returns all apps
    :param id: ID of Domo
    :type id: int

    :rtype: Apps
    """
    apps = db.query(Apps).all()

    return jsonify(apps)


def get_all_ligths(id):
    """
    Lights list
    Returns all lights
    :param id: ID of Light
    :type id: int

    :rtype: Apps
    """
    light = db.query(Light).filter_by(id=id).all()

    return jsonify(light)


def get_authorized_users(id):
    """
    Users list with access to security
    Returns all authorized users
    :param id: ID of App
    :type id: int

    :rtype: User
    """
    user = db.query(User)

    return jsonify(user)


def get_light_by_id(id):
    """
    Find light by ID
    Returns a single light
    :param id: ID of Light
    :type id: int

    :rtype: Apps
    """
    light = db.query(Light).filter_by(id=id).first()

    return jsonify(light)


def get_weather(id):
    """
    Weather Forecast
    weather forecast and advice for how to dress
    :param id: ID of App(weather)
    :type id: int

    :rtype: Apps
    """
    weather = db.query(Weather)

    return jsonify(weather)


def update_alarm(id):
    """
    Update an existing alarm
    Edit an existing alarm
    :param id: Alarm that needs to be edited
    :type id: int

    :rtype: Apps
    """
    alarm = db.query(Alarm).filter_by(id=id).first()
    params = connexion.request.get_json()

    alarm.time = params["time"]
    alarm.goodmorning = params["goodmorning"]

    db.commit()
    return jsonify(alarm)



def update_light(id):
    """
    Update an existing light
    Edit an existing light
    :param id: Light that needs to be edited
    :type id: int

    :rtype: Apps
    """
    light = db.query(Light).filter_by(id=id).first()
    params = connexion.request.get_json()

    light.name = params ["name"]
    light.status = params ["status"]

    db.commit()
    return jsonify(light)
