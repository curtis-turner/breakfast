import unittest

import breakfast

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food = breakfast.Food()

    def test_food_defaults(self):
        self.assertEqual(self.food.name, None, 'Default Values where not correclty set')
        self.assertEqual(self.food.cals, 0, 'Default Values where note correctly set')