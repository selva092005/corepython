class college:
    def __init__(self,name,course):
        self.n=name
        self.c=course
    def print(self):
        print(self.n,self.c)
        print("hello")
c=college("mec",2024)
c.print()

class A:
    def __init__(self,age,place):
        self.A=age;
        self.p=place;
    def display(self):
        print(self.A,self.p)
s=A(20,"mec")
s.display()