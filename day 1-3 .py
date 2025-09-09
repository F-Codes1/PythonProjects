# import os
# os.system('cls')
# # # name = "fatima faheem"
# # # age = "19"
# # # lang = "python"
# # # print(f"My name is {name}, My age is {age}, i am doing {lang}.")
# # # x = input("Enter your file name here: ")
# # # print(x)
# # # y = (x.endswith(".txt"))
# # # print(y)
# # # name = "Fatima"
# # # print("name after capitalization is:",(name.capitalize()))
# # # print("first letter capitalize is:",name[0].capitalize(),"remaining as it is:",name[1])
# # # name = "fatimaaafaaaheeem"
# # # rep = (name.replace("a","@"))
# # # print("All a's in your name will be replaced by @:",rep)
# # # u_name = input("Enter the name:")
# # # u_char = input("Enter the char whose index you wanna find:")
# # # occ = (u_name.find(u_char))
# # # print("The char",u_char,"is appearing at index",occ,"\tThanks...")
# # name = input("Enter a name or sentence: ")
# # print("First char is:",name[0])
# # print("last char is:",name[-1])
# # print("first 5 characters are :",name[0:5])
# # print("every 2nd character is :",name[0::2])
# # print("Whole sentence reversed is :",name[::-1])
# # # name = input("Enter a name or sentence: ")
# # # print("your input text is: ",name)
# # # print("the e's in your text replaced by 3's: ",name.replace("e","3"))
# # # print("The number of a's in your text are: ",name.count("a"))
# # # print("The first o in your text is on index: ",name.find("o"))
# # # print("First 5 characters in your text are: ",name[0:5])
# # # print("Last 5 characters are: ",name[-5:])
# # # name = "Fatima"
# # # print("name after capitalization is:",(name.capitalize()))
# # # second = (name[2].capitalize()) #printing the t as T
# # # before = name[0:2]  #printing before the T
# # # last = name[3:]
# # # print("whole: ",before+second+last)
# # 
# # name = input("writre the name: ")
# # u_char = input("write the char: ")
# # index = name.index(u_char)
# # mainchar = (name[index].capitalize())
# # before = name[0:index]
# # after = name[index+1:]
# # print("your name: ",name)
# # print("whole name withj specific char capitalizxed: ",before+mainchar+after)
# # name = "fatima"
# # index = name.index("t")
# # print(index)
# # name = "fatima"
# # print(name.upper())
# # print(name.capitalize())
# # print(name[1].upper())
# # print(name[1].capitalize())
# # user=input("Enter username: ")
# # if(user=="123456"):
# #     passw = input("Enter password: ")
# #     if(passw=="abcd"):
# #         print("Login Succesful")
# #     else:
# #         print("Password is incorrect!")
# # else:
# #     print("access Denied*")      
# #   
# # num = int(input("Enter the number here: "))
# # if(num>0):
# #     if(num%2==0):
# #         print("Even Number!")
# #     else:
# #         print("Odd Number!")
# # elif(num==0):
# #     print("You Enterted 0!")
# # else:
# #     print("You Entered Negative Number!")                   
# # RESTAURANT MENU
# # menu = input("enter your meal/> Choose: PIZZA, BURGER, PASTA..'WRITE IN SMALL CASE PLEASE'..: ")
# # if(menu=="pizza"):
# #     vegnonveg= int(input("You want veg or non veg pizza?..Press 1 for veg and 2 for non veg: "))
# #     if(vegnonveg==1):
# #         print("Veg is for 500!")
# #     elif(vegnonveg==2):
# #         print("Non-veg is for 700!")
# #     else:
# #         print("please enter 1 or 2 if you want veg or non veg Pizza.")    
# # elif(menu=="burger"):
# #     print("Price of Burger is 300!")
# # elif(menu=="pasta"):
# #     print("Price of Pasta is 400!")
# # else:
# #     print("NOT AVALAIBLE!")        
# # ATM
# # pin = int(input("Enter your pin: "))
# # if(pin==5678):
# #     amount = int(input("Enter Amount You Want To Withdraw: "))
# #     if(amount<=10000):
# #         print("Withdrawal Successful!!")
# #     else:
# #         print("Limit Exceeded!!")   
# # else:
# #     print("WRONG PIN!")         
# # name = input("Enter Your Name: ")
# # print("WELCOME!", name)
# # person = input("Are you a Member or a Guest?").lower()
# # if(person == "member"):
# #     print("CONGRATS on 10% Discount!")
# #     order = input("What will you like order Sir/Mam? \nYou can have Coffee, Tea and Sandwich..Please write here: ").lower()
# #     if(order=="coffee"):
# #         size = input("Size of Coffee should be 'Small/ Large/ medium'..?: ").lower()
# #         if(size=="small"):
# #             print("Price of Small Coffee is Rs 100")
# #         elif(size=="medium"):
# #             print("Price of Medium Coffee is Rs 150")
# #         elif(size=="large"):
# #             print("Price of Large Coffee is Rs 200")   
# #         else:
# #             print("Please Enter From Given Sizes...")         
# #     elif(order=="tea"):
# #         colour= input("You want the colour of tea to be Green or Black?").lower()
# #         if(colour=="green"):
# #             print("Price of Green Tea is Rs 80")
# #         elif(colour=="black"):
# #             print("Price of Black Tea is Rs 70")
# #         else:
# #             print("Please Enter from Given Colours Only..")    
# #     elif(order=="sandwich"):
# #         vegnonveg = input("You want Veg or Non-Veg Sandwich: ").lower()
# #         if(vegnonveg=="veg"):
# #             print("Price of Veg sandwich is Rs 120")
# #         elif(vegnonveg=="non-veg"):
# #             print("Price of Non-Veg is Rs 150")   
# #         else:
# #             print("Please Enter Veg or Non-Veg..")         
# #     else:
# #         print("SORRY! We dont have that...")
# # else:
# #     print("You are not a Member, SORRY!")                        
# name = input("Enter your name : ")
# print("Welcome!",name)
# status = input("Are you a memb0.er or a Guest?..").lower()
# if(status=="member"):
#     discount= 0.10
# else:
#     discount=0
# price=0    
# order=input("MENU:\n'Coffee','Tea','Sandwich'\nSmall Coffee: Rs 100, Medium Coffe: Rs 150, Large Coffee: Rs 200\nGreen Tea: Rs 80, Black Tea: Rs 70\nVeg Sandwich: Rs 120, Non-Veg Sandwich: Rs 150\nPlease Enter Your Choice: ").lower() 
# if(order=="small coffee"):
#     price=100
# elif(order=="medium coffee"):
#     price=150
# elif(order=="large coffee"):
#     price=200
# elif(order=="green tea"):
#     price=80
# elif(order=="black tea"):
#     price=70
# elif(order=="veg sandwich"):
#     price=120
# elif(order=="non-veg sandwich"):
#     price=150
# else:
#     print("Order not available!")                
# final_price=price*(1-discount)
# if(final_price>0):
#     print("*........RECIEPT........*")
#     print("Your Order: ",order.capitalize())
#     print("Price of Order: ",price)
#     if(status=="member"):
#         print("You got 10% Discount, Your Final Price is: ",final_price)
#     elif(status=="guest"):
#         print("Your Final Price is: ",final_price)    
#     print("..........THANK YOU FOR ORDER............")
# else:
#     print("Order Something to generate Receipt!")



# order=input("MENU:\n'Coffee','Tea','Sandwich'\nSmall Coffee: Rs 100, Medium Coffe: Rs 150, Large Coffee: Rs 200\nGreen Tea: Rs 80, Black Tea: Rs 70\nVeg Sandwich: Rs 120, Non-Veg Sandwich: Rs 150\nPlease Enter Your Choice: ").lower() 
# if(order=="small coffee"):
#     price=100amna rupies and