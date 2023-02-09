#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:17:11 2023

I  dette eksemplet skal vi se hvordan vi kan lage figurer/plots utfra lister.

@author: m
"""

# for å kunne plotte, må vi importere plotte-funksjonene fra pylab-biblioteket
from pylab import plot, scatter, show, xlabel, ylabel


x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 9, 16, 25, 36]

plot(x, y)
show() # må fortelle python (hvis man ikke bruker spyder): VIS MEG PLOTTET

# vi kan lage ulike plot, for eksempel prikk-plot (scatter) 

kaffepauser = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
produktivitet = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0] 

scatter(kaffepauser, produktivitet) 
xlabel("Antall kaffepauser") 
ylabel("Produktivitet")
show()