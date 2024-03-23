#!/usr/bin/python3
""" place module testing """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ class for place module testing """

    def __init__(self, *args, **kwargs):
        """ initialize args """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ city id test function """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ user_id test function"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ name test function"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ description test function"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ number of rooms test function"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ bathrooms number test function"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ max guest test function"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ price test function"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ lat test function """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ long test function"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ amenity ids test function"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
