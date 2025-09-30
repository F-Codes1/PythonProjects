import os
os.system('cls')
#Recursion
#1
# total=1    
# def factorial(x):
#     global total
#     if(x==0):
#         return
#     else:
#         total=total*x
#         factorial(x-1)
#     print(f"Factorial is {total}")
# factorial(3)
#2
# def sum(x):
#     if(x==1):
#         return 1
#     return x+(sum(x-1))
# n=sum(5)
# print(n)
#3
# n=int(input("Enter a number: "))
# def rev(n):
#     if(n==0):
#         return
#     print(n)
#     return(rev(n-1))
# rev(n)
#4
# def fact(n):
#     print(f"{n} has been kicked by fac1(n)")
#     if(n==1):
#         return 1
#     else:
#         return n* fact1(n-1)
#5
# def fact1(n):
#     print(f"{n} has been kicked by fact(n)")
#     if(n==1):
#         return 1
#     else:
#         return n* fact(n-1)
# print(fact1(n))
#6
# def fib(x,y):
#     if(x==13):
#         return
#     else:
#         z=x+y
#         x=y 
#         y=z
#         print(z)
#         return fib(x,y)
# print(fib(0,1))
#7
# def countdown(x):
#     if(x==0):
#         print("Blast off!")
#     else:
#         print(x)
#         countdown(x-1)
# countdown(5)
#8
# def fact(n):
#     if(n==1):
#         print(f"Finally factorial is found")
#         return 1
#     else:
#         # print(F"Factorial of {n} working!")
#         # print(f"{n}*fact({n-1})")

#         return n*(fact(n-1))
# print(fact(5))
#9
# def factorial(n,depth=0):
#     print(" "*depth + f"enter factorial({n})") 
#     if(n<=1):
#         print(" "*depth + f"return 1")
#         return 1
#     res=n*factorial(n-1,depth+1)

#     print(" "*depth + f"exit factorial({n}) -> {res}")
#     return res
# print(factorial(4))
# def factorial(n):
#     if(n==3):
#         return 6
#     else:
#         y=n*(factorial(n-1))
#         return y
# print(factorial(4))

# total=1
# def factorial(x):
#     global total
#     total=total*x
#     if(x==1):
#         print(f"Factorial is {total}")
#         return
#     else:
#         factorial(x-1)
# factorial(3)
# def backward(x): #3
#     print(x)
#     if(x==1):
#         return 0
#     else:
#         y=(backward(x-1))
#         print(y)
#         print(f"see am i returned? after ")
# print(backward(3))   
# fibanicco Series
# def fib(x):
#     if(x==0):
#         print(f"fib(0) was called!")
#         return 0
#     elif(x==1):
#         print(f"fib(1) was called!")
#         return 1
#     else:
#         print(f"fib{x} was called!")
#         return fib(x-1)+fib(x-2)
# print(fib(5))
# c=-1
# def taking(x):
#     global c
#     print(x[c],end="")
#     c-=1
#     if (c<-len(x)):
#         return
#     else:
#         return (taking(x))
# taking("cat")
# \
# def fact(x):
#     if x==1:
#         print(f"Base case reached! (1) Returned to be multiplied with 2 in last calling!!")
#         return 1
#     else:
#         print(f"calling factorial ({x})!")
#         print(f"its going to solve formula [{x}*fact({x-1})] but jk it cant solve and will return a new call")
#         y=x*fact(x-1)
#         print(f"factorial {x} is solved!")
# print(fact(4))
# def rev(x):
#     if(x==""):
#         return ""
#     else:
#         return x[-1]+rev(x[0:-1])
# print(rev("fatima"))
# name="fara"
# stringy=""
# for i in name[::-1]:
#     stringy+=i
# print(stringy)
# if (name==stringy):
#     print("palindrome")
# else:
#     print('not a palindrome!')
#
# def sum(x):
#     if x==1:
#         print (1)
#         return 1
#     else:
#         y=x+sum(x-1)
#         print(f"Sum of {x} is {y}")
#         return y
# sum(5)
# def nums(x,y=1):
#     print(y)
#     if(y==x-1):
#         return x
#     else:
#         y+=1
#         return nums(x,y)
# print(nums(5))
# def num(x):
#     if(x==0):
#         return 1
#     else:
#         y = num(x-1)
#         # print(f"this is y: {y}")
#         print(f"this is x: {x}")
#         return y 
# print(num(5))
# def sum(x):
#     if(x==1):
#         return 1
#     else:
#         y=x+sum(x-1)
#         print(f"The sum of {x} is {y}")
# sum(3)
#factorial
# def fact(x):
#     if(x==1):
#         print(f"factorial of {x} is 1")
#         return 1
#     else:
#         y=x*fact(x-1)
#         print(f"factorial of {x} is {y}")
#         return y
# print(fact(3))
# print(2*2*2)
# def power(x,y):
#     if(y==0):
#         return 1
#     elif(y<0):
#         print(f"Please enter value <= 0")    
#         return 0                                                                                  
#     else:
#         return x*power(x,y-1)
# print(power(3,-2))
# def listy(*arg,ind=0):
#     print(len(arg[0]) )  
# listy([1,2,3,4])
# def listy(*arg,ind=-1):
#     # z=(len(arg[0]))
    # if(ind==z):
    #     return arg[0][-1]
    # else:
    # if(ind==len(arg[0])):
    #     return 1
    # else:
    #     return listy[]
    #     print(arg[0][ind])
    #     return
        # print(arg[0][ind])
        # return y
    # print(z)
