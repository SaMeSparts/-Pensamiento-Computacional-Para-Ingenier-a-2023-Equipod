lista=[]
while 1==1:
    def crear_lista(tamaño):
        while tamaño != 0:
            valor=int(input("valor: "))
            lista.append(valor)
            tamaño =tamaño - 1 
        return lista   

    def inicializa_lista(lista,valor):
        for i in lista:
            lista[i] = valor
        return lista

    def cuenta_impares(lista):
        impares = 0
        for elem in lista:
            if elem % 2 != 0:
                impares = impares +1
        return impares



    def inverti(temp):
        i=0
        max=len(lista[-1])
        while i < max/2:
            temp=lista[i]
            lista=lista[max-i]
            lista[max-i]=lista[i]
            i=i-i

    def mayor_valor(lista):
        lista.sort()
        print(lista[-1])

    opcion=int(input("opcion: "))            
    if opcion == 1:
        tamaño1=int(input("tamaño: "))
        lista=crear_lista(tamaño1)
        print(lista)
    elif opcion ==2:
        tamaño2=int(input("tamaño: "))
        lista2=crear_lista(tamaño2)
        valor2=int(input("valor: "))
        inicializa_lista(tamaño2,valor2)
        print(lista2)
    elif opcion ==3:
        tamaño3=int(input("tamaño: "))
        lista3=crear_lista(tamaño3)
        cuenta_impares(lista)

    elif opcion ==4:
        tamaño4=int(input("tamaño: "))
        lista4=crear_lista(tamaño4)
        print(inverti(tamaño4))

    elif opcion ==5:
        tamaño5=int(input("tamaño: "))
        lista5=crear_lista(tamaño5)
        mayor_valor(lista5)
    else:
        print("del 1 al 5")
