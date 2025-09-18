import os
os.system('cls')
#FUNCTIONS
# def greet():
#     print("Hello Fatima Faheem")
# def (A Keyword to Define a Function)
# greet (A Function Name)
# () parenthesis
# : Start of the function block
#--------
# print("hello Fatima faheem ") is a code inside function
# def greet(name):
#     print(f"Hello {name}")
# greet("hiba")
#--------
# def sum(a,b):
#     print(a+b)
# sum(9,8)
#----------
# def sum(a,b):
#     return(a+b)
# box = sum(4,7)
# print(box)
#------------
# def choice(a,b):
#     return(a*b)
# product=choice(8,9)
# print(product)
#-------------
# def greet(name="Friend"):
#     print(f"Salam {name}")
# greet()
# greet("Meow")
#--------------
# def add_numbers(a,b=5):
#     print(a+b)
# add_numbers(6,1)
#---------------
# def calculate(a,b):
#     sum_val=a+b
#     diff_val=a-b
#     print(sum_val,diff_val)
# calculate(7,2)
# def calculate(a,b):
#     sum_val=a+b
#     product_val=a*b
#     return(sum_val,product_val)
# sum,prod=calculate(9,4)
# print(f"Sum: {sum}")
# print(f"Product: {prod}")
#1
#Printing Average
# def average(a,b,c):
#     print((a+b+c)/3)
# a,b,c=map(int,input("Enter 3 Numbers to do Average: ").split())
# average(a,b,c)
#2
# Another Method
# def average():
#     a,b,c=map(int,input("Enter 3 Nums here: ").split())
#     av = (a+b+c)/3
#     print(f"Average: {av}")
# average()
#3
# def student_result():
#     Eng,Urdu,Math=map(int,input("Enter The Marks Of Eng,Urdu,Maths: ").split())
#     Total=(Eng+Urdu+Math)
#     av=(Eng+Urdu+Math)/3
#     print(f"Total Marks: {Total}")
#     print(f"Average: {av}")
# student_result()
#4
# def calc():
#     num_1=int(input("Enter 1st Num: "))
#     num_2=int(input("Enter 2nd Num: "))
#     sum=(num_1+num_2)
#     diff=(num_1-num_2)
#     product=(num_1*num_2)
#     print(f"Sum of nums: {sum}")
#     print(f"Difference of nums: {diff}")
#     print(f"Product of nums: {product}")
# calc()
#5
#Circle Area and CIrcumference
# def circle(radius=1):
#     radius=int(input("Enter Radius: "))
#     area=(3.14)*(radius*radius)
#     circum=2*(3.14)*(radius)
#     return(area,circum)
# a,c=circle()
# print(a,c)
#6
# def result_making(Name=" ",Eng=0,Urdu=0,Math=0):
#     Name=input("Enter Students's Name: ")
#     Eng=int(input("Enter Eng Marks: "))
#     Urdu=int(input("Enter Urdu Marks: "))
#     Math=int(input("Enter Math Marks: "))
#     Total=(Eng+Urdu+Math)
#     Av=(Eng+Urdu+Math)/3
#     max_marks=max(Eng,Urdu,Math)
#     return(Name,Eng,Urdu,Math)
# N,E,U,M=result_making(Eng=89,Urdu=64)
# print(f"Student Name: {N}")
# print(f"Eng Marks: {E}")
# print(f"Urdu Marks: {U}")
# print(f"Math Marks: {M}")
#7
# def intro(*arg):
#     print(arg)
# intro("fatima,19,abc,eng,math")
#8(passing integers)
# def square(x):
#     return x*x
# x=square(6)
# print(x)
#9(passing strings)
# def stringy(text):
#     return text.upper()
# s = stringy("fatima faheem")
# print(s)
#10 (Passing list using *arg)
# def listy(*arg):
#     print(list(arg))
# listy(2,3,4,5)
#11 
# def num_to_list(*arg):
#     print(list(arg))
# num_to_list(5,6,7,8,943,23)
#12
# def num_to_tup(*arg):
#     print(tuple(arg))
# num_to_tup([23,56,7])
#13
# listy=[]
# def list_of_tup(*arg):
#     for a in arg:
#         t=(a,)
#         listy.append(t)
#     print(listy)
# list_of_tup(34,22,67,44,1)
#14
# def continues_sum():
#     tup=0
#     while True:
#         x=int(input("Enter the num you wanna add: "))
#         tup+=x
#         user=input("Enter yes to continue and stop to stop adding: ").lower()
#         if(user=="stop"):
#             break
#     print(f"Sum is: {tup}")
# continues_sum()        
#15
# def greet(**kwargs):
    # print(kwargs)
