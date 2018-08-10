import json
import unittest
from unittest.mock import patch

from asteroid import Asteroid


class TestAsteroid(unittest.TestCase):
    def setUp(self):
        print(self)
        print ('running setUp')
        self.asteroid = Asteroid(2099942)
        print ('finishing setUp')

    def mocked_get_data(self):
        print('running mocked_get_data')
        
        with open('apophis_fixture.txt') as f:
            return json.loads(f.read())

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_name(self):
        print('running test_name')
        self.assertEqual(
            self.asteroid.name, '99942 Apophis (2004 MN4)'
        )

    @patch('asteroid.Asteroid.get_data', mocked_get_data)
    def test_diameter(self):
        print('running test_diameter')
        self.assertEqual(self.asteroid.diameter, 682)
        print ('finishing test_diameter')


test = TestAsteroid()
