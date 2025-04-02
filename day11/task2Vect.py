class Vect(object):
    def __init__(self,a,b):
        self.fst=a
        self.sec=b
    #add overloading 
    def __add__(self,other):
        return Vect((self.fst+other.fst),(self.sec+other.sec))
    #sub overloading 
    def __sub__(self,other):
        return Vect((self.fst-other.fst),(self.sec-other.sec))
    def __str__(self,other):
        if Vect((self.fst==other.fst),(self.sec==other.sec)):
            return True
        else:
            return False
    def display(self):
        print(f"{self.fst},{self.sec}")


#test code
c=Vect(1,3)
c1=Vect(2,4)
y=c+c1
y.display()




