#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 08:44:08 2023

I dette eksemplet skal laste inn "testfil.txt" med open()

@author: m
"""

fil = open("testfil.txt", mode = "r") # read leser inn testfil.txt 

innhold = fil.read() # les alt som er i filen.

print(innhold)

fil.close() # alltid god skikk å lukke filene sine!