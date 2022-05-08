def basic():
    class Thing():
        pass
    
    example = Thing()
    print(Thing)
    print(example)

def class_attr():
    class Thing2():
        letters = 'abc'
        
    print(Thing2.letters)

def instance_attr():
    class Thing3():
        def __init__(self) -> None:
            self.letters = 'abc'
            
    example = Thing3()
    print(example.letters)

def special_methods():
    class Element():
        def __init__(self, name, symbol, number) -> None:
            self.name = name
            self.symbol = symbol
            self.number = number
        
        def dump(self):
            print(self.name, self.symbol, self.number)
            
        def __str__(self):
            return '{},{},{}'.format(self.name, self.symbol, self.number)
        

    element = Element('Hydrogen', 'H', 1)
    print(element.name)

    d = {
        'name': 'Hydrogen',
        'symbol': 'H',
        'number': 1
    }
    hydrogen = Element(**d)
    hydrogen.dump()
    print(hydrogen)

def property_getter():
    class Element2():
        def __init__(self, name, symbol, number) -> None:
            self.__name = name
            self.__symbol = symbol
            self.__number = number
            
        @property
        def name(self):
            return self.__name
        @property
        def symbol(self):
            return self.__symbol
        @property
        def number(self):
            return self.__number

    hydrogen =Element2('Hydrogen', 'H', 1)
    print(hydrogen.name)
    
def polymorphism ():
    class Bear():
        def eat(self):
            return 'berries'
        
    class Rabbit():
        def eat(self):
            return 'clover'
        
    class Octothorpe:
        def eat(self):
            return 'campers'
        
    b = Bear()
    r = Rabbit()
    o = Octothorpe()
    print(b.eat())
    print(r.eat())
    print(o.eat())
    
def composition():
    class Laser():
        def does(self):
            return 'disintegrate'
        
    class Claw():
        def does(self):
            return 'crush'
        
    class SmartPhone():
        def does(self):
            return 'ring'
        
    class Robot():
        def __init__(self) -> None:
            self.laser = Laser()
            self.claw = Claw()
            self.smartphone = SmartPhone()
            
        def does(self):
            return '''
        I have many attachments:
        \tMy laser, to {}
        \tMy claw, to {}
        \tMy smartphone, to {}
        '''.format(self.laser.does(), self.claw.does(), self.smartphone.does())
        
    robbie = Robot()
    print(robbie.does())
    
if __name__ == '__main__':
    basic()
    class_attr()
    instance_attr()
    special_methods()
    property_getter()
    polymorphism()
    composition()
