nombres_epicos_geekdom = [
["Naofumi", "Filo", "Raphtalia"], 
["Rand Al'thor", "Perrin Arabaya", "Mathrim Cauldron", "Egwene Al'vere", "Nynaieve Al'mere"], 
["Lithany of Fury", "Macragge's Honour", "Vengeful Spirit", "Harbinger of Doom", "Chronicle of Ashes"],
["Cloud Strife", "Sephiroth", "Vincent Valentine", "Zack Fair", "Aerith Gainsborough", "Tifa Lockhart", "Barret Wallace", "Yuffie Kisaragi"],
["Cormyr", "WestGate", "Suzeil", "Menzoberranzan", "Waterdeep"],
["Atlas", "Dectective Comics", "Dark Horse", "Image"],
]

def crear_matriz(e, i):
    matriz=[]
    ext = e
    lista = []
    while ext > 0:
        lista = []
        inte = i
        while inte > 0:
            a = int(input())
            lista.append(a)
            inte = inte - 1
        matriz.append(lista)
        ext = ext - 1
    return(matriz)

def suma_diagonal(matriz):
    for i in matriz:
        x = matriz.index(i)
        acum = acum + matriz[x][x]
    return(acum)

def suma_diagonal_inversa(matriz):
    while i >= 0:
        acum = acum + matriz[b][i]
        i = i - 1
        b = b + 1
    return(acum)

def encuentra_grupo(nombre):
    global nombres_epicos_geekdom
    for i in nombres_epicos_geekdom:
        for x in i:
            if nombre == x:
                return(i)
    else:
        return("el nombre no es epico")

opcion = int(input())
if opcion == 1:
    interior = int(input())
    exterior = int(input())
    print(crear_matriz(exterior, interior))
elif opcion == 2:
    interior = int(input())
    exterior = int(input())
    if exterior != interior:
        print(False)
    else:
        matriz = crear_matriz(exterior, interior)
        print(suma_diagonal(matriz))
elif opcion == 3:
    interior = int(input())
    exterior = int(input())
    if exterior != interior:
        print(False)
    else:
        matriz = crear_matriz(exterior, interior)
        print(suma_diagonal_inversa(matriz))
elif opcion == 4:
    nombre = input()
    print(encuentra_grupo(nombre))