# greet(Hello="Fatima",Age=20,Bye="fatiii")
#16
# def sum_user(*many):
#     many=[]
#     while True:
#         value=int(input("Enter value to add: "))
#         many.append(value)
#         user=input("Enter you wanna add more? Yes or No? ").lower()
#         if(user=="no"):
#             break
#     print(sum(many))
# sum_user()
#17
#Mini Project (Student Info)
# student_dict={} #Global Dictionary can be accessed for all functions.
# def student_info():
#     name = input("Enter student name: ")
#     age = int(input("Enter students's age: "))
#     roll_no= int(input("Enter students's Roll No: "))
#     enrolled= int(input("Enter the year when student enrolled: "))
#     student_dict[roll_no]={}
#     student_dict[roll_no]["Name"]=name
#     student_dict[roll_no]["Age"]=age
#     student_dict[roll_no]["Roll No"]=roll_no
#     student_dict[roll_no]["Enrolled Year"]=enrolled
#     student_dict.update(student_dict[roll_no])
# # student_info() 
# def student_update():
#     check=int(input("Enter Roll no who you wanna update: "))
#     if check in student_dict:
#         print(f"press 1 for updating students's name,\nPress 2 for updating age,")
#         print(f"press 3 for updating Roll No,\nPress 4 for  updating Enrolled Year: ")
#         user=int(input("Enter Your Choice: "))
#         if(user==1):
#             new_name=input(f"Enter New Name for Roll no {check}: ")
#             student_dict[check]["Name"]=new_name
#             print(f"Name Updated Succesfully!")
#         if(user==2):
#             new_age=int(input(f"Enter New Age for Roll no {check}: "))
#             student_dict[check]["Age"]=new_age
#             print(f"Age Updated Succesfully!")
#         if(user==3):
#             new_roll=int(input(f"Enter New Roll No for this previous Roll No {check}: "))
#             student_dict[check]["Roll No"]=new_roll
#             print(f"Roll No Updated Succesfully!")
#         if(user==4):
#             new_enrolled=int(input("Enter the New year of Enrollment: "))
#             student_dict[check]["Enrolled Year"]=new_enrolled
#             print(f"{student_dict[check]} updated info: ")  
#     else:
#         print(f"Roll no {check} not Found!")
# student_update() 
#18
#Global and Non-Global
# x=10 #5
# def func():
#     global x
#     x=5
#     print(x)
# func()
# print(x)
#19
# x=100 #90 #80
# def decrease():
#     global x
#     x=x-10
#     print(x)
# print(x)
# decrease()
# decrease()
#20
#Mini Projects
# total = 0
# def add_points(points):
#     global total
#     total+=points
#     print(f"You added {points} points and current score is {total}")
# def reset_total():
#     total=0
#     print(f"Score Reset, Score: {total}")
#21
#Bank Balanace:
# Balance=1600
# def deposit(amount):
#     global Balance
#     Balance+=amount
#     print(f"You deposited Rs {amount}, Now Your Total amount is: {Balance}")
# def withdraw(amount):
#     global Balance
#     Balance-=amount
#     print(f"You withdraw Amount of Rs {amount}, Now your Total amount is Rs {Balance} ")
# withdraw(500)
# deposit(5000)
#22
# def student_info(**dict):
#     dict={}
#     num=int(input("How many students do want to add: "))
#     for n in range(0,num):
#         roll_input=int(input("Enter Roll No Here: "))
#         dict[roll_input]={}
#         dict[roll_input]["Name"]=input("Enter Student's Name here: ")
#         dict[roll_input]["Age"]=input("Enter Student's Age here: ")
#         # dict[roll_input]["Subject"]=input("Enter Student's Subject here: ")
# #----------------
#     print(dict)
#23
#Kwargs:
# def order_pizza(size,*toppings,**details):
#     print(f"Ordered a pizza, Size: {size}")
#     print(f"Toppings on Pizza: *{toppings}*")
#     print(f"Details: {details}")
# order_pizza("Large","Olives","Cheese","Tomatoes",Delivered=False,Quantity=1,Delivery_Charges= "Rs 100")
#24
#Lambda Function:
# sum=lambda x,y: x+y
# print(sum(2,3))
# average=lambda x,y,z: (x+y+z)/3
# print(average(3,4,5))
# def add10(x):
#     return(x+10)
# storing=add10(5)
# print(storing)
# def add(x,y):
#     return (x+y)
# print(add(4,6))
# def add(x,y):
#     return (x+y)
# s_v=(add(4,6))
# print(s_v)
#25
#function inside another function:
# def outer_func():
#     def inner(x):
#         return x+2
#     return inner 
# inner = outer_func()
# f=inner(2)
# print(f)
# def great(a,b):
#     if (a>b):
#         return a
#     else:
#         return b
# def greatest(a,b,c):
#     if(great(a,b)<c): 
#         return c
#     else:
#         return(great(a,b))    
# store = greatest(6,7,8)
# print(store)
# def sum_2(x,y):
#     print(x+y)
# sum_2(9,8)
# sum_2=lambda x,y:x+y
#26
# USE OF MAPS
# def double(x):
#     print(x*2,end=" ")
# nums=[2,3,4,5,6]
# list(map(double,nums))
# def double(x):
#     return x*2
# nums=[2,3,4,5,6]
# collector=list(map(double,nums))
# print(collector)
# double=lambda x:x*2
# nums=[2,3,4,5,6]
# collector=list(map(double,nums))
# print(collector)
#27
#MAPS
# nums = [1,2,3,4,5]
# def square(x):
#     return x*2
# collector=list(map(square,nums))
# print(collector)
#28
# square=lambda x:x*2
# print(list(map(square,nums)))
#29
# names=["Fatima","Bisma","hiba"]
# def capital(x):
#     return x.upper()
# storing=list(map(capital,names))
# print(storing)
#30
# a=[1,2,3]
# b=[10,20,30]
# def adding(x,y):
#     return(x+y)
# storing=list(map(adding,a,b))
# print(storing)
#31
# Not using Filter 
# nums=[2,5,8,1,10,3]
# def greater_than_5(x):
#     return(x>=5)
# storing=list(map(greater_than_5,nums))
# c=0
# for i in nums:
#     print(f"{i} is greater than 5: {storing[c]}")
#     c+=1
#32
# Using Filter with function
# nums=[2,5,8,1,10,3]
# def greater_than_5(x):
#     return(x>5 )
# storing=list(filter(greater_than_5,nums))
# print(storing)
#33
# Using Filter with lambdas
# nums=[2,5,8,1,10,3]
# greater_than_5=lambda x:x>5
# storing=list(filter(greater_than_5,nums))
# print(storing)
#34
# printing Even using simple function
# def even(x):
#     print(f"{x} is Even: {x%2==0}")
# even(3007)
#35
# printing Even using simple lambda
# Even=lambda x:x%2==0
# print(Even(78))
#36
# printing Even using filter with function
# def even_in_lists(x):
#     return x%2==0
# num=[23,55,43,221,76,59,100]
# storing=list(filter(even_in_lists,num))
# print(f"These are even Numbers from the list: {num.copy()}\n{storing}")
#37
# printing Even using filter with lambdas
# even=lambda x :x%2==0
# storing=list(filter(even,num))
# print(f"Even Nums: {storing}")
#38
#Sorted using simple function
# def sorting(*arg):
#     arg=list(arg)
#     arg.sort()
#     return(arg)
# print(sorting(12,56,2,7,45))
#39
# Sorted using simple lambda
# listy=[12,56,2,7,45]
# listyn=sorted(listy)
# print(listyn)
#40
# listy=["Fat","Bis","Hib","Eman"]
# listyn=sorted(listy,key=str.lower)
# print(listyn)
#41
#how to make the strings in list in lower case
# new=[]
# listy=["FATim","BISma","Hibaaa","Eman"]
# for l in listy:
#     new.append(l.lower())
# #42
# store=sorted(new,key=len)
# print(store)
#43 (For storing only the last digits of the n in nums)
# num=[12,45,34,20,67,43]
# for n in num:
#     num[(num.index(n))]=n%10
# print(num)
# #44 (Another Method)
# list=[]
# for n in num:
#     list.append(n%10)
# print(list)
#45
# num=[12,453,3444,2,677777,43931]
# def ln(x):
#     return len(x)
# print(sorted(num,key=))
# print(num)
# 46(for calculating length of the integers)
# list=[]
# num=[12,333,5,6345]
# for n in num:
#     list.append(len(str(n)))
# print(list)
#47 (Shorter way)
# num=[12,333,5,6345]
# num=[len(str(n)) for n in num]
# print(num)
#48 (Sorting Based on length:)
# num=[12,333,5,6345]
# num=sorted(num,key=lambda n: len(str(n)))
# print(num)
#49 (Sorting using Function)
# def ln(x):
#     if (type(x)==str):
#         return len(x)
#     else:
#         return len(str(x))
# names=["fatima","hiba""BismA","eMAN","eSA","iBRAHIM"]
# new=sorted(names,key=ln)
# print(new)
#50 
#Sorting Students by marks:
# def sec(x):
#     return x[1]
# students=[("Ali",85),("Fatima",92),("Sara",78),("Umer",90)]
# so=sorted(students,key=sec)
# print(so)
#51
# #Sorting Shopping Items by price:
# items=[{"name":"Shoes","price":2500},
#     {"name":"bag","price":1200},
#     {"name":"Watch","price":4000},
#     {"name":"Perfume","price":2000}]
# store=sorted(items,key=lambda x:x["price"])
# print("here are the items from price low to high...")
# print(store)
#52
#sorting names by last letter:
# names=["alI","fatima","umeR","sara"]
# store=sorted(names,key=lambda x:x[-1].lower())
# print(store)
#53
#sorting crickeT players by runs:
# players=[{"name":"Babar","runs":150},
# {"name":"Rizwan","runs":200},
# {"name":"Shaheen","runs":50}
# ]
# store=sorted(players,key=lambda x:x["runs"],reverse=True)
# print(store)
#54
#Filter
# nums = [1,2,3,4,5,6,67,8,9,10,11,12,13,14,15,16,17]
# store=list((filter(lambda x:x%2==0,nums)))
# print(store)
#55
# students=[("Ali",50),("Fatima",92),("Sara",78),("Umer",90),("Eisha",65)]
# passing=list(filter(lambda x:x[1]>=70,students))
# print(passing)
#56
#(Real life example)
# users=[{"name":"Ali","active":True},
# {"name":"Sara","active":False},
# {"name":"Omar","active":True}]
# active_user=list(filter(lambda x:x["active"],users))
##Now to print the names of active users
# names=set()
# for l in active_user:
#     for j in l:
#         names.add(l["name"])
# print(f"The active users are: {names}")
##OR
# names=[]
# for l in active_user:
#     names.append(l["name"])
# print(names)
##OR
# def n(x):
#     return x["name"]
# store=list(map(n,active_user))
# print(store)
##
#OR
# store=list(map(lambda x:x["name"],active_user))
# print(store)
#57
# listy=[1,2,3,4,5,6]
# from functools import reduce
# total=reduce(lambda x,y: x+y,listy)
# print(total)
# print(sum(listy))
#58
#USE OF REduce:
# from functools import reduce
# prices=[1200,500,800,1500]
# total=reduce(lambda x,y:x+y,prices)
# print(total)
#59
#Mini Project (Student Management System)
# dicti={}
# marks_dict={}
# listy=[]
# sum_store=[]
# def student_info():
#     global dicti
#     global listy
#     nos=int(input("How many students you wanna add: "))
#     for n in range(1,nos+1):
#         name=input("Enter Student's Name: ")
#         roll_num=int(input("Enter Students's Roll Number: "))
#         print(f"Now you have to enter marks:")
#         marks_eng=int(input("Enter Marks of English: "))
#         marks_urdu=int(input("Enter Marks of Urdu: "))
#         marks_math=int(input("Enter Marks of Math: "))
#         dicti[roll_num]={"name":name,"roll":roll_num}
#         dicti[roll_num]["marks"]={"eng":marks_eng,"urdu":marks_urdu,"math":marks_math}
#         # from functools import reduce
#         # Total=reduce(lambda x,y:x+y,dicti[roll_num]["marks"].values())
#         # dicti[roll_num]["Total_marks"]=Total
#         marks_dict[roll_num]=dicti[roll_num]["marks"].values()
#         print(f"This is marks_dict: {marks_dict[roll_num]}")
#         sum_store=(sum(dicti[roll_num]['marks'].values()))
#         print(f"This is the total of roll no {roll_num}: {sum_store}")
#         print(f"This is the dictii of this student you just added:\n{dicti[roll_num]}")
#         listy.append(f"Total marks of Roll No {roll_num} are {sum_store}")
#     print(f"This is the dictii:{dicti}")
#     for i in listy:
#         print(i)
#     print(f"This is marks_dict all: {marks_dict}")
# student_info()









    




