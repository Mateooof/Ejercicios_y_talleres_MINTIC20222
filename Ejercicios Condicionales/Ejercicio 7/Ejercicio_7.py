def dict(caracter):
    dict={"a":"Android","i":"IOS"}
    if caracter == "a":
        m= dict["a"]
    elif caracter == "i":
        m=dict["i"]
    else:
        m="Caracter invalido"
    return m
print(dict("i"))
