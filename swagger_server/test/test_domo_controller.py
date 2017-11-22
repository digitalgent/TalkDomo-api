# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.domo import Domo
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDomoController(BaseTestCase):
    """ DomoController integration test stubs """

    def test_add_voice_command(self):
        """
        Test case for add_voice_command

        STT
        """
        response = self.client.open('/v1/domo/{id}/mic'.format(id=789),
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_all_users(self):
        """
        Test case for get_all_users

        User list
        """
        response = self.client.open('/v1/domo/{id}/users'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_domo_by_id(self):
        """
        Test case for get_domo_by_id

        Find Domo by ID
        """
        response = self.client.open('/v1/domo/{id}'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
