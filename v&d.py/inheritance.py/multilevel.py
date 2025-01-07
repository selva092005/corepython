# class college:
#     def getstudentinfo(self):
#         self.__rollno=input("enter roll number:")
#         self.__name=input("enter name:")
#     def printstudentinfo(self):
#         print("roll number:",self.__rollno,"name:",self.__name)
        
# class BE(college):
#     def getBE(self):
#         self.getstudentinfo()
#         self.__p=int(input("enter phy marks:"))
#         self.__c=int(input("enter chem marks:"))
#         self.__m=int(input("enter maths marks:"))
        
        
#     def printBE(self):
#         self.printstudentinfo()
#         print("marks in different subjects",self.__p,self.__c,self.__m)

#     def calctotalmarks(self):
#         return(self.__p+self.__m+self.__c)

# class result(BE):
#     def getresult(self):
#         self.getBE()
#         self.__total=self.calctotalmarks()
#     def putresult(self):
#         self.printBE()
#         print("total marks out of 100:",self.__total)

# college=result()
# college.getresult()
# college.putresult()

# # Single Inheritance

# class Account:
#     accountNo=0
#     accountBal=0.0
#     accountHolder=""
#     def __str__(self):
#         return str(self.accountNo)+" "+self.accountHolder+" "+str(self.accountBal)+"\n"
# #single
# class Card(Account):
#     cardNumber=0
#     def __init__(self,cn=0,anum=0,ahold="",abal=0.0):
#         self.cardNumber=cn
#         self.transactions=[]
#         self.accountNo=anum
#         self.accountHolder=ahold
#         self.accountBal=abal
#     def __add__(self,amt):
#         self.accountBal+=amt
#         print(amt,"deposited to",self.accountHolder)
#         self.transactions.append('Credit')
#     def __sub__(self, draw):
#         if self.accountBal>=draw:
#             self.accountBal-=draw
#             print(draw,"has been withdrawn from ",self.accountHolder)
#             self.transactions.append('Debit')
#         else:print("Insufficient account balance")
#     def countTrans(self):
#         creCount=self.transactions.count('Credit')
#         debCount = self.transactions.count('Debit')
#         charges=0
#         if creCount>=5:
#             charges+=(creCount-5)*10
#         if debCount>=3:
#             charges+=(debCount-3)*20
#         print("Total charges on transaction count is",charges)
#         self.accountBal-=charges
#         print("Charges debited in your account")
#     def __str__(self):
#         return str(super(Card, self).__str__())+"\n"+str(self.cardNumber)+" "+str(self.accountBal)+"\n"
# a1=Account()
# a1.accountNo=1456;a1.accountHolder="Nandha";a1.accountBal=15000.0
# print(a1)

# c1=Card(789456123,9876787,"Annamalai",777.9)
# c1+4000
# print(c1)
# c1-1800
# print(c1)
# c1-200
# c1+1000
# c1-100
# c1-500
# c1+10000    
# c1-100
# c1+4000
# print(c1)
# c1.countTrans()


#  # Encapsulation

# class Mobile:
#     __model=""
#     __price=0.0
#     __ram=0
#     __internal=0
#     def setModel(self, mod=""):self.__model=mod
#     def getModel(self):return self.__model
#     def setPrice(self, pri=""):self.__price=pri
#     def getPrice(self):return self.__price
#     def setRam(self, ra=""):self.__ram=ra
#     def getRam(self):return self.__ram
#     def setInternal(self, inte=""):self.__internal=inte
#     def getInternal(self):return self.__internal


# mob1=Mobile()
# mob1.setModel("Iphone 13")
# mob1.setPrice(73000)
# mob1.setRam(128)
# mob1.setInternal(128)
# print(mob1.getModel(),mob1.getPrice(),mob1.getRam(),mob1.getInternal())


# mob2=Mobile()
# mob2.setRam(12)
# mob2.setModel("One plus 10R")
# mob2.setInternal(256)
# mob2.setPrice(45000)
# print(mob2.getModel(),mob2.getPrice(),mob2.getRam(),mob2.getInternal())





# #POLYMORPHISM
# class Bird:
#     def sound(self):
#         print("CUCKKOO")

#     def fly(self):
#         print("its can be flying the birds")
# class Bird1(Bird):
#     def cockatail(self):
#         print("cuteiee")
# class Bird2(Bird):
#     def Lovebirds(self):
#         print("couple of love")
# obj1=Bird()
# obj2=Bird1()
# obj3=Bird2()
# obj1.sound()
# obj1.fly();
# obj1.sound()
# obj2.cockatail()
# obj1.sound()
# obj3.Lovebirds()

# # overloading
# class sam:
#     def aa(self,a):
#         print(a)
#     def aa(self,a,b):
#         print(a+b)
#     def aa(self,a,b,c):
#         print(a+b+c)
# s=sam()
# s.aa(10)

# class over:
#     def load(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             return a+b+c
#         elif a!=None and b!=None:
#             return a+b
#         else:
#             return a
# o=over()

# print("Sum",o.load(10))
# print("sum1",o.load(10,20)) 
# print("sum",o.load(10,20,30))


# multiple args passing 
# class multiple:
#     def add(self,*args):
#         sum=40;
#         for i in args:
#             sum+=i
            
#         print("add values:",sum)
            
# m=multiple()
# m.add(20)
# m.add(40,50)
# m.add(40,50,100)
# m.add(40,50,100,200)
# m.add(10,20,60,100,150)
# m.add(10,20,30,40,50,60,70)


# #OVERRIDING
# class sam:
#     def name(self):
#         print("sampk")
# class raja(sam):
#     def name(self):
#         super().name()
#         print("raja")
# class arun(raja):
#     def name(self):
#         super().name()
#         print("ARUN")
# s=arun()
# s.name()
# s1=raja()
# s1.name()
# s=arun()
# s.name()


#operator overloading

# class operator:
#     def __init__(self,a):
#         self.a=a

#         print(self.a+self.a)
# obj=operator(10)
# obj1=operator(20)
# print("sum:",obj.a+obj.a)

#using operator overloading
class oper:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
            return self.a+b.a
        
o=oper(50)
o1=oper(100)
print("value:",o+o1)