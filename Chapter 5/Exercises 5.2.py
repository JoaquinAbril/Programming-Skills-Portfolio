# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 19:28:38 2023

@author: hp
"""

# Exercise 2: Glossary 
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.    
glossary={"bitwise_operator":"A bitwise operator is an operator used to perform bitwise operations on bit patterns or binary numerals that involve the manipulation of individual bits.",
          "data_types":"Data types are the classification or categorization of data items.",
          "print":"The print() function prints the specified message to the screen, or other standard output device.",
          "String":"String is a collection of alphabets, words or other characters.",
          "Integers":"Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."
    }
print("\nBitwise Operator:",glossary["bitwise_operator"],
      "\n\nData Types:",glossary["data_types"],
      "\n\nPrint:",glossary["print"],
      "\n\nString:",glossary["String"],
      "\n\nIntegers:",glossary["Integers"])