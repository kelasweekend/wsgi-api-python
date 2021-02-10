import pymonad.tools
from pymonad.tools import curry
from pymonad.reader import Compose

@pymonad.tools.curry(2) # Pass the expected number of arguments to the curry function.
def pertambahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

def add_1(x):
    return x + 1

def mul_3(x):
    return 3 * x

# menggunakan fungsi compose pada multioperator dengan compose
new_func = (Compose(add_1)
            .then(mul_3)
            .then(str)
)
