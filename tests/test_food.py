import unittest

import breakfast

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food = breakfast.Food()

    def test_food_defaults(self):
        self.assertEqual(self.food.name, None, 'Default Values where not correclty set')
        self.assertEqual(self.food.cals, 0, 'Default Values where note correctly set')
    
    def test_add_name(self):
        self.food.add_name('Bacon')
        self.assertEqual(self.food.name, 'Bacon', 'Add Name method has failed')
    
    def test_add_cals(self):
        self.food.add_cals(43)
        self.assertEqual(self.food.cals, 43, 'Add Cels method has failed')