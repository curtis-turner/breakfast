import unittest
#from context import breakfast
import breakfast

class TestBreakfast(unittest.TestCase):

    def setUp(self):
        self.breakfast = breakfast.Breakfast()
        self.bacon = breakfast.Food(43, 'Bacon')

    def test_breakfast_defaults(self):
        self.assertEqual(len(self.breakfast.items), 0, 'Default should have no items')
        self.assertEqual(self.breakfast.count_cals(), 0, 'Default values not correct')

    def test_add_item(self):
        num_items = len(self.breakfast.items)
        self.breakfast.add_item(self.bacon)
        self.assertEqual(len(self.breakfast.items), num_items+1, 'Item was not successfully add to breakfast')

    def test_remove_item(self):
        self.breakfast.add_item(self.bacon)
        num_items = len(self.breakfast.items)
        self.breakfast.remove_item(self.bacon)
        self.assertEqual(len(self.breakfast.items), num_items-1, 'Item was not sucessfully removed from breakfast')
    
    def test_count_cals(self):
        self.breakfast.add_item(self.bacon)
        self.assertEqual(self.breakfast.count_cals(), 43, 'Calories were not correct summed together')

if __name__ == '__main__':
    unittest.main

'''
def test_breakfast():
    items = []

    bacon = breakfast.food.Food(43, 'Bacon')
    apple = breakfast.food.Food(95, 'Apple')

    items.append(bacon)
    items.append(apple)

    meal = breakfast.breakfast.Breakfast(items)

    meal.complete_breakfast()
    
    print('Total Calories of your breakfast: {cals}'.format(cals=str(meal.count_cals())))
'''