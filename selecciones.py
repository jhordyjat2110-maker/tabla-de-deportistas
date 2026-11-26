'''
La Universidad Unpamplona desea llevar un registro de 5 estudiantes deportistas vinculados a las selecciones de la universidad.
Existen 3 selecciones:
_____________________________________
| Código     | Nombre                |
|------------|-----------------------|
|  1015      |      Futbol           |
|  1030      |    Baloncesto         |
|  1045      |    Ciclismo           |
 ----------------------------------   
De cada estudiante se conoce:
> Nombre.
> Cedula.
> Sexo (1 Hombre, 2 Mujer).
> Edad.
> Código de la Selección a la que pertenece.

Realice las siguientes funciones:

>> Información de la matriz.

>> Determine el porcentaje de Hombres y mujeres.

>> El nombre del estudiante más joven a que selección pertenece

>> Determine el número de deportistas por selección.


'''

# ----------------------------------
def porsex(d, n):
    homb = 0

    for i in range(n):
        if d[i][2] == 1:
            homb += 1

    homb = (homb / n) * 100
    muj = 100 - homb

    print('''
╔════════════════════════════════════╗
║ PORCENTAJE POR SEXO                ║
╚════════════════════════════════════╝''')
    print(f"Mujeres: {muj:.2f}%")
    print(f"Hombres: {homb:.2f}%")



# ----------------------------------
def masjov(d, n):
    # Buscar edad mínima
    jov = d[0][3]  # asumiendo que la persona de menor esta en la primera posicion

    for i in range(1, n):
        if d[i][3] < jov:
            jov = d[i][3]

    print('''
╔════════════════════════════════════════════════════════════╗
║ DEPORTISTA(S) MÁS JOVEN(ES)                                ║
╚════════════════════════════════════════════════════════════╝
╔══════════════╦══════╦═══════════════════════╗
║ Selección    ║ Edad ║ Nombre                ║
╠══════════════╬══════╬═══════════════════════╣''')

    # Mostrar todos los que tengan la edad mínima
    for i in range(n):
        if d[i][3] == jov:

            if d[i][4] == 1015:
                seleccion = "Fútbol"
            elif d[i][4] == 1030:
                seleccion = "Baloncesto"
            else:
                seleccion = "Ciclismo"

            print(f"║ {seleccion:12} ║ {jov:4} ║ {d[i][0]:21} ║")

    print('╚══════════════╩══════╩═══════════════════════╝')

#----------------------------

def estxsel(d, n):
    futbol = 0
    baloncesto = 0
    ciclismo = 0

    for i in range(n):
        if d[i][4] == 1015:
            futbol += 1
        elif d[i][4] == 1030:
            baloncesto += 1
        else:
            ciclismo += 1

    print("\nESTUDIANTES POR SELECCIÓN")
    print("Fútbol:", futbol)
    print("Baloncesto:", baloncesto)
    print("Ciclismo:", ciclismo)


# ----------------------------------
def imprimir(d, n):
    print('''
╔════════════════════════════════════════════════════════════════════════════════╗
║          MATRIZ DE ESTUDIANTES                                                 ║
╚════════════════════════════════════════════════════════════════════════════════╝
╔════╦══════════════════════╦════════════╦══════════╦════════╦═══════════════════╗
║ No ║ Nombre               ║ Cédula     ║ Sexo     ║ Edad   ║ Selección         ║
╠════╬══════════════════════╬════════════╬══════════╬════════╬═══════════════════╣''')

    for i in range(n):

        if d[i][2] == 1:
            sexo = "Hombre" 
        else: 
            sexo = "Mujer"

        if d[i][4] == 1015:
            seleccion = "Fútbol"
        elif d[i][4] == 1030:
            seleccion = "Baloncesto"
        else:
            seleccion = "Ciclismo"

        print(f"║ {i+1:2} ║ {d[i][0]:20} ║ {d[i][1]:10} ║ {sexo:8} ║ {d[i][3]:6} ║ {seleccion:17} ║")

    print("╚════╩══════════════════════╩════════════╩══════════╩════════╩═══════════════════╝")


# ----------------------------------
def principal():

    # MATRIZ DEFINIDA DIRECTAMENTE
    datos = [
        ["JUAN PEREZ", 12345, 1, 20, 1015],
        ["ANA LOPEZ", 54321, 2, 19, 1030],
        ["CARLOS RUIZ",67890, 1, 21, 1045],
        ["ANA TORRES",98765, 2, 23, 1015],
        ["LUIS DIAZ", 11111, 1, 22, 1030]
    ]

    n = 5
    imprimir(datos, n)
    porsex(datos, n)
    masjov(datos,  n)
    estxsel(datos, n)

# ----------------------------------
if __name__ == "__main__":
    principal()