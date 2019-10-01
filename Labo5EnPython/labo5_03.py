print("La media de cuantos numeros quiere calcular: ")
x=int(input())
acum=0
for i in range(0,x):
    print("Ingrese numero a calcular: ")
    y=int(input())
    acum=acum+y
media=acum/x
print("la media es: "+str(media))
