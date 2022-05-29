def nota_def(nota:float):
    if nota <3.0:
        m=f"Insuficiente"
    elif nota >=3.0 and nota <=3.5:
        m=f"Aceptable"
    elif nota >=3.5 and nota <=4.0:
        m=f"Sobresaliente"
    elif nota >=4.0 and nota <=5.0:
        m=f"Excelente"
    else:
        m=f"Dato invalido"
    return m
print(nota_def(2.9))
print(nota_def(3.8))
print(nota_def(4.6))
