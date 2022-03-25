import module01.zoo
import module02
# print(module01.zoo.hours())
# print(module02.hello())

print("in {} 1".format(__file__))
from module03 import *
print("in {} 2".format(__file__))
h1(__file__)
h2(__file__)
