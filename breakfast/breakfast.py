class Breakfast():

    def __init__(self, items):
        self.items = items

    def count_cals(self):
        cal_count = 0
        for i in self.items:
            cal_count += i.cals

        return cal_count
    
    def complete_breakfast(self):
        for i in self.items:
            print('{item} is a part of a complete and balanced breakfast.'.format(item=i.name))

if __name__ =='__main__':
    pass
