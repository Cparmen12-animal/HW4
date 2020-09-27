# -*- coding: utf-8 -*-
"""
Created on 3/6/2020

@author: Christopher

The homework has multiple purposes. anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer

"""
from typing import Any, Set, List, Tuple
from collections import defaultdict, Counter
from typing import DefaultDict
import typing



def anagrams_lst(str1: str,str2: str) -> bool:
    """This function will return true if str1 and str2 are anagrams, false if not"""
    x:List = list(str1)
    y:List = list(str2)
    x.sort()
    y.sort()
    """i tried to do this all in one if statement but python didn't like it very much
    it liked when i clearly defined the lists and types better"""
    if x==y: #convert the string into a string
        return True
    else:
        return False 
    
def anagrams_dd(str1, str2) -> bool:
    """uses a default dictionary to see if str1 and str2 are anagrams. returns true/false """
    dd:DefaultDict[str, int] = defaultdict(int)
    #go through each string and add each character to the defaultdict if not already in there. 
    for char in str1:
        dd[char] += 1 #add to the value the first time
    for char in str2: 
        dd[char] -= 1 #subtract for the second, then we'll be looking for a zero for each character
    """# I googled all(iterable)!it returns true if all elements of the given 
    iterable are true, this seems similar to your any(iterable) suggestion, 
    except i like it better because any != 0 wuold return a false when the 
    overall answer would be true. all returns true when we want true    
    """
    return all(value == 0 for value in dd.values())     
    
def anagrams_cntr(str1:str, str2: str) -> bool: 
    """uses counter to find anagrams, returns true false"""
    #same logic as the defaultdict, but using counters instead
    cc:typing.Counter[str] = Counter(str1)
    cc.subtract(str2)
    return all(value == 0 for value in cc.values()) 

def covers_alphabet(sentence: str) -> bool:
    """this function will return true if a sentence includes one instance of
    character in the alphabet or false if not so much"""
    s1: Set[Any] = set("abcdefghijklmnopqrstuvwxyz")  #create a set for the alphabet
    s2: Set[Any] = set(sentence.lower()) #create a set for the sentence in lower case
    return s1 <= s2 #check to see if s1 a subset of s2 returns T/F 

def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """ This function creates a summary with distinct sites and sorted names of distinct people
    and their internet search history"""
    dd:DefaultDict[str, list] = defaultdict(list)
    # run through tuples in a list as done on slide 13 lecture 07
    for first, second in weblogs: 
        #check if employee name is already a "value" - in the list, in the defaultdictionary
        if first not in dd[second]:
            # at the same time we're adding to the default dict key, add to the default dict value, list
            dd[second].append(first)
            #sort the DD's list of values (second column in the dictionary)
            dd[second].sort()    
    # sort the key's in the dictionary
    result = sorted(dd.items())
    return result    
 
""" weblogs: List[Tuple[str, str]] = [
     ('Nanda', 'google.com'), ('Maha', 'google.com'), 
     ('Fei', 'python.org'), ('Maha', 'google.com'), 
     ('Fei', 'python.org'), ('Nanda', 'python.org'), 
     ('Fei', 'dzone.com'), ('Nanda', 'google.com'), 
     ('Maha', 'google.com'), ]

summary: List[Tuple[str, List[str]]] = [
     ('dzone.com', ['Fei']), 
     ('google.com', ['Maha', 'Nanda']), 
     ('python.org', ['Fei', 'Nanda']), ]

self.assertEqual(web_analyzer(weblogs), summary)
 """    

