import funciones

def mostrar_menu():
    print("--- Menu de opciones---")
    print("1. existencias")
    print("2. calcular total de juguetes por deposito")
    print("3. obtener juguetes para reponer")
    print("4. Maxima cantidad de juguetes por tipo")
    print("5. deposito con mayor recaudacion")
    print("6. depositos con mas de 50.000 juguetes")
    print("7. porcentaje de juguetes por tipo")
    print("8. ordenar recaudaciones")
    print("9. terminar")




def main():
    existencias = []
    provincias = []
    juguetes = []
    precios = [50, 100, 75, 150, 10, 5]

    while True:
        mostrar_menu()
        opcion = int(input("ingrese una opcion: "))

        if opcion == 1:
            existencias, provincias, juguetes = funciones.cargar_existencias()
        elif opcion == 2:
            if existencias:
                totales = funciones.calcular_total_juguetes_por_deposito(existencias)
                for i, total in enumerate(totales):
                    print("Total en", provincias,":",  total ,"total de juguetes.")
            else:
                print("debe cargar las existencias primero.")
        elif opcion == 3:
            if existencias:
                juguetes_reponer = funciones.juguetes_para_reponer(existencias, juguetes)
                for i, reponer in enumerate(juguetes_reponer):
                    print("En", provincias, "reponer", reponer)
            else:
                print("debe cargar las existencias primero.")
        elif opcion == 4:
            if existencias:
                maximos = funciones.maximo_juguete_por_tipo(existencias, provincias)
                for i, (provincias, cantidad) in enumerate(maximos):
                    print("mayor cantidad de", juguetes, "en", provincias, ":", cantidad)
            else:
                print("Debe cargar las existencias primero.")
        elif opcion == 5:
            if existencias:
                recaudaciones = funciones.deposito_mayor_recaudacion(existencias, precios)
                for i, recaudaciones in enumerate(recaudaciones):
                    print("recaudacion en", provincias, ":", recaudaciones)
            else:
                print("debe cargar las existencias primer.")
        elif opcion == 6:
            if existencias:
                depositos = funciones.depositos_con_mas_de_50000_juguetes(existencias, provincias)
                if depositos:
                    print("depositos con mas de 50.000 juguetes:", depositos)
                else:
                    print("No hay depositos con mas de 50.000 juguetes")
            else:
                print("Debe cargar las existencias primero.")
        elif opcion == 7:
            if existencias:
                procentajes = funciones.porcentaje_juguetes_por_tipo(existencias)
                for i, procentaje in enumerate(existencias):
                    print(juguetes, ":", existencias)
            else:
                print("Debe cargar las existencias primero.")
        elif opcion == 8:
            if existencias:
                recaudaciones = funciones.deposito_mayor_recaudacion(existencias, precios)
                recaudaciones, provincias_ordenadas = funciones.recaudaciones(recaudaciones, provincias)
                for i, recaudacion in enumerate(recaudaciones):
                    print(provincias_ordenadas, "recaudacion:", recaudacion)
            else:
                print("Debe cargar las existencias primero.")
        elif opcion == 9:
            print("Terminando operaciones...")
            break

if __name__ == "__main__":
    main()

        

