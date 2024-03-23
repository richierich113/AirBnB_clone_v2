#!/usr/bin/python3
""" state module testing """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ state module testing class"""

    def __init__(self, *args, **kwargs):
        """ init function """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """ name test function"""
        new = self.value()
        self.assertEqual(type(new.name), str)
