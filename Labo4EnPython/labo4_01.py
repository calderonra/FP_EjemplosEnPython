#Realizar un programa en python que devuelva el promedio de 3 números enteros.
print("Ingrese los numeros de los cuales quiere sacar el promedio: ")


a=int(input())
b=int(input())
c=int(input())

promedio=a+b+c

promedio=promedio/3

if promedio<6:
    print("El promedio es menor a 6")
    
elif promedio>6:
    print("el promedio es mayor a 6")
    
elif promedio==6:
    print("el promedio es igual a 6")
    