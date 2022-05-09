class Bill():
    def __init__(self, description) -> None:
        self.description = description
        
class Tail():
    def __init__(self, length) -> None:
        self.length = length
        
class Duck():
    def __init__(self, bill, tail) -> None:
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')
        
tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()