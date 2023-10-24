# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:31:15 2023

@author: hp
"""

# Exercise 5: Cities
# Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country='Philippines'):
    cc=f"{city.title()} is in the {country.title()}."
    print(cc)

describe_city('Manila')
describe_city('Dubai', 'United Arab Emirates')
describe_city('Davao City')