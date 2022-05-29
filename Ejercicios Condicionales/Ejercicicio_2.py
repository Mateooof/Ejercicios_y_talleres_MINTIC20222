def nota_final(nota:float):
    if nota >=0.0 and nota <=5.0:
        if nota >=3.0:
            mensaje=f"Con una nota de {nota},ganó el curso"
        else:
            mensaje=f"Con una nota de {nota},perdió el curso"
        return mensaje
    return f"Ingrese valores entre 0.0 y 5.0"
nota=float(input("Ingrese nota: "))
print(nota_final(nota))
