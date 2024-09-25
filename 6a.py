def captura_lista(tam):
    lista = []
    while tam > 0:
        var = int(input())
        lista.append(var)
        tam = tam - 1
    return(lista)

def inicializa_lista(lista, valor):
    for i in lista:
        lista[lista.index(i)] = valor
    return(lista)

def cuenta_impares(lista):
    imp = 0
    for i in lista:
        if i%2 != 0:
            imp = imp + 1
    return(imp)

def invierte_lista(lista):
    i = len(lista)/2
    a = 0
    b = -1
    while i > 0:
        temp = lista[a]
        lista[a] = lista[b]
        lista[b] = temp
        a = a+1
        b = b-1
        i = i-1
    return(lista)

def mayor(lista):
    lista.sort()
    return(lista[-1])

opcion = int(input())
if opcion == 1:
    tam = int(input())
    print(captura_lista(tam))
elif opcion ==2:
    tam = int(input())
    lista = captura_lista(tam)
    valor = int(input())
    print(inicializa_lista(lista, valor))
elif opcion == 3:
    tam = int(input())
    lista = captura_lista(tam)
    print(cuenta_impares(lista))
elif opcion == 4:
    tam = int(input())
    lista = captura_lista(tam)
    print(invierte_lista(lista))
elif opcion == 5:
    tam = int(input())
    lista = captura_lista(tam)
    print(mayor(lista))
else:
    print("entrada no valida")
