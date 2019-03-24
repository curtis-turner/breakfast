
class Food:

    def __init__(self, cals=0, name=None):
        self.cals = cals
        self.name = name

    def add_name(self, name):
        self.name = name
    
    def add_cals(self, cals):
        self.cals = cals