# print()listy([1,2,3,4])

# def listy(lst,ind=0):
#     if(ind==len(lst)-1):
#         print(lst[ind])
#         return lst[ind]
#     else:
#         # if(type(lst[ind])==int):
#         #     print(lst[ind])
#         #     return listy(lst,ind+1)
#         # else:
#         #     return(listy(lst[ind]))
#         if(type(lst[ind])==int):
#             print(lst[ind])
#         else:
#             listy(lst[ind])
#         return(listy(lst,ind+1))
# (listy([1,[2,3],[4,[5,6]],7]))
# # listy=[1,[2,3],[4,[5,6]],7]
# # print(listy[1])
# # def listy(lst,ind=0):
# #     if(ind==len(lst)-1):
# #         print(lst[ind])
# #         return lst[ind]
# #     else:
# #         y= listy(lst,ind+1)
# #         print(lst[ind])
# #         return y
# # (listy([1,[2,3],[4,[5,6]],7]))
# # print("\n")
# # print(listy([1,2]))
# nums=[1,2,3,1]
# nums=[1,2,3,4]
# st=set()
# def common_checks(*arg):
#     st=set()
#     for i in arg[0]:
#        for j in arg[1]:
#            if (i==j):
#                st.add(i)
#     print(f"These are the common nums: {st}")
# common_checks([1,2,3,1],[1,2,3,4])
# def cc(*args):
#     print(set(args[0]).intersection(set(args[1])))
#     print(set(args[0])&set(args[1]))
# cc([1,2,3,4],[4,65,7,2])
# def sd(x,y):
#     print(x^y)
# sd({1,2,3,4},{3,4,5,6})
# A={1,2,8,9,6,23,4,5,6}
s="A man,a plan,a canal: Panama"
# s=[1,23,4,5]
# def rev(x):
#     x=""
#     for i in s:
#         if i.isalpha():
#             x+=i
#     st=""
#     for i in x:
#         st=i+st
#     print(f"Original: {x}")
#     print(f"Reversed: {st}")
#     if (x.lower()==st.lower()):
#         return True
#     else:
#         return False
# print(s)
# print(rev(s))
# def rev(x:str):
#     st=" "
#     for i in x:
#         if i.isalnum():
#             st+=i.lower()
#     print(f"Without Punct: {st}")
#     print(f"String Reversed:{st[::-1]}")
#     return (st==st[::-1])
# print(rev("A man,a plan,a canal: Panama"))


    


