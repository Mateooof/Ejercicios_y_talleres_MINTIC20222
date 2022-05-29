def num(numero):
    if numero>3.5 and numero<=9.5:
        m=f"{numero} esta en el rango de (3.5, 9.5]"
    elif numero>=23.4 and numero<=45.3:
        m=f"{numero} esta en el rango de [23.4, 45.3]"
    else:
        m=f"El numero no esta en ningun rango "
    return m
print(num(24.0))
