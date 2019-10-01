def Suma():
    print("Ingrese los numeros a sumar: ")
    a = int(input())
    b = int(input())
    suma = a+b
    print("La suma es: "+str(suma))
    pass


def Resta():
    print("Ingrese los numeros a restar: ")
    a = int(input())
    b = int(input())
    resta = a-b
    print("La resta es: "+str(resta))
    pass


def Multiplicacion():
    print("Ingrese los numeros a multiplicar: ")
    a = int(input())
    b = int(input())
    multi = a*b
    print("La multiplicacion es: "+str(multi))
    pass


def Division():
    print("Ingrese los numeros a dividir: ")
    a = int(input())
    b = int(input())
    div = a/b
    print("La division es: "+str(div))
    pass


def fibonacci():
    print("Posicion de fibbonacci que quiere saber")
    n = int(input())
    a = 0
    b = 1
    for i in range(0, n):
        aux = a
        a = b
        b = aux + b
    print(str(a))


def factorial():
    print("Ingree el numero del cual quiere saber el factorial")


    x = int(input())
    acum = 1
    for i in range(1, x+1):
        acum = i*acum


    print(acum)


x = 0
while x != 7:
    print("***INGRESE UNA OPCION***")
    print("1-Suma de dos numeros")
    print("2-Resta de dos numeros")
    print("3-Multiplicacion de dos numeros")
    print("4-Division de dos numeros")
    print("5-Fibbonacci ")
    print("6-Factorial de un numero")
    print("7-Salir")
    x = int(input())

    if x == 1:
        Suma()
        pass
    elif x == 2:
        Resta()
        pass
    elif x == 3:
        Multiplicacion()
        pass
    elif x == 4:
        Division()
    elif x == 5:
        fibonacci()
    elif x == 6:
        factorial()
        pass
    pass
