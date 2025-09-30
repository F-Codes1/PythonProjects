import os    
os.system('cls')
#File Handling
# f=open("Nf.txt","a")
# f.write("My name is Bisma\nI am 13 yeras old!")
# f.close()
# f=(open("Nf.txt","w+"))
# a=[23,24,35,44,32,12,31,28,26,41]
# b=["a,b,c,d,e,f,g,h,i,j"]
# c=b[0].split(",")
# student=[]
# for i in range(len(a)):
#     student.append(f"{c[i]}: {a[i]}")
# f.write(f"Marks Of Students:\n{student}")
# f.seek(0)
# print(f.read())
# f.close()
#adding 5 nums to each student in file Nf:
# f=open("Nf.txt","r+")
# f.readline()
# data=(f.readline())
# for i in range(len(data)):
#     name,num=data[i].split(":")
#     num+=5
# x=data[0].split(":")
# print(x) 
#Practice
#1
# with open("practice.txt",'w+') as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in java.")
# with open('practice.txt',"w+") as f:
#     f.write("Hi everyone\nWe are learning File I/O\n")
#     f.write("using java\n")
#     f.write("I like programming in java")
#2
# def rep(x):
#     with open(x,"r+") as f:
#         data=f.read()
#         print(f"Original data:\n{data}")
#         new_data=data.replace("java","python")
#         f.seek(0)
#         f.write(new_data)
#         print(f"New Data:\n{new_data}")
#         f.seek(0)
#         print(f.read())
# rep("practice.txt")
#3
# with open ("practice.txt","r+") as f:
#     f.write("dont")
#     f.seek(0)
#     print(f.read())
#4
# def check_word(x,y):
#     with open(x,"r") as f:
#         data=f.read()
#         if y in data:
#             print(f"{y} found!")
#         else:
#             print(f"{y} not found!")
# check_word("practice.txt","python")
#5
# def check_w(x,y):#x for filename and y for word
#     with open(x,'r') as f:
#         data=f.read()
#         box=data.find(y)
#         if(box!=-1):
#             print(f"{y} found at index: {box}")
#         else:
#             print(f"{y} not found!")
# check_w("practice.txt","everyone")
#6
# def check_line(x,y): #x for filename and y for word
#     with open(x,"r") as f:
#         print(f.read())
#         f.seek(0)
#         box=False
#         check=-1
#         line=1
#         data=f.read()
#         if y in data:
#             f.seek(0)
#             while (box==False):
#                 data=f.readline()
#                 check=data.find(y)
#                 if (check!=-1):
#                     print(f"data:{data}")
#                     print(f"Word Found at line: {line}")
#                     box=True
#                     return
#                 else:
#                     line+=1
#         else:
#             print(f"{y} not Found!")
# check_line("practice.txt","like")
#7 another method        
# def check_line(x,y): #x for filename and y for word
#     with open(x,"r") as f:
#         box=True
#         line=1
#         z=1
#         while box:
#             box=f.readline()
#             check=box.find(y)
#             if (check!=-1):
#                 # print(f"data:{box}")
#                 print(f"Word Found at line: {line}")
#                 return
#             else:
#                 print(f"Loop runs: {z}")
#                 z+=1
#                 line+=1
#         return -1
# print(check_line("practice.txt","jho"))
# with open("sample.txt","w") as f:
#     f.write("1,2,3,4,5,6,7,8,12,13,14,15,17,1618")
# def check_e(x):
#     with open(x,"r") as f:
#         data=f.read()
#         print(data)
#         x=data.split(",")
#         print(x)
#         box=0
#         nums=[]
#         for i in x:
#             if(int(i)%2==0):
#                 box+=1
#                 nums.append(i)
#         print(f"The count of Even Nums: {box}")
#         print(f"The Even Nums are: {nums}")
# check_e("sample.txt")
# 1,2,3,4,5,6,7,8,12,13,14,15,17,1618
# with open("sample.txt","r") as f:
#     data=f.read()
#     print(data)
#     box=""
#     for c in data:
#         if(c==","):
#             print(box)
#             box=""
#             continue
#         else:
#             box=box+c
#     print(box)


    

    








        







