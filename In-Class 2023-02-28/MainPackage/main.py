#main.py
from VehiclePackage.VehicleClass import *

#Instantiate an object of type Vehicle
car = Vehicle("Corvette") #This called the __init__ method in the class
#Invoke the printType method on the car object
car.printType()