

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        aux = a
        a = b
        b = aux + b
    return a

for c in range(0, 3):
    print(fibonacci(c))