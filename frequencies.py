"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

import string


def frequencies(items):
    frequencies = {}
    # Your code goes here
    dict={}
    for i in range (len(items)):
        if(isinstance(items[i],str)==False):
            items[i]=str(items[i])
    for number in items:
        count=items.count(number)
        dict[number]=count
    return dict
