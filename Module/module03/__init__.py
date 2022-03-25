print('__init__.py')

from ._module1 import hello as h1
from ._module2 import hello as h2

__all__ = ["h1", "h2"]
h1("__init__.py")
h2("__init__.py")