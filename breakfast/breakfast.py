class Breakfast():
    def __init__(self, meal):
        self.meal = meal

    def calories(self):
        cal_count = 0
        for i in self.meal:
            cal_count += i.cals

        return cal_count
    
    def complete_breakfast(self):
        for i in self.meal:
            print('{item} is a part of a complete and balanced breakfast.'.format(item=i.name))
