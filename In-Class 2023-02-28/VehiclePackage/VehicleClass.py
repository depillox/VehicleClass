#VehicleClass.py
'''
Vehicle Class
'''
class Vehicle:
    '''
    Initialize the object at instantiation
    "Constructor" method
    '''
    def __init__(self, type):
        self.type = type;
    def printType(self):
        print(self.type);
        
#This code only runs if this module is the entry point
if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    #This could be the test code for this module
    print("I am in VehicleClass.py")
