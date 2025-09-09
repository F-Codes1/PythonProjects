import os
os.system('cls')
#Loops
#1
# i = 10
# while i<15:
#     print("hello World")
#     i = i+1
#2
# total = 0
# answer = "yes"
# while answer=="yes":
#     num = int(input("enter a numvber you want to add: "))
#     total = total + num 
#     answer = input("you wanna add more nums yes/no: ")
# print(f"This is you added num= {total}")
#3
# num = int(input("enter a number:")) #num = 4
# total = 0
# total = total + num   #total = 0+4 =4
# print(f"total so far :{total}")
# yesno =input("Do you wanna add more nums? yes/no? ")
# if(yesno=="yes"):
#     num = int(input("enter a number:")) #num = 2
#     total = total + num 
#     print(f"total so far:{total}")  #total = 4+2 =6
# yesno=input("Do you wanna add more nums? yes/no? ")
# if(yesno=="yes"):
#     num = int(input("enter a number:")) #num = 1
#     total = total + num  
#     print(f"total so far:{total}")  #total =6+1 = 7
# if(yesno=="yes"):
#     num = int(input("enter a number:"))
#     total = total + num   
#     print(f"total so far:{total}") 
# else:
#     print(f"OKay!")
# print(f"total so far:{total}") 
#4
# print("Enter 5 fruits you wanna add to cart")
# fruit_list=[]
# i = 1
# while(i<=5):
#     fruits = input(f"enter fruit no {i}: ")#mango
#     fruit_list.append(fruits)
#     i+=1
# print(f"These are your fruits added to cart: {fruit_list}")
#5
# i = 0
# while(i<6):
#     print("i:",i)
#     i+=1
#6
# total = 0
# user="yes"
# while(user=="yes"):
#    num =  int(input("write a number to add: "))
#    total = total+num
#    user=input("You wanna add more...Yes/No? ").lower()
# print(f"total : {total}")
#7
# total = 0
# while True:
#     num = int(input("Enter the number you wanna add: "))
#     total = total +num
#     choice = input("You wanna add more nums?Yes/No? ").lower()
#     if(choice!="yes"):
#         break
# print(f"Total: {total}")
#8
# print("Enter 5 Fruits: ")
# i=1
# fruit_list=[]
# while(i<=5):
#     fruits = input(f"Enter fruit no {i}: ")
#     fruit_list.append(fruits)
#     i+=1
# print(f"Your fruits are: {fruit_list}")
#9
# i = 5
# listt=[]
# while(i>=0):
#     print(f"i:{i}")
#     listt.append(i)
#     i = i-1
# print(f"list of i's:{listt}")
#10  
#FACTORIAL
# total = 1
# i=5
# while(i>=1):
#     total = total*i  
#     i-=1
# print(f"Factorial of 5: {total}")
#11
#FACTORIAL INPUT
# fac = int(input("Enter the num for Factorial: "))
# total = 1
# i=fac   
# while(i>=1):
#     total=total*i  
#     i-=1
# print(f"Factorial of {fac} is {total}.")
#------------------
#ANOTHER LOGIC FOR FACTORIAL
# total = 1
# i=1
# fac = int(input("Enter a num for factorial: "))
# while(i<=fac):
#     total=total*i
#     i+=1
# print(f"Factorial of {fac} is {total}")
#12   continuous Sum from 1 to 10 values like 0+1=1 1+1=2 2+2=4 4+3=7
# prev_num = 0
# i=1
# while(i<10):
#     prev_num=prev_num+i
#     i+=1
# print(f"Sum from 1 tpo 10:{prev_num}")
#13
#GUESS GAME 
# r_num = 11
# while True:
#     u_num= int(input("Guess the Secret number: "))
#     if(u_num==11):
#         print("You Got it Right!!!")
#     elif(u_num>9 and u_num<12):
#         print("It was Close!")
#     elif(u_num<9 and u_num>7):
#         print("It was Close!")
#     else:
#         print("Too Far!")
#     if(u_num==11):
#         break
#14
#REVERSING NUMBERS(MY OWN LOGIC)
# u_num = input("Enter a Positive Integer: ")
# length = len(u_num)
# total = " "
# i= -1        
# while(i>=-length):
#     total = total + u_num[i]
#     i-=1
# print(f"your reversed num: {total}")
#Another Method for REVERSE 
#15
# num = input("Enter a number: ") 
# pr = " "
# i=1
# while(i<len(num)):
#     pr = num[i]+pr
#     i+=1
# print(f"reversed Number: {pr}")
#16
#Multiplication table 
# num = int(input("Enter a number you want the multiplication table of: "))
# print(f"Table of {num}")
# i = 1
# while(i<=10):
#     t= i*num
#     print(f"{num}\t*\t{i}\t=\t{t}")
#     i+=1
#17
# num = (input("Enter a number whose total elements you wanna count: "))
# i=1
# n=0
# length=len(num)
# while(i<=length):
#     n = i
#     i+=1
# print(f"Count:{n}")
#18
# total = 0
# user="yes"
# num=0
# while(user=="yes"):
#     num = int(input("Enter num:"))
#     total = num+total
#     user=input("Do you wanna add more? ").lower()
# print(f"Your Total: {total} ")
#19
#PRIME NUMBERS
# num =int(input("Enter a num to check if its prime or not: "))
# i=1
# check="Prime"
# while (i<=num):
#         if(num%i==0):
#             if(i!=1 and i!=num):
#                 check="Not Prime"
#                 break
#         i+=1
# if(check=="Not Prime"):
#     print("not prime")
# else:
#     print("Prime")
#20
#Another Method:
# num = int(input("Enter a Number: "))
# ch="prime"
# i=1                    #15  15/1  15/3
# while True:           #7  7/1  7/7  7/6
#     if(num%i==0):
#         if(i!=1 and i!=num):
#             ch = "non_prime"
#             break
#     if(i>num):
#         break
#     i+=1
# if(ch=="non_prime"):
#     print("Not a Prime Number")
# else:
#     print("Prime Number")
#21
# total = 0
# user=int(input("Enter a number you wanna add--type 0 to Stop: "))
# while(user!=0):
#     total = total+user
#     user=int(input("Enter a number you wanna add--type 0 to stop: "))
# print(f"Sum is: {total}")
#22
#printing from list
# listt = [1,4,9,16,25,36,49,64,81,100]
# sett=set()
# length=len(listt)
# i=0
# while(i<=length-1):
#     print(listt[i])
#     i+=1
#23
# tup=(1,4,9,16,25,36,49,64,81,100)
# print(tup)
# num = int(input("enter a num you wanna find: "))
# i=0
# find=False #we can even set it as True 
# while(i<len(tup)):
#     if(tup[i]==num):
#         find=True
#         break   #set break here so that loop cant going and then it can change find it shouldnot change it continuously.
#     else:
#         find=False
#     i+=1
# if(find==True):
#     print("Number Finded")
# else:
#     print("Number Not Finded")
# #24
# #Another way to check if a num is present or not
# tup=(1,4,9,16,25,36,49,64,81,100)
# print(tup)
# num = int(input("enter a num you wanna find: "))
# i=0
# find=False
# while(i<len(tup)):
#     if(tup[i]==num):
#         find=True   #set break here so that loop cant going and then it can change find it shouldnot change it continuously.
#     i+=1
# if(find==True):
#     print("Number Finded")
# else:
#     print("Number Not Finded")
#25
# tup = (1,4,7,9,18,45,87,33,22,56,7,9)
# num = int(input("Enter a num, we will check its presence: "))
# i=0
# while(i<len(tup)):
#     if(tup[i]==num):
#         print(f"founded at index {i}")
#     else:
#         print("founding...")
#     i+=1
#26
# Another Method for prime numbers
# i = 1
# num=int(input("Enter a number"))  #15
# box=""
# while(i<=num):
#     if(num%i==0):
#         box =box +  str(i)
#     i+=1
# if(len(box)==2):
#     print("Prime Number")
# else:
#     print("Not a Prime Number")
#27
#Continue in While
# i=1
# while (i<=5):
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1
#28
#Odd Numbers
# i=0
# while(i<=10):
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
#29
#Odd Numbers:
# i = 0
# while(i<=10):
#     if(i%2!=0):
#        i+=1
#        continue
#     print(i)
#     i+=1
#Test of while Loops
#1-Break(keep asking nums from user until negative num)
# box = []
# while True:
#     num=int(input("Enter Numbers: "))
#     if(num<0):
#         box = num
#         break
# print(f"You entered negative number : {box}, So we stopped asking")
#2-Continue
# i=0
# while(i<=10):
#     if(i==5):
#         i+=1
#         continue
#     print(i)
#     i+=1
#3-Combination
# box=[]
# user="dont stop"
# while(user!="stop"):
#     user=input("Enter a word: ").lower()
#     if(user=="skip"):
#         continue
#     if(user=="stop"):
#         break
#     box.append(user)
# print(f"List of Words: {box}")
#FOR
#30
# fruits = ["apple","banana","cherry"]
# for i in range(len(fruits)):
#     print(f"fruit-{i+1} is {fruits[i]}")
#31
# another way
# fruits = ["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)
# word =  "fatima"
# for a in word:
#     print(a)
#32
#USE of ENUMERATE:
# names = ["ali","umer","sarah"]
# for i,name in enumerate(names):
#     print(i,name)
#33
# for i in range (5): # for i in (0,1,2,3,4)
#     print("hello")
# for e in range(5):   #for each character e in (f,a,t,i,m,a)
#     print("hello")
# i=0
#34
#USE of Else and BREAK In While
# listt=[0,1,2,3,4,5,6,8,5,4,3]
# num = int(input("Enter a  num: "))
# # check=False
# while(i<len(listt)):
#     if(num==listt[i]):
#         print("Founded")
#         break
#     i+=1
# else:
#     print("Not Founded")
#35
#USE off Else and break in For
# listt=[0,1,2,3,4,5,6,8,5,4,3]
# num = int(input("Enter a num: "))
# for n in listt:
#     if(n==num):
#         print("Founded")
#         break
# else:
#     print("Not Founded")
#36
# listy = [1,4,9,16,25,36,49,64,81,100]
# for i , l  in enumerate(listy,start=1):
#     print(i,"--",l)
#37
# tup = (1,4,9,16,25,36,49,64,81,100)
# user = int(input("Enter a num to check if it's present in tuplr or not:  "))
# print(tup)
# for i in range(len(tup)):#0---9
#     if(tup[i]==user):
#         print(f"Founded at index {i}")
#         break
#     # else:
#     #     print("founding....")
# else:
#     print("Not Founded!")
#37
#RANGE
# for i in range(10,0,-1):
#     print(i)
# for i in range(1,21):
#     print(f"2 * {i} = {2*i}")
#------------
#38
# print(f"From 100 - 1:")
# for i in range(100,0,-1):
    # print(i)
