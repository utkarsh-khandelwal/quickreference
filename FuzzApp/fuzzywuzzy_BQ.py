# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:05:37 2017

"""
# coded by a teammate. Credits to Bryce Quesnel

#https://github.com/seatgeek/fuzzywuzzy

# how to installl...
# ! pip install fuzzywuzzy
#how to install python levenshtein
# ! pip install python-Levenshtein

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import Levenshtein

import os
os.chdir('C:\\Users\\quesn\\Documents\\GitHub\\FuzzMatchSpellingBee')

import numpy as np

from pandas import Series, DataFrame

import pandas as pd

fortune_500 = pd.read_csv('fortune500.csv', squeeze=True)

sp_500 = pd.read_csv('S&P_500.csv', squeeze=True)

fort_names = fortune_500['company']
sp_names = sp_500['Name']




def fuzz_match(a_list, b_list):
    temp_dict = dict()
    for b in b_list:
        b = b.lower()
    for item in a_list:
        a = process.extractBests(item.lower(),b_list,score_cutoff=80)
        temp_dict[item] = a
    return Series(temp_dict)


#below is to test wtih only X rows
def fuzz_match_range(a_list, b_list,num):
    temp_dict = dict()
    for b in b_list:
        b = b.lower()
    for item in a_list[:num]:
        a = process.extractBests(item.lower(),b_list,score_cutoff=85)
        temp_dict[item] = a
    return Series(temp_dict)


def fuzz_match_binary(a_list, b_list):
    temp_dict = dict()
    for b in b_list:
        b = b.lower()
    for item in a_list:
        a = process.extractBests(item.lower(),b_list,score_cutoff=100)
        temp_dict[item] = len(a)
    return Series(temp_dict)


#
a = fuzz_match_binary(sp_names,fort_names)
#b = fuzz_match(sp_names,fort_names)

#b.to_csv(path='C:\Users\quesn\Google Drive\MSBA\Summer Semester\MSBA 6310 - Programming and App Development\MSBA Python Project\manually_check.csv', mode='w')    
#use the above code to write to a pre-created CSV


#sp_to_f_95 = fuzz_match(sp_names,fort_names)


#step 1: using Fuzz

#a = 'kevin!!!!?!?!!'
#aa = 'kevin'
#b = 'kelvin'
#c = 'kleven'
#d = 'kats'
#e = 'kyle'
#long1 = 'this is a test'
#long2 = 'test a is this'
#long3 = 'this is is a a test test test'

#matches basded off all characters including symbols
#print fuzz.ratio(a,aa)

#partial ratio shows matches without any symbols or syntax in the first statement
#print fuzz.partial_ratio(a,aa)

#fuzz.token_sort_ratio looks strings disregarding the order of strings
#print fuzz.token_sort_ratio(long1,long2)

#fuzz.token_set_ratio looks at strings with no regard to duplicates
#print fuzz.token_set_ratio(long1,long3)



#step 2: using process

#a_list = [a,b,c,d,e]

#extra feeds a string to search and a list and shows how well items in the list
#match up with that list
#print process.extract('cats',a_list)

##extractOne pulls the best match for a process lookup
#print process.extractOne('aactks',a_list)


#extract bests (score_cutoff drops the limit needed)
#print process.extractBests('aactks',a_list,score_cutoff=40)



#ab = 'nevikkk'
#cd = 'kevin'
#
#fuzz.ratio(ab,cd)

