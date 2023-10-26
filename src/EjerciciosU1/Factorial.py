def factorial(num:int):
    total=1
    while num>1:
        total*=num
        num-=1
    return total

def factorialStr(num:int):
    total=1
    res=str(num)+"! => "+str(num)
    while num>0:
        res+=str(num)
        if(num!=1):
            res+=" x "
        total*=num
        num-=1
    res+=" = "+total
    return res

numero=input("Introduce un número: ")

print("El factorial de 4! es "+str(factorial(4)))
print(factorialStr(numero))