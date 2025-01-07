# Hierarchy inheritance:
from array import *

class Stocks:
    products=array('i')
    def show(self):print("Products are: ",self.products)

class Jaysurya(Stocks):
    def __init__(self,hey):
        self.products=array('i')
        self.products.extend(hey)
    def search(self):
        budget=int(input("Enter the price  search:"))
        for x in self.products:
            if x<=budget:print(x)
class Reliance(Stocks):
    def __init__(self,hai):
        
        self.products = array('i')
        self.products.extend(hai)
    def getByPosition(self,start,stop):
        print(self.products[start:stop])

j=Jaysurya([5000,300,800,780,150])
r=Reliance([100,200,300,400,500,600,800,1000])

j.search()

r.getByPosition(0,5)
r.show()
j.show()


from abc import *

class Falcon(ABC):
    def __init__(self):
        self.mine={78,33,10,40,923,42,56,5,75,477,3,56}
    #abstract function        
    def heyThere(self):
        pass
    

class Winter(Falcon):
    def heyThere(self):
        print(self.mine)


win=Winter()
win.heyThere()

