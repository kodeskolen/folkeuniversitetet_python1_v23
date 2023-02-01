#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:12:11 2023

@author: johan
"""

#lese fil
møbler = []
priser = []

with open("bestillinger_møbler.txt") as infile:
    for line in infile:
        l = line.split()
        print(f"[ {' '.join(l[0:-1])} {l[-1]}],")
        
        
