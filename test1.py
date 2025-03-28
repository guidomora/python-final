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

def verificacionFechas(ingreso, egreso):
    fechasIngreso = [int(i) for i in ingreso.split('/')]
    fechasEgreso = [int(i) for i in egreso.split('/')]
    if (fechasEgreso[2], fechasEgreso[1], fechasEgreso[0]) < (fechasIngreso[2], fechasIngreso[1], fechasIngreso[0]):
        return False
    return True

def ingresoHuespedes():
    try:
        archivoHuespedes = open('huespedes.txt', 'wt', encoding='UTF8')
        while True:
            dni = input('Ingrese dni, -1 para terminar: ')
            if dni == '-1':
                break
            archivoHuespedes.write(dni + ',')
            nombreApellido = input('nombre y apellido: ')
            if len(nombreApellido) > 4:
                archivoHuespedes.write(nombreApellido + ',')
            fechaIngreso = input('fecha de ingreso dd/mm/aaaa: ')
            fechaEgreso = input('fecha de Egreso dd/mm/aaaa: ')
            while verificacionFechas(fechaIngreso, fechaEgreso) == False:
                print('Fechas incorrectas')
                fechaIngreso = input('fecha de ingreso dd/mm/aaaa: ')
                fechaEgreso = input('fecha de Egreso dd/mm/aaaa: ')
            archivoHuespedes.write(fechaIngreso + ',')
            archivoHuespedes.write(fechaEgreso + ',')
            cantidad = input('cantidad: ')
            if cantidad.isdigit() and cantidad != '0':
                archivoHuespedes.write(cantidad + '\n')
    except FileNotFoundError:
        print('No se encontro el archivo')
    
ingresoHuespedes()