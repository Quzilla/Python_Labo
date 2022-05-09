from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {
    'bill': 'wede orange',
    'tail': 'short'
}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

duck['color'] = 'green'