#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dette programmet skal regne volumet av en fotball.
V = 4/3 pi r^3
"""
from math import pi

print(pi)

radius = 12 #cm

volum = 4/3*pi*radius**3

volum = volum/1000

print(f"Volumet av en fotball er {volum:.3f} L")