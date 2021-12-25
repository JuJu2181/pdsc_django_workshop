class Car:
    def __init__(self,mileage,brand):
        print('Congrats you bought a car')
        self.mileage = mileage
        self.brand = brand 

    def start(self):
        print("Brand:",self.brand,"Bhrooom","Your car will run for",self.mileage,"Km")
    
class Car4WD(Car):
    def start(self):
        super().start()
        print("bhroom with 4 wheels")

class ElectricCar(Car):
    def start(self):
        print("Suiii with battery power")

yuc = Car4WD(mileage=13, brand="Toyota")
yuc.start()

ec = ElectricCar(mileage=10, brand="Tesla")
ec.start()