# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:22:25 2023

@author: hp
"""

# Exercise 5: Compute area of Circle 
# Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
r=int(input("Enter the radius of the circle: "))
a=pi * (r**2)#"*" is an arithmetic operator equivalent to multiplication.
print("The area of your circle is ", a)