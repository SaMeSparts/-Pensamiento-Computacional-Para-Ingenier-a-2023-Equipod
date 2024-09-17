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

def pokemon(v):
    while v != "pikachu":
        v = input()
    if v == "pika!":
        print("pika")
    elif v == "pikapika":
        print("chu")
    elif v == "pikachu":
        print("pikachu!!!")
    else:
        print("???")

def pi():
    n=float(input(""))
    num=1
    res=0
    pos=0
    while num <= n:
        if pos==1:
            res=res + 1/num
            num+=2
            pos=0
        else:
            res=res-1/num
            num+=2
            pos=1

print((res)*(4)*(-1))

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
