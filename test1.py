# TP7 ej 1

# def creacionArchivo(nombre):
#     archivo = open(f'{nombre}.txt', 'a', encoding='UTF8')
#     return archivo

# try:
#     archivoMain = open('nombres.txt', 'r', encoding='UTF8')
#     for linea in archivoMain:
#         nombreEntero = linea.split()
#         apellido = nombreEntero[1]
#         if apellido[-3:] == 'ian':
#             archivo = creacionArchivo('armenia')
#             archivo.write(apellido + '\n')
#             archivo.close()
#         if apellido[-3:] == 'ini':
#             archivo = creacionArchivo('italia')
#             archivo.write(apellido + '\n')
#             archivo.close()
#         if apellido[-2:] == 'ez':
#             archivo = creacionArchivo('espana')
#             archivo.write(apellido + '\n')
#             archivo.close()
#         if apellido[-3:] != 'ian' and apellido[-3:] != 'ini' and apellido[-2:] != 'ez':
#             archivo = creacionArchivo('descartar')
#             archivo.write(apellido + '\n')
#             archivo.close()
#     archivoMain.close()
# except Exception:
#     print('error')
# -------------------------------------------

# TP7 ej 2
# import math
# def splitFile(quantity):
#     try:
#         file = open('datos.txt', 'r', encoding='UTF8')
#         lineCount = 0
#         line2Count = 0
#         fileVersion = 1
#         for line1 in file:
#            lineCount += 1
#         splitsLines = math.ceil(lineCount / quantity)
#         file.seek(0)
#         lines = []
#         fileVersion = 1
#         line2Count = 0
#         for line in file:
#             lines.append(line)
#             line2Count += 1
#             if line2Count == splitsLines:
#                 newFile = open(f'datos_{fileVersion}.txt', 'w', encoding='UTF8')
#                 newFile.writelines(lines)
#                 newFile.close()
#                 fileVersion += 1
#                 lines.clear()
#                 line2Count = 0
#         if lines:
#             newFile = open(f'datos_{fileVersion}.txt', 'w', encoding='UTF8')
#             newFile.writelines(lines)
#             newFile.close()
#         file.close()
#     except FileNotFoundError:
#         print('Error')

# splitFile(4)

# -------------------------------------------

# TP7 ej 3

# def grabarRangoAlturas():
#     archivoAlturas = open('alturasTotales.txt', 'a', encoding='UTF8')
#     while True:
#         ingresarDeporte = input('Ingresar nombre del Deporte: ')
#         if ingresarDeporte == '-1':
#             break
#         archivoAlturas.write(ingresarDeporte + '\n')
#         while True:
#             ingresarAltura = int(input('ingresar la altura del atleta: '))
#             if ingresarAltura == -1:
#                 break
#             archivoAlturas.write(str(ingresarAltura)+ '\n')
#     archivoAlturas.close()
    
# # grabarRangoAlturas()
# def grabarPromedio():
#     archivoAlturas = open('alturasTotales.txt', 'r', encoding='UTF8')
#     archivoPromedios = open('alturasPromedio.txt', 'a', encoding='UTF8')
#     alturas = []
#     alturasPromPorDeporte = []
#     for line in archivoAlturas:
#         linea = line.strip()
#         if len(linea) > 3:
#             if alturas:
#                 promedio = sum(alturas) // len(alturas)
#                 alturasPromPorDeporte.append(promedio)
#                 archivoPromedios.write(str(promedio)+ '\n')
#                 alturas.clear()
#             archivoPromedios.write(linea + '\n')

#         if len(linea) == 3:
#             lineaParseada = int(linea)
#             alturas.append(lineaParseada)
#     if alturas:
#         promedio = sum(alturas) // len(alturas)
#         alturasPromPorDeporte.append(promedio)
#         archivoPromedios.write(str(promedio) + '\n')
#     archivoAlturas.close()
#     archivoPromedios.close()
#     alturaPromedioTotal = sum(alturasPromPorDeporte) // len(alturasPromPorDeporte) 
#     print(alturaPromedioTotal, '------------')
#     return alturaPromedioTotal

