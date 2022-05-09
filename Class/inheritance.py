def basic():
    class Car():
        def exclaim(self):
            print("I am a Car!")
    class Yugo(Car):
        pass
    give_me_a_car = Car()
    give_me_a_yugo = Yugo()
    give_me_a_car.exclaim()
    give_me_a_yugo.exclaim()
   
def method_override(): 
    class Car():
        def exclaim(self):
            print("I am a Car!")
    class Yugo(Car):
        def exclaim(self):
            print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
        
    give_me_a_car = Car()
    give_me_a_yugo = Yugo()
    give_me_a_car.exclaim()
    give_me_a_yugo.exclaim()


    class Person():
        def __init__(self, name) -> None:
            self.name = name
    class MDPerson(Person):
        def __init__(self, name) -> None:
            self.name = "Doctor" + name
    class JDPerson(Person):
        def __init__(self, name) -> None:
            self.name = name + ", Esquire"
            
    person = Person("Fudd")
    doctor = MDPerson("Fudd")
    lawyer = JDPerson("Fudd")
    print(person.name)
    print(doctor.name)
    print(lawyer.name)
    
def add_method():
    class Car():
        def exclaim(self):
            print("I am a Car!")
    class Yugo(Car):
        def exclaim(self):
            print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
            
        def need_a_push(self):
            print("A little help here?")
        
    give_me_a_car = Car()
    give_me_a_yugo = Yugo()
    give_me_a_yugo.need_a_push()
    # give_me_a_car.need_a_push()
    
def use_supper():
    class Peson():
        def __init__(self, name) -> None:
            self.name = name
            
    class EmailPeson(Peson):
        def __init__(self, name, email) -> None:
            super().__init__(name)
            self.email = email
            
    bob = EmailPeson('Bob Frapples', 'bob@frapples.com')
    print(bob.name)
    print(bob.email)
    
if __name__ == "__main__":
    print("\t===Basic===")
    basic()
    
    print("\t===Method_Override===")
    method_override()
    
    print("\t===Add_Method===")
    add_method()
    
    print("\t===Use_Supper===")
    use_supper()
    
    print("\t===Appendix==")
    class Car():
        def exclaim(self):
            print("I am a Car!")
    car = Car()
    car.exclaim()
    Car.exclaim(car)
    