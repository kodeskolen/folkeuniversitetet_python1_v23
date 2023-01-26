#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hva er det største kvadrattallet mindre enn 1000?
Kvadrattall : n^2 = n*n
1*1 = 1
2*2 = 4
3*3 = 9
4*4 = 16
"""

n = 0

while n*n < 1000:
    print(f"{n}*{n} = {n*n}")
    n = n + 1