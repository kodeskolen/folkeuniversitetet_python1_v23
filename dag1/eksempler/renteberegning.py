#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hvor mye øker beløpet på en konto med gitt en rente på 2.8%
Hvor mange år tar det før beløpet har doblet seg?
"""

saldo = 10000 # beløp på konto i kr
rente = 4.5 # rente i prosent
år = 0 #år

while saldo < 15000:
    saldo = saldo + saldo*rente/100
    år = år + 1
    print(f"Etter {år} år er det {saldo:.2f} kr på kontoen.")