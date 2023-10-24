# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:14:56 2023

@author: hp
"""

# Exercise 5: Pets
# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about each pet.
Fred={"Type of pet":"Dog",
           "Owner":"Joaquin"}
Nathan={"Type of pet":"Dog",
           "Owner":"Joaquin"}
Bay={"Type of pet":"Cat",
           "Owner":"Joaquin"}
Yang={"Type of pet":"Cat",
           "Owner":"Joaquin"}
Cess={"Type of pet":"Cat",
           "Owner":"Joaquin"}
Pets=[Fred,Nathan,Bay,Yang,Cess]
for p in Pets:
    print(p)