# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.user import User
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUsersController(BaseTestCase):
    """ UsersController integration test stubs """

    def test_add_user(self):
        """
        Test case for add_user

        Add a new user
        """
        body = User()
        response = self.client.open('/v1/users',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_user(self):
        """
        Test case for delete_user

        Delete a user
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open('/v1/users/{username}'.format(username='username_example'),
                                    method='DELETE',
                                    headers=headers)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_user_by_username(self):
        """
        Test case for get_user_by_username

        Find user by username
        """
        response = self.client.open('/v1/users/{username}'.format(username='username_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_user(self):
        """
        Test case for update_user

        Update an existing user
        """
        body = User()
        response = self.client.open('/v1/users/{username}',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
