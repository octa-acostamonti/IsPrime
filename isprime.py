def IsPrime(numero):
    es_primo = True
    for i in range(2,numero):
        if (numero % i == 0):
            es_primo = False
            break

    if (es_primo):
        print("El numero es primo")
    else:
        print("No es primo")


