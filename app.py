import funciones

Lista = []
while True:
    print("-----Menu-----")
    print("1. Registrar consumo")
    print("2. Listar consumo ")
    print("3. Imprimir consumo ")
    print("4. Buscar consumo ID")
    print("5. SALIR ")
    opcion = input("Ingrese opcion ")
    if opcion == "1":
        funciones.registrar_consumo(Lista)
    elif opcion == "2":
        funciones.listar_consumo(Lista)
    elif opcion == "3":
        consumo = input("")
        funciones.imprimir_consumo(Lista, consumo)
    elif opcion == "4":
        funciones.buscar_consumo_id(Lista)
    elif opcion == "5":
        break
    else:
        print("Opcion incorrecta")
