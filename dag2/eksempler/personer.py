#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Introduksjon til lister i Python. Min første liste!
"""

#En ordnet liste med ulike elementer i en bestemt rekkefølge
#indekser :   0         1        2      3        4       5
#eller     :  -6       -5       -4      -3       -2      -1
personer = ["Anna", "Terje", "Jonas", "Emil", "Maja", "Silje"]

#Vi kan printe listen:
print(f"Dette er min første liste: {personer}")

#Vi kan se hvor mange elementer vi har i listen vår:
print(f"Listen min har {len(personer)} elementer")

#Vi kan "indeksere" listen vår. Det betyr at vi henter ut 
#elementet ved indeksen n.

første_person = personer[0]
andre_person = personer[1]
siste_person = personer[-1]

print(f"Første person i listen er {første_person}.")
print(f"Andre person i listen er {andre_person}.")
print(f"Siste person i listen er {siste_person}.")