#-------------
#39
# num = int(input("Enter a number whose Table you wanna print: "))
# for r in range(1,11):
#     print(f"{num}\t*\t{r}\t=\t{num*r}")
#40
#Sum of 1st 5 numbers using range and for
# total = 0
# for i in range(1,6): #1 2 3 4 5
#     total = total + i
# else:
#     print(f"sum of 5 natural nums: {total}")
#41
#Sum of 1st 5 numbers using while
# i=1
# total = 0
# while(i<=5):
#     total = total + i
#     i+=1
# else:
#     print(f"Sum of values: {total}")
#42
#factorial of first 5 numbers:
# total=1
# for i in range(5,0,-1):
#     total=i*total
# else:
#     print(f"The factorial of 5 is: {total}")
#43
#Right Triangle Printing
# n=1
# for i in range(0,5):              #0,1,2,3,4
#     for j in range(0,n):          #0,1
#        print("*" , end=" ")
#     n+=1
#     print()    
#44
#Another Method for right triangle
# for i in range(0,7):              
#     for j in range(i):         
#        print("*" , end=" ")
#     print() 
#45
#Square Printed
# x=5
# y=5
# for i in range(x+1):    #0,1,2,3,4,5
#     for j in range(y+1):   #0,1,2,3,4,5
#         print("*" ,end=" ")
#     print()
#46
#Printing I (My Own Logic)
# x=5
# y=6
# for i in range(x+1):    #0,1,2,3,4,5,6,7
#     if(i==1 or i==2 or i==3 or i==4):
#         for k in range(y+1):
#             if(k==3):
#                 print("*" , end=" ")
#             else:
#                 print(" ",end=" ")
#     else:
#         for j in range(y+1):   
#          print("*" ,end=" ")
    # print()
