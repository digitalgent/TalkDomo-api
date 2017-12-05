# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.alarm import Alarm
from swagger_server.models.light import Light
from swagger_server.models.weather import Weather
# from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model

from sqlalchemy import Table, Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relationship, backref
from swagger_server.models.base import Base

class Apps(Base):
    __tablename__ = 'apps'

    # domo_id = Column(Integer, ForeignKey('domo.id'))
    # domo = relationship("Domo", backref=backref('domo', uselist=True, cascade='delete,all'))


    # weather = Column(String(128))
    # lights = Column(String(128))
    # alarms = Column(String(128))
    # security = Column(Integer)

# class Apps(Model):
#     """
#     NOTE: This class is auto generated by the swagger code generator program.
#     Do not edit the class manually.
#     """
#     def __init__(self, weather: Weather=None, lights: Light=None, alarms: Alarm=None, security: bool=False):
#         """
#         Apps - a model defined in Swagger
#
#         :param weather: The weather of this Apps.
#         :type weather: Weather
#         :param lights: The lights of this Apps.
#         :type lights: Light
#         :param alarms: The alarms of this Apps.
#         :type alarms: Alarm
#         :param security: The security of this Apps.
#         :type security: bool
#         """
#         self.swagger_types = {
#             'weather': Weather,
#             'lights': Light,
#             'alarms': Alarm,
#             'security': bool
#         }
#
#         self.attribute_map = {
#             'weather': 'weather',
#             'lights': 'lights',
#             'alarms': 'alarms',
#             'security': 'security'
#         }
#
#         self._weather = weather
#         self._lights = lights
#         self._alarms = alarms
#         self._security = security

    @classmethod
    def from_dict(cls, dikt) -> 'Apps':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Apps of this Apps.
        :rtype: Apps
        """
        return deserialize_model(dikt, cls)

    # @property
    # def weather(self) -> Weather:
    #     """
    #     Gets the weather of this Apps.
    #
    #     :return: The weather of this Apps.
    #     :rtype: Weather
    #     """
    #     return self._weather
    #
    # @weather.setter
    # def weather(self, weather: Weather):
    #     """
    #     Sets the weather of this Apps.
    #
    #     :param weather: The weather of this Apps.
    #     :type weather: Weather
    #     """
    #
    #     self._weather = weather
    #
    # @property
    # def lights(self) -> Light:
    #     """
    #     Gets the lights of this Apps.
    #
    #     :return: The lights of this Apps.
    #     :rtype: Light
    #     """
    #     return self._lights
    #
    # @lights.setter
    # def lights(self, lights: Light):
    #     """
    #     Sets the lights of this Apps.
    #
    #     :param lights: The lights of this Apps.
    #     :type lights: Light
    #     """
    #
    #     self._lights = lights
    #
    # @property
    # def alarms(self) -> Alarm:
    #     """
    #     Gets the alarms of this Apps.
    #
    #     :return: The alarms of this Apps.
    #     :rtype: Alarm
    #     """
    #     return self._alarms
    #
    # @alarms.setter
    # def alarms(self, alarms: Alarm):
    #     """
    #     Sets the alarms of this Apps.
    #
    #     :param alarms: The alarms of this Apps.
    #     :type alarms: Alarm
    #     """
    #
    #     self._alarms = alarms
    #
    # @property
    # def security(self) -> bool:
    #     """
    #     Gets the security of this Apps.
    #
    #     :return: The security of this Apps.
    #     :rtype: bool
    #     """
    #     return self._security
    #
    # @security.setter
    # def security(self, security: bool):
    #     """
    #     Sets the security of this Apps.
    #
    #     :param security: The security of this Apps.
    #     :type security: bool
    #     """
    #
    #     self._security = security
