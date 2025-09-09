import os
os.system('cls')
# print("hello World")
# library = {"python","English","Maths","python"}
# print(library)
# print(len(library))
# print(type(library))
# listy = [20,30,40]
# listy[0]=100
# print(listy)  loves
# sentence = ("Fatima loves Python Fatima codes in Python").lower()
# print(sentence[7])
# indexx = sentence.index("l")
# print(indexx)
# indexs = sentence.index("e",indexx)
# print(indexs)
# print(f'''Index of L in Love :{indexx},
# Printing second word: {sentence[indexx:indexs+1]}''')
# fruits = ["apple","banana","cherry","banana","apple"]
# print(len(fruits))
# print(f"counting:{fruits.count('banana')}")
# print(fruits.index("cherry"))
# fruits.remove("apple")
# print(f"Removing 1st fruit: {fruits}")
# fruits.pop()
# print(fruits)
# groups = (["Ali","Fatima"],["Umer","Ayesha"])
# print(f"Printing Ayesha:{groups[1][1]}")
# groups[0].append("sara")
# print(f"Added to Tuple :{groups}")
# words = ["python","is","fun"]
# words[2]=words[2].replace("fun","awesome") 
# print(f"we replaced fun :{words}")
# words =" ".join(words)
# print(f"we joined words: {words}")
# a = int(input("Enter 1st numbers : "))
# b = int(input("Enter 2nd numbers : "))
# c = int(input("Enter 3rd numbers : "))
# if (a>b and b>c): 
#     largest=a
# elif (b>a and a>c):
#     largest=b
# else:
#     largest=c
# print("largest: ",largest)
# price = int(input("Enter your Price: "))
# if (price>5000):
#     discount = (0.20)*(price)
# elif(price>=2000 and price<=5000):
#     discount = (0.10)*(price)
# else:
#     discount = 0
# print(f"Your Price: Rs{price}")
# print(f"Your Discount on Rs{price} is {discount}")   
# print(f"Your Total Price is Rs{(price)-(discount)}")
# marks = {"ali":{"english":90,"math":99},
# "sara":{'english':88,"math":90}}
# if (marks["ali"]["math"]>marks["sara"]["math"]):
#     Highest = marks[0].keys
# marks = {"ali":{"english":90,"math":99},
# "sara":{'english':88,"math":90}}
# info = {"student_1":{"name":"fatima","age":19,"grade":"A"
# },"student_2":{"name":"Ali","age":20,"grade":"B"},
# "student_3":{"name":"Ahmed","age":21,"grade":"C"}}
# print("INFO Of Each Student")
# print(info["student_1"])
# print(info["student_2"])
# print(info["student_3"])
# print(f"\nGrade of 2nd Student: {info['student_2']['grade']}")
# info["student_1"]["city"]="Lahore"
# print(f"2nd Student:{info['student_1']}"
# user = {"id":101,"name":"Fatima","orders":[{"order1":{"id":5001,
# "items":[{"product":"book","quantity":2,"price":500},
# {"product":"Pen","quantity":3,"price":700}],
# "Status":{"delivered":"False","date":"20-09-2025"}}}]}
# print(f"User Name: {user['name']}")items:[0,1]
# print(f"Id of user: {user['id']}")
# print(f'''Price of first item: {user['orders'][0]
# ['order1']['items'][0]['price']}''')
# user['orders'][0]['order1']['items'][1]['quantity']=10
# print(f'''Changing quantity of Pens: {user['orders'][0]
# ['order1']['items'][1]['quantity']}''')
# print(f'''Getting the product Perfume: {user['orders'][0]['order1']
# ['items'][0].get('perfume','N/A')}''')
# students = {"ali":{"age":18,"grade":"B"},
# "fatima":{"age":19,"grade":"A"},
# "Umer":{"age":20,"grade":"A+"}}
# print(f"Fatima Marks:{students['fatima'].get('marks')}")
# cityy = input("City of Ali: ")
# students["ali"].update({'city':cityy})
# print(f"Info of Ali: {students.get('ali')}")
# print(f"All info of Umer: {list(students['Umer'].items())}")
# print(f"All info of Fatima: {list(students['fatima'].items())}")
# students.pop("ali")
# print(students)
#SETS---------
#1
# student_ids = {101,102,103,102,101}
# print(f"All Unique IDs: {student_ids}")
# #2
# student_ids = {101,102,103,102,101}
# student_ids.add(104)
# print(f"New added Id: {student_ids}")
# print(f"Sorted set: {sorted(student_ids)}")
# print(f"Un-Sorted set: {sorted(student_ids, reverse=True)}")
# student_ids.update({109,108,106})
# print(f"Updated Set: {student_ids}")
#3
# student_ids = {101,102,103,104,105,106}
# student_ids.remove(103)
# print(f"Removing ids:{student_ids}")
# student_ids.discard(999)#when the value we removing doesnot even exist
# print(student_ids)
# print(student_ids.pop())
#4 
# listyy = [78,98,923]
# # listyy.pop(0)
# print(f"popy: {listyy.pop(1)}") 
# print(listyy)
# print(f"counting:{listyy.count(923)}")
# listyy.reverse()
# print(f"reverse list: {listyy}")
# listyy.insert(1,10000)
# print(listyy)
#5 set discard and remove ways and pop
# student_ids = {101,102,103,104,105,106}
# # student_ids.remove(103)
# # print(f"Removing ids:{student_ids}")
# # student_ids.discard(999)#when the value we removing doesnot even exist
# # print(student_ids)
# print(student_ids.pop())
# student_ids.add(109)
# print(student_ids)
#6 
# updating in sets by .update
# student_ids.update({234,898,765,78,56})
# print(f"Updated: {student_ids}")
#7 UNION 
# A = {1,2,3}
# B = {4,7,9}
# print(f"Union of A and B: {A|B}") __________method 1 
# print(f"Union of A and B:{A.union(B)}")_____method 2
# A = {"apple","banana"}
# B = {"banana","cherry"}
# A.update(B) #another way to take union
# print(A)
# M = {1, "one", (2,3)}
# N = {2, "two", (3,4)}
# print(f"Union of M and N: {M|N}")
#8 Intersection
# M={1,2,3,4,5}
# N={3,4,5,6}
# print(f"both sets:{M}___{N}")
# print(f"Intersection M and N: {M.intersection(N)}")__method 1
# print(f"Intersection N and M: {N.intersection(M)}")__method 2
# print(f"Intersection using &:{M & N}")________method 3
# M.intersection_update(N)__________method 4
# print(f"Intersection using update:{M}")
# Difference
# A = {1,2,3,4,5}
# B = {3,4,5,6}
# print(f"Difference between seT A and set B: {A-B}")___method 1
# print(f"Difference between seT B and set A: {B-A}")___method 2
# print(f"Difference between A and B: {A.difference(B)}")method3
# X = {"apple","banana","cherry"}
# Y = {"banana","cherry","Kiwi","anaar"}
# print(f"Difference between seT A and set B: {X-Y}")
# print(f"Difference between seT B and set A: {Y-X}")
# print(f"Difference between A and B: {X.difference(Y)}")
# A = {1,2,3,4}
# B = {1,2,3,4,6,9,78}
# C = {0,1,2}
# print(f"A:{A}")
# print(f"B:{B}")
# print(f"C:{C}")
# print(f"Union: {A|B}")  #there are other ways also for these oper
# print(f"Intersection:{A&B}")
# print(f"A-B Difference:{A-B}")
# print(f"Symmetric difference: {A.symmetric_difference(B)}")
# print(f"Is A subset of B? {A.issubset(B)}") 
# print(f"Is B subset of A? {B.issubset(A)}") 
# print(f"Is A superset of B? {A.issuperset(B)}") 
# print(f"Is B superset of A? {B.issuperset(A)}") 
# print(f"Do A and B have no common elements: {A.isdisjoint(B)}")
# print(f"Do A and C have no common elements: {A.isdisjoint(C)}")
# print(f"Coverting A into frozen: {frozenset(A)}")
# A = frozenset(A)
# print(A)
# print(type(A))
# SORTED SETS
# A = {1,88,9,6,8}
# B = {1,2,3,4,6,9,78}
# C = {0,1,2}
# print(f"A:{A}")
# print(f"B:{B}")
# print(f"C:{C}")
# sorted_set = sorted(A)
# print(f"Sorted Set: {sorted_set}")
#PRACTICE EXAMPLES-----
#Dictionary
# things = {"table":["A piece of furniture","List of facts and figures"],
# "cat":"A small animal"}
# print(f"things: {things}")
# print(f"KEYS: {things.keys()}")
# print(f"VALUES:{things.values()}")
# print(f"TABLE MEANS: {things['table']}")
# print(f"CAT MEANS: {things['cat']}")
# print(f"Second meaning of table: {things['table'][1]}")
#Sets
# lang = {"python","java","C++","python","javascript",
# "java","python","java","C++","C"}
# print(f"Languages: {lang}")
# # lang = list(lang)
# print(f"Counting Classes needed: {len(lang)}")
#Input in Dicts
# Mathh = int(input("Enter Marks of math: "))
# English = int(input("Enter Marks of English: "))
# Urdu = int(input("Enter Marks of Urdu: "))
# Math_Perf = input("Enter Math performance, Good or Bad: ")
# subjects = {}
# subjects["maths"]={"Marks":Mathh,"Performance":Math_Perf}
# subjects["English"]={"Marks":English}
# subjects["Urdu"]={"Marks":Urdu}
# print(subjects)
#Sets
# nums = {9,"9.0"}
# print(nums)
#LOGICAL EXAMPLES
#1
# cart = {"book":500,"pen":50,"bag":2000}
# price_bag = cart["bag"]
# discount=0
# if(price_bag > 1500):
#     discount = (0.10*price_bag)
# else:
#     discount = (0*price_bag)
# price = price_bag - discount
# print(f"Final price of Bag: {price}")
#2
# friends = {"ali":("karachi",22),"Sara":("Lahore",20)}
# print(f"sara is younger and lives in {friends['Sara'][0]}")
#3
# student = {"name":"fatima","marks":{"math":80,"english":90}}
# student["marks"]["english"] += 5 #here we just are increasing 5 in marks of english
# print(student)
#4
# fruits = {"apple","banana","mango"}
# if "oranges" in fruits:
#     print("Orange is available")
# else:
#     print("ORANGE NOT AVILABLE")
#5
# order = {"id":5001,
# "items":[('book',2),('pen',3)],
# "status":{"deli":False}}
# if(order["status"]['deli']==True):
#     print("order was delivered")
# else:
#     print("order aint delivered")
# print("\nAfter Some Time\n")
# order['status']['deli'] = True
# if(order["status"]['deli']==True):
#     print("Order Delivered")
# else:
#     print("Not delivered")
#TEST
#1
# text = "python is fun"
# indexofn = text.index("n")
# print(indexofn)
# print(f"slicing: {text[0:6]}")
# text =text.replace("fun","awesome")
# print(f"replaced: {text}")
#2
# numbers = [100,78,30,40]
# print(f"Original List: {numbers}")
# numbers[2]=35
# print(f"changed 30 to 35: {numbers}")
# numbers.append(50)
# print(f"Added something at end: {numbers}")
# # numbers.sort() # using sort() to find largest
# # print(f"Largest number from list: {numbers[-1]}")
# print(f"Largest number from list: {max(numbers)}") #using max to find largest
#3
# tup = (5,10,15)
# #tup is immutable so we cant change its elemnts
# tuplist = list(tup)
# tuplist [1] = 12
# print(type(tuplist))
# print(f"Tuplist: {tuplist}")
#4
# fruits = {"apple","banana","mango"}
# print(f"Original Fruit Basket: {fruits}")
# fruits.add("oranges")
# print(f"Adding Oranges:{fruits}")
# fruits.discard("banana")
# print(f"After Removing banana: {fruits}")
# print(f"Fruit basket: {fruits}")
# if ("grapes" in fruits):
#     print("graped are also present")
# else:
#     print("No Grapes")
# student = {"name":"fatima",
# "marks":{"math":90,"eng":85}}
# print(student)
# print(f"Math's Marks of fatima:{student['marks']['math']}")
# student["marks"]['eng']= 88
# print(f"Updated eng marks:{student['marks']}")
# student["marks"]['science']=92
# print(f"New subject added:{student['marks']}")
# user = {"orders":[{"product":"Book","quantity":2,"price":500},
# {"product":"pen","quantity":3,"price":50}]}
# quantity_of_book= user['orders'][0]['quantity']
# price_of_book=user['orders'][0]['price']
# tprice_of_book = quantity_of_book*price_of_book
# print(f"Total price of book: {tprice_of_book}")
