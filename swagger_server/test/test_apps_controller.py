# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.apps import Apps
from swagger_server.models.user import User
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestAppsController(BaseTestCase):
    """ AppsController integration test stubs """

    def test_add_alarm(self):
        """
        Test case for add_alarm

        Add a new Alarm
        """
        body = Apps()
        response = self.client.open('/v1/apps/{id}/alarms',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_add_authorized_user(self):
        """
        Test case for add_authorized_user

        Add a new authorized user
        """
        response = self.client.open('/v1/apps/security/users/{username}'.format(username='username_example'),
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_add_light(self):
        """
        Test case for add_light

        Add a new light
        """
        body = Apps()
        response = self.client.open('/v1/apps/{id}/lights',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_alarm(self):
        """
        Test case for delete_alarm

        Delete a alarm
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open('/v1/apps/alarms/{id}'.format(id=789),
                                    method='DELETE',
                                    headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_authorized_user(self):
        """
        Test case for delete_authorized_user

        Delete an authorized user
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open('/v1/apps/security/users/{username}'.format(username='username_example'),
                                    method='DELETE',
                                    headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_light(self):
        """
        Test case for delete_light

        Delete a light
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open('/v1/apps/lights/{id}'.format(id=789),
                                    method='DELETE',
                                    headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_alarm_by_id(self):
        """
        Test case for get_alarm_by_id

        Find alarm by ID
        """
        response = self.client.open('/v1/apps/alarms/{id}'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_all_alarms(self):
        """
        Test case for get_all_alarms

        Alarms list
        """
        response = self.client.open('/v1/apps/{id}/alarms'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_all_apps(self):
        """
        Test case for get_all_apps

        Find all apps on Domo
        """
        response = self.client.open('/v1/domo/{id}/apps'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_all_ligths(self):
        """
        Test case for get_all_ligths

        Lights list
        """
        response = self.client.open('/v1/apps/{id}/lights'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_authorized_users(self):
        """
        Test case for get_authorized_users

        Users list with access to security
        """
        response = self.client.open('/v1/apps/{id}/security/users'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_light_by_id(self):
        """
        Test case for get_light_by_id

        Find light by ID
        """
        response = self.client.open('/v1/apps/lights/{id}'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_weather(self):
        """
        Test case for get_weather

        Weather Forecast
        """
        response = self.client.open('/v1/apps/{id}/weather'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_alarm(self):
        """
        Test case for update_alarm

        Update an existing alarm
        """
        body = Apps()
        response = self.client.open('/v1/apps/alarms/{id}',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_light(self):
        """
        Test case for update_light

        Update an existing light
        """
        body = Apps()
        response = self.client.open('/v1/apps/lights/{id}',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
