def exp(a, b):
    count = 1
    if b == 0:
        c = 1
    else:
        c = a
        while count < b:
            c = c * a
            count = count + 1
    return(c)


# pide opción y dependiendo de la opción llama una función diferente
opcion = int(input("opción "))     
if(opcion == 1):
    base  = float(input("base "))
    exponente = float(input("exp "))
    print(exp(base, exponente))
elif(opcion == 2):
    n  = input("num ")
    print(pi(n))
elif(opcion == 3):
    pok  = input("pokemon ")
    pokemon(pok)
