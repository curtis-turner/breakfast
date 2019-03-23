from context import breakfast

def test_breakfast():
    items = []

    bacon = breakfast.food.Food(43, 'Bacon')
    apple = breakfast.food.Food(95, 'Apple')

    items.append(bacon)
    items.append(apple)

    meal = breakfast.breakfast.Breakfast(items)

    meal.complete_breakfast()
    
    print('Total Calories of your breakfast: {cals}'.format(cals=str(meal.count_cals())))

if __name__ == '__main__':
    test_breakfast()
