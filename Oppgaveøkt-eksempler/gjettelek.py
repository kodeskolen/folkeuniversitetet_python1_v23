"""Et program hvor vi gjetter på et tall mellom 1 og 100."""

from random import randint

fasit = randint(1, 100)

gjett = int(input("Gjett et tall mellom 1 og 100: "))

forsøk = 1

while gjett != fasit:  
    if gjett > fasit: 
        print("Du gjettet for høyt.")  
    elif gjett < fasit: 
        print("Du gjettet for lavt.")
    gjett = int(input("Gjett en gang til: ")) 
    forsøk = forsøk + 1 
print("Du gjettet riktig!")
print(f"Du brukte {forsøk} forsøk.")
