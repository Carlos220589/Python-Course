# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:40:50 2019

@author: Juan Carlos
"""

'''
class Employee:
   
   empCount = 0

   def __init__(self,name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d", Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"      
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Sandra", 5000)
emp3 = Employee("Ana",8000)
emp4 = Employee("Briguitte",8000)
emp5 = Employee ('Juan',1200)
emp6 = Employee ('Carlos',1600)
emp7=Employee("Mirkka", 2500)
emp8=Employee(5888, 2500)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()
emp6.displayEmployee()
emp7.displayEmployee()
emp8.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
'''
'''
class cine:
   def __init__(self, titulo, horario, categoria, genero):
      self.titulo = titulo
      self.horario = horario
      self.categoria = categoria
      self.genero = genero
   
   def proyectar(self):
     print ("La pelicula se esta reproduciendo")

   def aluz(self):
      print ("se apagan las luces")
      
   def enluces(self):
     print ("encender luces")

   def terminar(self):
      print ("se termina la reproduccion")
      
class libro:
   def __init__(self, titulo, autor, año, paginas):
      self.titulo = titulo
      self.autor = autor
      self.año = año
      self.paginas = paginas
   
   def abrir(self):
     print ("empezar a leer")

   def resaltar(self):
      print ("resaltar texto")
      
   def significado(self):
     print ("significado de la palabra")

   def marcar(self):
      print ("marcar pagina")     
      
class coche:
   def __init__(self, marca, año, kilometraje, direccion):
      self.marca = marca
      self.año = año
      self.kilometraje = kilometraje
      self.direccion = direccion
   
   def encender(self):
     print ("encender el coche")

   def apagar(self):
      print ("apagar el coche")
      
   def bloquear(self):
     print ("bloquear el coche")

   def desbloquear(self):
      print ("desbloquear el cohe")  
      '''
dct = {'uno': 'dos', 'tres': 'uno', 'dos': 'tres'}
v = dct ['tres']
for k in range (len (dct)):
   v = dct [ v]
print (v)