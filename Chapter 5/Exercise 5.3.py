# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:02:58 2023

@author: hp
"""

#Exercise 3: Glossary 2 ☑️
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
glossary={"bitwise_operator":"A bitwise operator is an operator used to perform bitwise operations on bit patterns or binary numerals that involve the manipulation of individual bits.",
          "data_types":"Data types are the classification or categorization of data items.",
          "print":"The print() function prints the specified message to the screen, or other standard output device.",
          "String":"String is a collection of alphabets, words or other characters.",
          "Integers":"Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."
    }
for g in glossary:
    print(g,"-",glossary[g])