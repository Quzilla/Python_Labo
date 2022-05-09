def property_method():
    class Duck():
        def __init__(self, input_name) -> None:
            self.hidden_name = input_name
        
        def get_name(self):
            print('inside the getter')
            return self.hidden_name
        def set_name(self, set_name):
            print('inside the setter')
            self.hidden_name = set_name
        name = property(get_name, set_name)
        
    fow1 = Duck('Howard')
    print(fow1.name)
    print(fow1.get_name())
    fow1.name = 'Daffy'
    print(fow1.name)
    fow1.set_name('Howard')
    print(fow1.name)

def property_decorator():
    class Duck2():
        def __init__(self, input_name) -> None:
            self.hidden_name = input_name
        @property
        def name(self):
            print('inside the getter')
            return self.hidden_name
        @name.setter
        def name(self, input_name):
            print('inside the setter')
            self.hidden_name = input_name
            
    fow1 = Duck2('Howard')
    print(fow1.name)
    fow1.name = 'Donald'
    print(fow1.name)
    
def calc_getter():
    class Circle():
        def __init__(self, radius) -> None:
            self.radius = radius
        @property
        def diameter(self):
            return 2 * self.radius
        
    c = Circle(5)
    print(c.radius)
    print(c.diameter)
    c.radius = 7
    print(c.diameter)
    c.diameter = 20
    
def mangling():
    class Duck3():
        def __init__(self, input_name) -> None:
            self.__name = input_name
        @property
        def name(self):
            print('inside the getter')
            return self.__name
        @name.setter
        def name(self, input_name):
            print('inside the setter')
            self.__name = input_name
            
    fow1 = Duck3('Howard')
    print(fow1.name)
    fow1.name = 'Donald'
    print(fow1.name)
    print(fow1.__name)
    print(fow1._Duck3__name)

if __name__ == "__main__":
    print("\t===Property_Method===")
    property_method()
    
    print("\t===Propety_Decorator===")
    property_decorator()
    
    print('\t===Calc_Getter===')
    calc_getter()
    
    print('\t===Mangling===')
    mangling()