#47
#Printing I (chatGpt Logic + My Logic)
# x = 6
# y = 8
# for i in range(x+1):
#     for j in range(y+1):
#         if(i==0 or i==6):
#             print("*",end=" ")
#         if(i==1 or i==2 or i==3 or i==4 or i==5):
#             if(j==4):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()
#48
#printing Hollow Square
# x = 6
# for i in range(x+1):
#     for j in range(x+1):
#         if(i==0 or i==6):
#             print("*", end=" ")
#         elif(j==0 or j==6):
#             print("*", end=" ")
#         else:
#             print(" " , end=" ")
#     print()
#49
# x = 10
# y = 17
# for i in range(x):
#     if(i==4 or i==5):
#         for j in range(y):
#             print("*",end=" ")
#     elif(i==0 or i==9):
#         for j in range(y):
#             if(j==5 or j==6 or j==7 or j==8 or j==9 or j==10 or j==11):
#                 print(" ",end=" ")
#             else:
#                 print("*",end=" ")
#     elif(i==1 or i==8):
#         for j in range(y):
#             if(j==6 or j==7 or j==8 or j==9 or j==10):
#                 print(" ",end=" ")
#             else:
#                 print("*",end = " ")
#     elif(i==2  or i==7):
#         for j in range(y):
#             if(j==7 or j==8 or j==9):
#                 print(" ",end=" ")
#             else:
#                 print("*",end=" ")
#     elif(i==3 or i==6):
#         for j in range (y):
#             if(j==8):

