def factura(estrato:int,metro:int):
    estrato1={"CargoFijo":2500,"MetroCons":2200,"BasAlcan":5500}
    estrato2={"CargoFijo":2800,"MetroCons":2350,"BasAlcan":6200}
    estrato3={"CargoFijo":3000,"MetroCons":2600,"BasAlcan":7400}
    estrato4={"CargoFijo":3300,"MetroCons":3400,"BasAlcan":8600}
    estrato5={"CargoFijo":3700,"MetroCons":3900,"BasAlcan":9700}
    estrato6={"CargoFijo":4400,"MetroCons":4800,"BasAlcan":11000}
    if estrato == 1:
        precio_factura= estrato1["CargoFijo"]+(estrato1["MetroCons"]*metro)+estrato1["CargoFijo"]
    elif estrato == 2:
        precio_factura = estrato2["CargoFijo"]+(estrato2["MetroCons"]*metro)+estrato2["CargoFijo"]
    elif estrato == 3:
        precio_factura = estrato3["CargoFijo"]+(estrato3["MetroCons"]*metro)+estrato3["CargoFijo"]
    elif estrato == 4:
        precio_factura = estrato4["CargoFijo"]+(estrato4["MetroCons"]*metro)+estrato4["CargoFijo"]
    elif estrato == 5:
        precio_factura = estrato5["CargoFijo"]+(estrato5["MetroCons"])*metro+estrato5["CargoFijo"]
    elif estrato == 6:
        precio_factura = estrato6["CargoFijo"]+(estrato6["MetroCons"]*metro)+estrato6["CargoFijo"]
    return precio_factura
print(factura(6,20))
