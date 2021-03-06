import connexion
from flask import jsonify
from swagger_server.models.app import App
from swagger_server.models.user import User
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.__init__ import db


def add_app_with_domo(id, body=None):
    """
    Add a new user
    Make a new account(username, name, face, password)
    :param body: Add new account to access Domo
    :type body: dict | bytes

    :rtype: User
    """
    params = connexion.request.get_json()

    app = App(
        name = params['name'],
        apptype = params['apptype'],
        status = params['status'],
        domo_id = id
    )

    db.add(app)
    db.commit()

    return jsonify(app), 200, {'Access-Control-Allow-Origin': '*'}

def get_app_by_id(id):
    """
    Find app by ID
    Returns a single app
    :param id: ID of App
    :type id: int

    :rtype: App
    """
    app = db.query(App).filter_by(id=id).first()

    return jsonify(app), 200, {'Access-Control-Allow-Origin': '*'}

def update_app(id):
    """
    Update an existing app
    :param id: App that needs to be edited
    :type id: int64

    :rtype: App
    """
    app = db.query(App).filter_by(id=id).first()

    params = connexion.request.get_json()

    app.name = params['name']
    app.apptype = params['apptype']
    app.status = params['status']

    db.commit()
    return jsonify(app), 200, {'Access-Control-Allow-Origin': '*'}

def add_alarm(id):
    """
    Add a new Alarm
    Add a new alarm
    :param id: Add new Alarm
    :type id: int

    :rtype: App
    """
    params = connexion.request.get_json()

    alarm = Alarm(
        id=params['id'],
    )

    db.add(alarm)
    db.commit()

    return jsonify(alarm), 200, {'Access-Control-Allow-Origin': '*'}


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

    return jsonify(user), 200, {'Access-Control-Allow-Origin': '*'}


def add_light(id):
    """
    Add a new light
    Add a new light to be remote controlled
    :param id: Add new Light
    :type id: int

    :rtype: App
    """
    params = connexion.request.get_json()

    light = Light(
        id=params['id'],
    )

    db.add(light)
    db.commit()

    return jsonify(light), 200, {'Access-Control-Allow-Origin': '*'}


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

    :rtype: App
    """
    alarm = db.query(Alarm).filter_by(id=id).first()

    return jsonify(alarm), 200, {'Access-Control-Allow-Origin': '*'}


def get_all_alarms(id):
    """
    Alarms list
    Returns all alarms
    :param id: ID of Domo
    :type id: int

    :rtype: App
    """
    alarm = db.query(Alarm).all()

    return jsonify(alarm), 200, {'Access-Control-Allow-Origin': '*'}


def get_all_apps(id):
    """
    Find all apps on Domo
    Returns all apps
    :param id: ID of Domo
    :type id: int

    :rtype: App
    """
    apps = db.query(App).all()

    return jsonify(apps), 200, {'Access-Control-Allow-Origin': '*'}


def get_all_ligths(id):
    """
    Lights list
    Returns all lights
    :param id: ID of Light
    :type id: int

    :rtype: App
    """
    light = db.query(Light).filter_by(id=id).all()

    return jsonify(light), 200, {'Access-Control-Allow-Origin': '*'}


def get_authorized_users(id):
    """
    Users list with access to security
    Returns all authorized users
    :param id: ID of App
    :type id: int

    :rtype: User
    """
    user = db.query(User)

    return jsonify(user), 200, {'Access-Control-Allow-Origin': '*'}


def get_light_by_id(id):
    """
    Find light by ID
    Returns a single light
    :param id: ID of Light
    :type id: int

    :rtype: App
    """
    light = db.query(Light).filter_by(id=id).first()

    return jsonify(light), 200, {'Access-Control-Allow-Origin': '*'}


def get_weather(id):
    """
    Weather Forecast
    weather forecast and advice for how to dress
    :param id: ID of App(weather)
    :type id: int

    :rtype: App
    """
    weather = db.query(Weather)

    return jsonify(weather), 200, {'Access-Control-Allow-Origin': '*'}


def update_alarm(id):
    """
    Update an existing alarm
    Edit an existing alarm
    :param id: Alarm that needs to be edited
    :type id: int

    :rtype: App
    """
    alarm = db.query(Alarm).filter_by(id=id).first()
    params = connexion.request.get_json()

    alarm.time = params["time"]
    alarm.goodmorning = params["goodmorning"]

    db.commit()
    return jsonify(alarm), 200, {'Access-Control-Allow-Origin': '*'}



def update_light(id):
    """
    Update an existing light
    Edit an existing light
    :param id: Light that needs to be edited
    :type id: int

    :rtype: App
    """
    light = db.query(Light).filter_by(id=id).first()
    params = connexion.request.get_json()

    light.name = params ["name"]
    light.status = params ["status"]

    db.commit()
    return jsonify(light), 200, {'Access-Control-Allow-Origin': '*'}
