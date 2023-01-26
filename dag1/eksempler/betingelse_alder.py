#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program som sjekker om brukeren er gammel nok for å gå på kino.
"""

alder = int(input("Hvor gammel er du? "))

if alder >= 15:
    print("Velkommen på kino!")
elif alder >= 12:
    med_voksen = input("Har du med en voksen (ja/nei)?")
    if med_voksen == "ja":
        print("Velkommen på kino!")
    else:
        print("Du er ikke gammel nok!")
else:
    år_igjen = 15 - alder
    print(f"Du er ikke gammel nok. Kom igjen om {år_igjen} år")

