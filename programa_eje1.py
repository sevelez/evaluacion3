from os import system
import csv
def obtener_fichero_asistencia():
    lista = []
    with open(r"C:\Users\cetecom\Downloads\asistencia_alumnos.csv", "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
                curso     = linea[0]
                rut       = linea[1]
                nombre    = linea[2]+" "+linea[3]+" "+linea[4]
                Asistencia_actual = round(int(linea[5])/(int(linea[5])+int(linea[6])+int(linea[7]))*100,1)
                lista.append({
                                 'curso':curso,
                                 'rut':rut,
                                 'nombre': nombre,
                                 'Asistencia_actual': Asistencia_actual,
                            })    
            else:
                pos = 1
    return lista






def menu_principal():
    opciones = {
        '1': ('Consultar Asistencia Actual  por  alumno', consulta_asistencia_rut),
        '2': ('Visualizar alumnos Asistencia Actual < 70%.', visualiza_asistencia_70),
        '3': ('Visualizar número alumnos con “Asistencia Actual”  < 70%  de un curso', visualiza_asistencia_curso),
        '4': ('Generar archivo alumnos con “Asistencia Actual”  < 70%  de un curso', accion3),
        '5': ('Salir', salir)
    }

    generar_menu(opciones, '5')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def consulta_asistencia_rut():
    rut_ingreso = input("Ingrese el rut del alumno ")
    lista_alumnos = obtener_fichero_asistencia()
    valido = False
    for alumnos in lista_alumnos:
        if rut_ingreso == alumnos['rut']:
           print(f"El alumno {alumnos['nombre']} tiene una asistencia actual de {alumnos['Asistencia_actual']}")
           input()
           valido = True
    if valido == False:
          print(f"El rut {rut_ingreso} no corresponde a un alumno")
          input()


def visualiza_asistencia_70():
    lista_alumnos = obtener_fichero_asistencia()
    for alumnos in lista_alumnos:
        if alumnos['Asistencia_actual'] < 70:
           print(f"{alumnos['curso']} alumno {alumnos['nombre']} Asistencia {alumnos['Asistencia_actual']}")
    input()


def visualiza_asistencia_curso():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


menu_principal()
