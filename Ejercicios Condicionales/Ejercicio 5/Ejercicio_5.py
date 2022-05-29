def numero(numero):
    if numero >3.5 and numero<=7.8:
        m=f"El numero {numero} esta dentro del rango"
    else:
        m=f"{numero} no esta dentro del rango"
    return m
print(numero(5.7))
print(numero(1.5))
