def par_impar(numero):
    par = numero % 2
    if par == 0:
        mensaje=f"El numero {numero} es par"
    else:
        mensaje=f"El numero {numero} es impar"
    return mensaje
print(par_impar(18))
print(par_impar(15))
