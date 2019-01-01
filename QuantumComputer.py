import random
from math import sqrt
h = 0
classicalb = random.randint(1,101)
In = 0
def N(In):
 global qubit
 qubit = 0 
 if(In == 1):
  In = 1
  qubit = In
 else:
     qubit = 0
def H(In):
 global h
 h = 1
 
def Measure(qubita):
 global classicalb
 classicalb = 0
 global qubit
 qubita = qubit
 if(qubit == 1 ):
  classicalb = qubit
  print(classicalb)
 elif(qubit == 0):
  classicalb = qubit
  print(classicalb)  
 elif(h == 1):
  classicalb = random.randint(0,1)
  qubit = classicalb 
  classicalb = qubit
 else:
  print ("error Please Check code")

N(2)
H(qubit)
print(qubit)
Measure(qubit)
print(classicalb)
print (random.randint(0,1))
