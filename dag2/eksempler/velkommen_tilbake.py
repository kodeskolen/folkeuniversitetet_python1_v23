# -*- coding: utf-8 -*-

print("Velkommen tilbake!")
print("Programmering med Python - Dag 2")

# Bruker datetime pakken til å skrive dagens dato.
from datetime import date
print(date.today())

print()

print("Tema for i dag er")
print("- Repetisjon")
print("- Lister")
print("- Mer om løkker")
print("- Tekstbehandling")

#Variabler:
    # type: int, float, str, bool
    # innholdet, verdien
    # navn 

a = 5
print(type(a))


b = int(15.4)

print(b)
print(type(b))

if a > b:
    print("Variabelen a er større enn b")
elif a < b:
    print("Variabelen b er større enn a")
else:
    print("a og b er helt like!")


