#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:36:55 2023

I dette skriptet skal vi laste inn huskelisten, og regne ut hvor lang tid
alle gjoremålene våre tar!

@author: m
"""

with open("huskeliste.txt", mode = "r") as fil:
    linjer = fil.readlines() 
    
#print(linjer) 

# vi vil finne ut hvor lang tid alt sammen tar! 

total_tid = 0 

for linje in linjer[1:]: 
    splittet_linje = linje.split(",") # del linjen etter tegnet ","
    tidsbruk = float(splittet_linje[1])
    
    total_tid += tidsbruk 
    
print(f"Det tar {total_tid} timer å gjøre alle gjøremålene.")