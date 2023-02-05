"""Et program som holder oversikt over bursdager"""""

personer = ['Anne', 'Birger', 'Ola', 'Vilde', 'Lise']
bursdager = [[10,2,1978], [3, 11, 1985], [6, 2, 1954], [20, 3, 1992], [1, 6, 1985]]

for person in personer:
    print(person)
    
for dato in bursdager:
    print(dato)
    
for dato in bursdager:
    print(f'{dato[0]}/{dato[1]}/{dato[2]}')
    

for indeks in range(len(personer)):
    dato = bursdager[indeks][0]
    måned = bursdager[indeks][1]
    år = bursdager[indeks][2]
    print(f'{personer[indeks]}: {bursdager[indeks][0]}/{bursdager[indeks][1]}/{bursdager[indeks][2]}')
  
for indeks in range(len(personer)):
    navn = personer[indeks]
    dato = bursdager[indeks][0]
    måned = bursdager[indeks][1]
    år = bursdager[indeks][2]  
    print(f'{navn}: {dato}/{måned}/{år}')
    
personer_sortert = []
bursdager_sortert = []

for i_måned in range(1, 12+1):
    for i_dato in range(1, 31+1):
        for i_bursdag in range(len(bursdager)): 
            dd = bursdager[i_bursdag][0]
            mm = bursdager[i_bursdag][1]
            if i_måned == mm and i_dato == dd:
                bursdager_sortert.append(bursdager[i_bursdag])
                personer_sortert.append(personer[i_bursdag])
 
for indeks in range(len(personer_sortert)):
    dato = bursdager_sortert[indeks][0]
    måned = bursdager_sortert[indeks][1]   
    print(f'{personer_sortert[indeks]}: {dato}/{måned}')
