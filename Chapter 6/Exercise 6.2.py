# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:05:13 2023

@author: hp
"""
while True:
    age=int(input("Enter your age: "))
    if age<3:
        print("The ticket is free")
    elif age>=3 and age<12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")
    finish=(input("Are you finish buying tickets? "))
    if finish=="yes":
        print("Thank you for buying.")
        break
    



    
        
    