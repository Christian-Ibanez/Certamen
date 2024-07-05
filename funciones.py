import random, csv
import equipos

def codigo_consumo():
    random.randint(100000, 999999)
    return random.randint(100000, 999999)

def registrar_consumo(lista):
    viernes = 0
    sabado = 0
    domingo = 0

    codigo = codigo_consumo()
    nombre = input("Ingrese nombre: ")
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad > 0:
                break
            else:
                print("Hay un fallo en la edad ")
                continue
        except:
            print("Algo falló en el registro ")
            registrar_consumo(lista)       
    equipo = input("Ingrese equipo ")

    while True:
        try:
            con_viernes = int(input("Ingrese consumo viernes: "))
            viernes += con_viernes
            con_sabado = int(input("Ingrese consumo sabado: "))
            sabado += con_sabado
            con_domingo = int(input("Ingrese consumo domingo: "))
            domingo += con_domingo
        except:
            print("Algo falló en el registro ")
            registrar_consumo(lista)
        try:
            if viernes + sabado + domingo >= 3:
                print("registro completo ")
                break
            else:
                print("Debe consumir al menos 3 tazas")
                continue
        except:
            print("Algo falló en el registro ")
            registrar_consumo(lista)
    lista.append([codigo, nombre, edad, equipo, viernes, sabado, domingo])

def listar_consumo(lista):
    print("ID consumo\tJugador\tEdad\tEquipo\tViernes\tSabado\tDomingo")
    for player in lista:
        print(f"{player[0]}\t{player[1]}\t{player[2]}\t{player[3]}\t{player[4]}\t{player[5]}")

def imprimir_consumo(lista, consumo):
    with open("hoja.csv", "w", newline= "") as hoja_consumo:
        
        hoja_consumo("ID consumo\tJugador\tEdad\tEquipo\tViernes\tSabado\tDomingo")
    


def buscar_consumo_id(lista):
    id = False
    jugador = int(input("Ingrese ID de jugador: "))
    for player in lista:
            print(f"{player[0]}\t{player[1]}\t{player[2]}\t{player[3]}\t{player[4]}\t{player[5]}")
            id = True