# def mostrarMasAltos(totalProm):
#     archivoPromediosRead = open('alturasPromedio.txt', 'r', encoding='UTF8')
#     masAltos = []
#     for line in archivoPromediosRead:
#         linea = line.strip()
#         if len(linea) == 3 and linea.isdigit():
#             numberLinea = int(linea)
#             if numberLinea >= totalProm:
#                 masAltos.append(numberLinea)
#     print(masAltos)
    
# totalProm = grabarPromedio()
# mostrarMasAltos(totalProm)
# ---------------------------------------------------------------


# TP7 ej 4

# try:
#     program = open('programa.txt', 'r', encoding='UTF8')
#     newProgram = open('nuevo_programa.txt', 'w', encoding='UTF8')
#     DocString = False

#     for line in program:
#         line = line.strip()
#         if line.startswith('"""') or line.startswith("'''"):
#             DocString = not DocString
#             continue
#         if DocString:
#             continue
#         if line.startswith('#'):
#             continue
#         newProgram.write(line + '\n')
#     program.close()
#     newProgram.close()
# except FileNotFoundError:
#     print('error')

# ---------------------------------------------------------------

# TP 7 ej 6

# def verificacionFechas(ingreso, egreso):
#     fechasIngreso = [int(i) for i in ingreso.split('/')]
#     fechasEgreso = [int(i) for i in egreso.split('/')]
#     if (fechasEgreso[2], fechasEgreso[1], fechasEgreso[0]) < (fechasIngreso[2], fechasIngreso[1], fechasIngreso[0]):
#         return False
#     return True

# def ingresoHuespedes():
#     try:
#         archivoHuespedes = open('huespedes.txt', 'wt', encoding='UTF8')
#         while True:
#             dni = input('Ingrese dni, -1 para terminar: ')
#             if dni == '-1':
#                 break
#             archivoHuespedes.write(dni + ',')
#             nombreApellido = input('nombre y apellido: ')
#             if len(nombreApellido) > 4:
#                 archivoHuespedes.write(nombreApellido + ',')
#             fechaIngreso = input('fecha de ingreso dd/mm/aaaa: ')
#             fechaEgreso = input('fecha de Egreso dd/mm/aaaa: ')
#             while verificacionFechas(fechaIngreso, fechaEgreso) == False:
#                 print('Fechas incorrectas')
#                 fechaIngreso = input('fecha de ingreso dd/mm/aaaa: ')
#                 fechaEgreso = input('fecha de Egreso dd/mm/aaaa: ')
#             archivoHuespedes.write(fechaIngreso + ',')
#             archivoHuespedes.write(fechaEgreso + ',')
#             cantidad = input('cantidad: ')
#             if cantidad.isdigit() and cantidad != '0':
#                 archivoHuespedes.write(cantidad)
#             archivoHuespedes.write('\n')
#         archivoHuespedes.close()
#     except FileNotFoundError:
#         print('No se encontro el archivo')
    
# # ingresoHuespedes()

# def pisoHabitacion(habitacion):
#     piso = 0
#     if habitacion <= 6:
#         piso = 1
#     if habitacion > 6 and habitacion <= 12:
#         piso = 2
#     if habitacion > 12 and habitacion <= 18:
#         piso = 3
#     if habitacion > 18 and habitacion <= 24 :
#         piso= 4
#     if habitacion > 24 and habitacion <= 30:
#         piso = 5
#     if habitacion > 30 and habitacion <= 36:
#         piso = 6
#     if habitacion > 36 and habitacion <= 42:
#         piso = 7
#     if habitacion > 42 and habitacion <= 48:
#         piso = 8
#     if habitacion > 48 and habitacion <= 54 :
#         piso= 9
#     if habitacion > 54 and habitacion <= 60:
#         piso = 10
#     return piso

