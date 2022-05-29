def mayor_edad(edad:int):
    if edad >=0 and edad <=110:
        if edad<18:
            mensaje=f"Con una edad de {edad}, es menor de edad"
        else:
            mensaje=f"Con una edad de {edad}, es mayor de edad"
        return mensaje
    else:
        return f"Ingrese una edad entre 0 y 110 años"
edad=int(input("Ingrese edad: "))
print(mayor_edad(edad))
