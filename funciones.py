def existencias():
    provincias = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
    juguetes = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]
    existencias = []

    for provincia in provincias:
        inventario = []
        print("ingresando provincias: ")
        for jueguete in juguetes:
            cantidad = int(input("Cual es la cantidad de juguetes: "))
            inventario.append(cantidad)
        existencias.append(inventario)
    return existencias, provincias, juguetes


def total_juguetes_deposito(existencias):
    totales = []
    for inventario in existencias:
        total = sum(inventario)
        totales.append(total)
    return totales


def juguetes_para_reponer (existencias, juguetes):
    juguetes_reponer = []
    for inventario in existencias:
        reponer = [juguetes[i] for i in range(len(inventario)) if inventario[i] < 500]
        juguetes_reponer.append(reponer)
    return juguetes_reponer





def maximo_juguete_por_tipo (existencias, provincias):
    juguetes_maximos = []
    for i in range(len(existencias[0])):
        max_cantidad = 0
        provicia_max = ""
        for j in range(len(existencias)):
            if existencias[j][i] > max_cantidad:
                max_cantidad = existencias[j][i]
                provincia_max = provincias[j]
        juguetes_maximos.append((provicia_max, max_cantidad))
    return juguetes_maximos




def deposito_mayor_recaudacion(existencias, precios):
    recaudaciones = []
    for inventario in existencias:
        recaudacion = sum([inventario[i] * precios[i] for i in range(len(inventario))])
        recaudaciones.append(recaudacion)
    return recaudaciones





def depositos_con_mas_de_50000_juguetes(existencias, provincias):
    depositos = []
    for i in range(len(existencias)):
        total_juguetes = sum(existencias[i])
        if total_juguetes > 50000:
            depositos.append(provincias[1])
        return depositos
    




def porcentaje_juguetes_por_tipo(existencias):
    total_juguetes = sum([sum(inventario) for inventario in existencias])
    porcentajes = []

    for i in range(len(existencias[0])):
        total_tipo = sum([inventario[i] for inventario in existencias])
        porcentaje = (total_tipo / total_juguetes) * 100
        porcentajes.append(porcentaje)
    
    return porcentajes






def recaudaciones(recaudaciones, provincias):
    for i in range(1, len(recaudaciones)):
        llave = recaudaciones[i]
        llave_provincias = provincias[i]
        j = i - 1
        while j >= 0 and recaudaciones[j] < llave:
            recaudaciones[j + 1] = recaudaciones[j]
            provincias[j + 1] = provincias[j]
            j -= 1
        recaudaciones[j + 1] = llave
        provincias[j + 1] = llave_provincias
    return recaudaciones, provincias



