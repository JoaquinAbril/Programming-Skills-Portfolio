# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:07:50 2023

@author: hp
"""

# Exercise 4: Rivers 
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.
dictionary={"Nile River":"The longest river in the world.",
"Amazon River":"Second longest and the largest by water flow.",
"Yangtze River":"The longest river in Asia."}
for d in dictionary:
    print(d,":",dictionary[d])