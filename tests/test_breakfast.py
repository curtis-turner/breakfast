from context import breakfast

def test_breakfast():
    items = []

    bacon = breakfast.food.Food(43, 'Bacon')

    items.append(bacon)

    meal = breakfast.breakfast.Breakfast(items)

    meal.complete_breakfast()
    
    print('Total Calories of your breakfast: {cals}'.format(cals=str(meal.count_cals())))

test_breakfast()
