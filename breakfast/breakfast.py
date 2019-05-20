class Breakfast:

    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if len(self.items) > 0:
            index = self.items.index(item)
            del self.items[index]

    def count_cals(self):
        cal_count = 0
        if len(self.items) > 0:
            for i in self.items:
                cal_count += i.cals

        return cal_count
    
    def complete_breakfast(self):
        if len(self.items) > 0:
            for i in self.items:
                print(f'{i.name} is a part of a balanced breakfast.')
        else:
            print('You did not eat anything for breakfast. Go get some food.')

