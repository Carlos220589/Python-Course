'''
try:
    x=int(input('Enter a number'))
    y=1/x
    print(y)
except ZeroDivisionError:
    print('you cannot divide by zero, sorry')
except ValueError:
    print('you must enter an integer value')
except:
    print('oh dear, something went wrong')
print('THE END')
'''

'''''
try:
    y=1/0
except ZeroDivisionError:
    print('division para cero')
except ArithmeticError:
    print('problema aritmetico')
    '''
''''
import math
x=float(input('enter a number'))
assert x>=0.0
x=math.sqrt(x)
print(x)
'''
def validarNumero(prompt, min, max):
    while (True):
        try:
            print("Ingrese un valor entre ",min," y ",max)
            x = int(input(prompt))
            assert x >= min and x <= max
            return x

        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("Error, el valor debe estar dentro del RANGO ")

v = validarNumero("Ingrese un valor en el rango:", -100, 100)
print("El número es:", v)
