class Word():
    def __init__(self, text) -> None:
        self.text = text
        
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
    
    def __eq__(self, __o: object) -> bool:
        return self.text.lower() == __o.text.lower()
    
    def __str__(self) -> str:
        return self.text
    
    def __repr__(self) -> str: # interpreter
        return self.text
    
first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))

print(first == third)
print(first)