#                 print(" ",end = " ")
#             else:
#                 print("*",end=" ")
#     print()
#50
#Multiplication Table of 3 using nested For:
# p = 1
# n = 4
# for i in range(1,4):
#     for j in range(p,n):
#         print(("3"),"*", (j), "=",(3*j),end='     ')
#     p+=3
#     n+=3    
#     print()
#51
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#   1 2 3 4 5
# r = 5
# c = 2
# for n in range(r):
#     for j in range(1,c):
#         print(j , end=" ")
#     c+=1
#     print()
#51
#Another method
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for i in range (2,7):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
#52
#Upside Down
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# for i in range (6,1,-1):
#     for j in range (1,i):
#         print(j,end=" ")
#     print()
#53
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# x=1
# for i in range(1,6):
#     for j in range(i,2*i):
#         print(i,end=" ")
#     print()
# for i in range(2,7):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
#54
# for i in range(1,4):
#     for j in range (1,4):
#         print(j,end=" ")
#     print()
#55
#Pyramid Of Numbers
# n = 4
# for i in range(2,7): 
#     print((" ")*(n),end=" ")
#     for j in range(1,i):  #1
#         print(j,end=" ")
#     print()
#     n-=1
#56
#Upside Down Pyramid
# n = 0
# for i in range(6,1,-1):
#     print((" ")*n,end=" ")
#     for j in range(1,i):
#         print("*",end=" ")
#     print()
#     n+=1
#57
#printing upside down pyramid
# n=4
# for i in range(1,6):
#     print((" ")*n,("*")*i)
#     n-=1
n = 2
for i in range(2,5):
    print((" ")*n,end=" ")
    for j in range(1,i): 
        
        print(j,end=" ")
    print()
    n-=1
        