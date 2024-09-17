def pi(n):
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

opcion = int(input())     
if(opcion == 1):
    base  = float(input())
    exponente = float(input())
    print(exp(base, exponente))
elif(opcion == 2):
    n  = input()
    print(pi(n))
elif(opcion == 3):
    v = ""
    pokemon(v)
