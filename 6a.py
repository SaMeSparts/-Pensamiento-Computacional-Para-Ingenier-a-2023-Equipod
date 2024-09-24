def crear_lista(tamaño):
    lista=[]    
    while tamaño !=0:
        valor=int(input("valor: "))
        lista.append(valor)
        tamaño=tamaño-1 
        return lista   

def inicializa_lista(lista,valor):
    i = 0
    for n in lista:
        lista[1]=valor
        i +=1
    return lista

def inverti(tamaño):
    while tamaño !=0:
        lista.insert(0,valor)
        tamaño =-1
        return lista



opcion=int(input("opcion: "))            
if opcion == 1:
    tamaño=int(input(""))
    lista=crear_lista(tamaño)
    print(lista)
elif opcion ==2:
    tamaño=int(input("tamaño: "))
    lista=crear_lista(tamaño)
    valor=int(input("valor: "))
    inicializa_lista(tamaño,valor)
elif opcion ==3:
    2

elif opcion ==4:
    tamaño=int(input("tamaño: "))
    lista=crear_lista(tamaño)
    valor=int(input("valor: "))
    inverti(tamaño)
    print(lista)

elif opcion ==5:
    2
else:
    print("del 1 al 5")
