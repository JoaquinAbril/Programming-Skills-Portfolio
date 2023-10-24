# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Exercise 6: Shrinking Guest List
dinner=["Natazha","Max","Nicole"]
for d in dinner:
    print('May I invite you,',d + " " + 'for dinner?')
print("\n Seems like", dinner[2] + " " + "can't come")
dinner=["Natazha","Max","Nicole"]
print("\nI can only invite two people")
print("I'm sorry", dinner[2], "I can't invite you.")
dinner.pop(2)
dinner=["Natazha","Max","Nicole"]
dinner.pop(2)
print("\n")
for d in dinner:
    print("Good news, you are still invited", d + ".")
del dinner
print("\n")
print("Dinner")

