# Tipos de errores
""""
1-error de sintaxis
"""
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
"""import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d)/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
"""

"""
>>> 3 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
"""
"""
>>> print(divisor)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'divisor' is not defined"""

"""
>>> 0 + "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

"""Desafio II: Creá una función denominada eneavo que tenga como argumento
 un número e imprima el resultado de la división de 1 por ese número"""

def eneavo (numero):
    try:
        return(1/numero)
    except ZeroDivisionError:
        return ("No podemos dividir por 0")
    except TypeError:
        return ("Eso es un texto")

print (eneavo("9"))

def check_int_type():
  if type(x)  != int:
    raise TypeError("Only integers are allowed") 