# def pisoConMasHab(pisosHab):
#     pisos = list(pisosHab.keys())
#     habitaciones = list(pisosHab.values())
#     habsMax = max(habitaciones)
#     print(habsMax)
#     indice = habitaciones.index(habsMax)
#     pisoConMasHabs = pisos[indice]
#     print('piso con mas habitaciones: ', pisoConMasHabs)
#     return pisoConMasHabs
         
    
# def habsVacias(pisosHabs):
#     habitaciones = 60
#     ocupadas = list(pisosHabs.values())
#     vacias = habitaciones - sum(ocupadas)
#     print('habitaciones vacias: ', vacias)

        
# import random
# def asignacionHabitaciones():
#     habitaciones = []
#     cantidades = []
#     huespededes = []
#     pisos = {1:0, 2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
#     archivoHuespedes = open('huespedes.txt', 'r', encoding='UTF8')
#     archivoHabtaciones = open('habitaciones.txt', 'wt', encoding='UTF8')
#     for huesped in archivoHuespedes:
#         huesped = huesped.split(',')
#         huespededes.append(huesped[0])
#         cantidades.append(huesped[4])
#         habitacion = random.randint(1,60)
#         while habitacion in habitaciones:
#             habitacion = random.randint(1,60)
#         habitaciones.append(habitacion)
#         piso = pisoHabitacion(habitacion)
#         pisos[piso] +=1
#         hola = f'huesped dni: {huesped[0]}, piso: {piso}, habitacion: {habitacion}' + '\n'
#         archivoHabtaciones.write(hola)
#     pisoConMasHab(pisos)
#     habsVacias(pisos)
#     archivoHuespedes.close()
#     archivoHabtaciones.close()
        
# asignacionHabitaciones()

# ---------------------------------------
# Ej Discord

# def mailValido(mail):
#     if '@' in mail:
#         mail = mail.split('@')
#         if len(mail) > 1:
#             if mail[0].isalpha() :
#                 if '.com' in mail[1]:
#                     return True
#     print('no valido')
#     return False

# def detectarPais(paises):
#     listaPaises = {}
#     for pais in paises:
#         if pais not in listaPaises:
#             listaPaises[pais] = 1
#         else:
#             listaPaises[pais] += 1
#     print(listaPaises)
#     return listaPaises
        

# try:
#     mailFile = open('email.txt', 'r', encoding='UTF8')
#     paises = []
#     cantidades = {}
#     for mail in mailFile:
#         mail = mail.strip()
#         if mailValido(mail):
#             if mail[-3:] != 'com':
#                 paises.append(mail[-2:])
#             if mail[-4:] == '.com':
#                 paises.append('us')
#     print(paises)
#     detectarPais(paises)    
# except FileNotFoundError:
#     print('error')

# ----------------------------------------------

def ordenVotos(votos):
    votosOrdenados = dict(sorted(votos.items(), key=lambda x: x[1], reverse=True))
    listaPartidos = list(votosOrdenados.keys())
    listaVotos = list(votosOrdenados.values())
    votosTotales = sum(listaVotos)
    for i in range(len(listaPartidos)):
        barras = '*' * int(round((listaVotos[i] / votosTotales) * 100, 2) // 2)
        print(f'{listaPartidos[i]:<25} {barras} {round((listaVotos[i] / votosTotales) * 100, 2)}%')
    return listaPartidos
        
def listaPartidoGanador(archivo, partidoGanador):
    votosLista = {}
    for partido in archivo:
        partido = partido.strip().split(';')
        if partido[0] == partidoGanador:
            lista = f'Lista {partido[1]}'
            if lista not in votosLista:
                votosLista[f'Lista {partido[1]}'] = 1
            else:
                votosLista[f'Lista {partido[1]}'] += 1
    ordenVotos(votosLista)
            
            
def principal():
    try:
        archivoResultados = open('resultados.txt', 'r', encoding='UTF8')
        votos = {}
        for voto in archivoResultados:
            voto = voto.strip().split(';')
            if voto[0] not in votos:
                votos[voto[0]] = 1
            else:
                votos[voto[0]] += 1
        ordenPartidos = ordenVotos(votos)
        archivoResultados.seek(0)
        print('--------------------------------------')
        print(f'Partido ganador: {ordenPartidos[0]}')
        listaPartidoGanador(archivoResultados, ordenPartidos[0])
        archivoResultados.close()
    except FileNotFoundError:
        print('No se encontro el archivo')

principal()