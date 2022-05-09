
def ins_method():
    class Person():
        def __init__(self, name) -> None:
            self.name = name
        def get_name(self):
            return(self.name)
    taro = Person('taro')
    print(taro.get_name())
        

def cls_method():
    class A():
        count = 0
        def __init__(self) -> None:
            A.count += 1
        def exclaim(self):
            print("I'm an A!")
        @classmethod
        def kids(cls):
            print("A has", cls.count, "little objects")
            
    easy_a = A()
    breezy_a = A()
    wheezy_a = A()
    A.kids()

def sta_method():
    class CoyoteWeapon():
        @staticmethod
        def commercial():
            print('This CoyoteWeapon has been brought to you by Acme')

    CoyoteWeapon.commercial()
    
if __name__ == "__main__":
    print('\t===InstanceMethod===')
    ins_method()
    
    print('\t===ClassMethod===')
    cls_method()
    
    print('\t===StaticMethod===')
    sta_method()