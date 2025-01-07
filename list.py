# #demonstrationn of list
value=["selva",10,4.5,'s',"bharathi"]
# # print(value)

# # #adding the new elemnets  in end if list
# value.append("bharathi")
# # print(len(value))
# print(value)

# #adding new elemnets in list
# value.insert(2,"selva")
# print(value)

# replace
# value[5]="team lead"
# print(value)

# adding values in list
monthly=[100,200,300,400,500]
# print(min(monthly))
# #sum of yhe list
# print(sum(monthly))
#remove
# monthly.remove(400)
# print(monthly)
# print(monthly.pop())
# print(monthly.pop(1))
# print(monthly)
# monthly.reverse()
# print(monthly)

# list methods
# li=[1,4,5,6,1,5,8]
# a=li.copy()
# print("copy:",a)
# count=a.count(5)
# print(count)

# list user
# a=input("enter the name")
# list=a.split(",")
# print("list names")
# for i in list:
#     print(i)

# #looping list values
# n=int(input("enter the list"))
# list1=[]
# for i in range(n):
#     liva1=input("enter the list:")
#     list1.append(liva1)
# print("list:",list1)
#middle list

a=[14,20,50,48,60,80]
print("original list:",a)
val=int(input("enter the new elements:"))
insert=int(input("enter the position:"))

a.insert(insert,val)
print("added list:",a)