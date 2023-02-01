#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vi gjentar renteberegning-programmet fra sist gang,
men denne gangen bruker vi en for-løkke i stedet
og vi lurer på hva beløpet er på kontoen etter 10 år?
"""

saldo = 10000
renten = 4.5

for år in range(10):
    saldo = saldo + renten/100*saldo
    print(f"Etter {år+1} så er det {saldo:.2f} kroner på konto.")

