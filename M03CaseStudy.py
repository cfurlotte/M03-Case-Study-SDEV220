#create vehicle class with attribute type
class Vehicle:
    def __init__(self, type):
        self.type = type
#create the subclass of Vehicle
class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year 
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    #displays all of the info when called
    def displayInfo(self):
        print(f'Vehicle type: {self.type}')
        print(f'Year: {self.year}')
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Number of Doors: {self.doors}')
        print(f'Type of roof: {self.roof}')

#gets all of the inputs for the Automobile class
type = input('Enter what type of vehicle this is. Example: car, truck, buss.\n')
year = str(input('Enter what year this vehicle was made. Example: 1994\n'))
make = input('Enter who made this truck. Example: Ford\n')
model = input('Enter what the model is. Example: Suburban\n')
doors = str(input('Enter how many doors the vehicle has, 2 or 4.\n'))
roof = input('Enter weather the vehicle has a solid roof or sun roof.\n')
#runs the Automobile class then displays everything in the console
display  = Automobile(type, year, make, model, doors, roof)
display.displayInfo()