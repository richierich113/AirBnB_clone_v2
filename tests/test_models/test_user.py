#!/usr/bin/python3
""" user module testing"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ class for testing user module """

    def __init__(self, *args, **kwargs):
        """ init function"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ first name test function"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ last name test function """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ email test function"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ password test function
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
