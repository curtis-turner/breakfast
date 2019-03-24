
class Food:

    def __init__(self, cals=0, name=None):
        self.cals = cals
        self.name = name

    def add_name(self, name):
        if self.name == None:
            self.name = name
    
    def add_cals(self, cals):
        if self.cals == 0:
            self.cals = cals
