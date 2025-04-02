class Car(object):
    nCars=0
    #this is constructor 
    def __init__(self,brand,year,name,mileage): #double underscored=dunder variable
        #instance variable
        self.brand=brand
        self.name=name
        self.year=year
        self.mileage=mileage
    #member functions
    def drive(self,distance):
        self.mileage+=distance
    def display_info(self):
        print("Brand".ljust(10),'|',self.brand)
        print("Name".ljust(10),'|',self.name)
        print("Year".ljust(10),'|',self.year)
        print("Mileage".ljust(10),'|',self.mileage)

class Electric(Car):
    def __init__(self, brand, year, name, mileage):
        super().__init__(brand, year, name, mileage)
        self.battery=0
    def charge(self,units):
        self.battery-=units

    def drive(self,distance):
        self.battery-=distance/10 #this is used to reduce the unit based on the distance
    def display_info(self):
        super().display_info()
        print("Battery".ljust(10),'|',self.battery)
        
#test code
    print("-"*100)
    print("From Superclass")
    print("-"*100)
if __name__== "__main__":
    c=Car("hyndai","getz",2005,10)
    c.drive(10)
    c.display_info()
#test code for the subclasss
    print("-"*100)
    print("From Subclass")
    print("-"*100)
    c1=Electric("hyndai","getz",2005,1000)
    c1.drive(200)
    c1.charge(10)
    c1.display_info()