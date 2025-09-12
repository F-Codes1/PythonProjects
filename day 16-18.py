import os
os.system('cls')
# Practice:
# listy=[]
# list = [1,2,3,4,5]
# for n in list:
#     x = n*2
#     listy.append(x)
# else:
#     print(f"list:{listy}")
#2 
# Multiplication table from 1-3 using nested for loop:
# for i in range(1,4):
#     for j in range(1,11):
#         print(f"{i}\t*\t{j}\t=\t{i*j}")
#     print()
#3
# n=2
# for i in range(1,6):
#     for j in range(1,n):
#         print(j,end=" ")
#     print()
#     n+=1
#4
#Butterfly Printing Short Method:
# n=4
# for i in range(1,6):
#     print(f'{"*"*i}{("  ")*n}{"*"*i}')
#     n-=1
# n=0
# for i in range(5,0,-1):
#     print(f'{"*"*i}{("  ")*n}{"*"*i}')
#     n+=1
#5
#Butterfly Printing Long Method:
# for i in range(1,10):
#     for j in range(1,10):
#         if(i==5):  
#             print("*",end=" ")
#         elif(i==4 or i==6):
#             if(j==5):
#                 print(" ",end=" ")
#             else:
#                 print("*",end=" ")
#         elif(i==3 or i==7):
#             if(j==4 or j==5 or j==6):
#                 print(" ",end=" ")
#             else:
#                 print("*",end=" ")
#         elif(i==2 or i==8):
#             if(j==1 or j==2 or j==8 or j==9):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if(j==1 or j==9):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()
#6
#Printing Even Numbers from list:
# listy=[]
# nums = [1,4,7,10,13,16]
# for n in nums:
#     if(n%2==0):
#         listy.append(n)
# else:
#     print(f"Even Numbers: {listy}")
#7
#Separating odd and even numbers:
# odd=[]
# even=[]
# nums=[1,4,7,10,13,16]
# for n in nums:
#     if(n%2==0):
#         even.append(n)
#     else:
#         odd.append(n)
# else:
#     print(f"Original List: {nums}")
#     print(f"Odd Numbers: {odd}")
#     print(f"Even Numbers: {even}")
#8
#Use of enumerate:
# fruits = ["apple","banana","cherry"]
# for i,fruit in enumerate(fruits):
#     print(f"{i}- {fruit}")
#9
#Use of While + for Nested Loops:
# i=1
# while(i<=3):
#     for j in range(1,4):
#         print(i,"*",j,"=",i*j,end="    ")
#     print()
#     i+=1
#10
# Number Pyramid (Simple)
# for i in range(2,7):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
#11
#Number pyramid (Centered)
# n=4
# for i in range(2,7):
#     print(" "*n,end=" ")
#     for j in range(1,i):
#         print(j,end=" ")
#     print()
#     n-=1
#12
#Sum Until User Tells To Stop:
# sum=0
# while True:
#     num=int(input("Enter a number you wanna add: "))
#     sum+=num
#     user=input("Do you wanna add more?type no to stop ").lower()
#     if(user=="no"):
#         print(f"Your Total Sum is: {sum}")
#         break
#13
# Password Retry System:
# print(f"Hello User 123!") 
# ps = "abc123" 
# while True:
#     user=input("Enter your Password: ")
#     if(user==ps):
#         print(f"You are logged in successfully...") 
#         break
#     else:
#         print("Try Again")
#14
#Shopping List:
# list = []
# print(f"Please Enter 5 items in Cart")
# i=1
# while (i<6):
#     items=input(f"Item {i}: ")
#     list.append(items)
#     i+=1
# else:
#     print(f"Your list: {list}")
# #OR THIS WAY
# # print(f"Your Items Are: ")
# # for i, l in enumerate(list):
# #     print(f"{i+1}- {l}")
#15
#Finding Greatest Num Using Loop:
# b_n=0
# list=[23,56,11,89,34] 
# for l in list:
#     if(l>b_n):
#         b_n=l
# else:
#     print(f"List: {list}")
#     print(f"Greatest Num: {b_n}")
#16
#Counting Vowels:
# word = input("Enter a word or a Sentence: ") #potato
# total = []
# for w in word:
#     if(w=="a" or w=="e" or w=="i" or w=="o" or w=="u"):
#         total.append(w)
# counting=len(total)
# print(f"Total vowels in your word are {counting}")
# print("The vowels in your word are: ")
# for t in total:
#     print(t,",",end=" ")
#17
#Reversed String:
# word = input('Enter a word To reverse it: ')
# i=-1
# while (i>=-len(word)):
#     print(word[i],end=" ")
#     i-=1
#18
#Removing Duplicates from a List Without Using Set
# list = []
# nums = [2,4,2,5,6,4,7,2] 
# for i in nums:
#     if i not in list:
#         list.append(i)
# print(f"List = {list}")
#19
#Removing Duplicates from a List Without Using Set(Another Method)
# list=[]
# i=0
# nums = [2,4,2,5,6,4,7,2] 
# while (i<len(nums)):
#     if(nums.index(nums[i])==i):
#         list.append(nums[i])
#     i+=1
# print(f"original List: {nums}")
# print(f"Corrected List: {list}")
#20
#Finding Common Letters Between Words:
# set=set()
# print("Enter Words Down Here")
# word_1=input("Enter 1st Word: ").lower()
# word_2=input("Enter 2nd word: ").lower()
# for i in word_1:
#     for j in word_2:
#         if(j==i):
#             set.add(i)
# print(f"You entered: {word_1} and {word_2}")
# print(f"Similar Letters are: {set}")
#21
#simple loop through Dicts
#Dictionaries Practice
# student = {'name':"Fatima","age":18,"city":"Lahore"}
# # print(student['name'])
# # print(student['age'])
# # print(student['city'])
# for i in student.values():
#     print(i)
#22
#Manullay Entering user details through empty dict
# math = int(input("Enter Marks of Math: "))
# eng_a= int(input("Enter Marks of eng_a: "))
# eng_b = int(input("Enter Marks of eng_b: "))
# urdu= int(input("Enter Marks of urdu: "))
# dict = {}
# dict["name"]="fatima"
# dict["Marks"]={}
# dict["Marks"]["Subjects"]={}
# dict["Marks"]["Subjects"]["Math"]=math
# dict["Marks"]["Subjects"]["English"]={}
# dict["Marks"]["Subjects"]["English"]["English_A"]=eng_a
# dict["Marks"]["Subjects"]["English"]["English_B"]=eng_b
# dict["Marks"]["Subjects"]["Urdu"]=urdu
# print(dict)
#23
# Creating and Filling an Empty Dictionary:
# nums = int(input("How many Students you wanna input Here: "))
# dict = {}
# # student={"Name":name,"Roll_no":rn}
# for i in range(0,nums):
#     name =input("Enter the Name of Student: ")
#     rn= int(input("Enter the Roll no of student: "))
#     dict_i={}
#     dict_i = {"Name":name,"Roll_No":rn}
#     dict[i]=dict_i
#24
# nums=int(input("Enter how many students info you wanna add: "))
# students={}
# for i in range(0,nums):
#     name=input("Enter the Name of Student: ")
#     roll=input("Enter the Roll No of Student: ")
#     students[f"student_{i}"]={}
#     students[f"student_{i}"][name]=roll
# print(students)
#25
#Storing the Students name in dict by their Roll Nums:
# dict={}
# nums = int(input("How Many Students You Wanna Add: "))
# for n in range(1,nums+1):
#     name = input(f"Enter Name of Student {n}: ")
#     roll = input(f"Enter Roll_No of Student {n}: ")
#     dict[roll]=name
# user = input("Enter Roll no Student whom you wanna Find: ")
# print(dict[user])
# user =input("Enter Roll no whose name you wanna update: ")
# if (user in dict):
#     print(f"For roll no {user} the previous name is {dict[user]}.")
#     new=input(f"What's the new name for roll no {user}: ")
#     dict[user]=new
# print("New Name is Updated Successfully.") 
# user = int(input("Enter the roll no of student who you wanna delete from record: "))
# if user in dict:
#     del dict[user]
# print(dict)
#26
# students= {"Ali":{"English":90,"Urdu":70},
# "Sara":{"English":80,"Urdu":87},
# "Ahmad":{"English":99,"Urdu":66}}
# way-1(using single loops)
# for i,g in students.items():
#     print(f"{i}'s Marks: {g}")
# way-2(using nested loops)
# for k in students:
#     print(f"{k}'s Marks: ",end=' ')
#     for v in students[k].items():
#         print(f"{v}",end=" ")
    # print()
# friends = {"Ali": ["Sara","Umer"], "Fatima": ["Ayesha","Hassan"]}
# for peep in friends:
#     print(f"{peep}'s friends: ")
#     for fr in friends[peep]:
#         print(fr)
#     print()
#Test
#1 
#Basic Access
# car= {"brand":"Toyota","Year":2020,"Colour":"white"}
# print(car["Year"])
#2
#Add/Update
# student = {"name":"Ali","age":18}
# student["Marks"]=89
# print(student)
#3
#Looping
# fruits = {"apple":100, "banana":50, "mango":120}
# for i,j in fruits.items():
#     print(f"{i}'price: {j} ")
#4
#Nested Dictionary:
# students = {"sara":{"Maths":80, "Eng":70},
# "Umer":{"Math":85, "Eng":90}}
# name = input("Enter whose Numbers you wanna access: ")
# sub = input("Enter Which Subject: ")
# if name in students:
#     print(f"{students[name][sub]}")











