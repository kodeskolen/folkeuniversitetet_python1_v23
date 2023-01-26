#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sjekke om et tall er positivt eller negativt.
"""

tall = float(input("Gi meg et tall: "))


if tall > 0:
    print("Tallet er positivt!")
elif tall < 0:
    print("Tallet er negativt!")
else:
    print("Tallet er akkurat null!")