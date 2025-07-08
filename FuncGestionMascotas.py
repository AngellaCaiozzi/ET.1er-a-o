diccMascota = {}
animales = {
    'perro': 0, 
    'gato': 0, 
    'conejo': 0, 
    'hamster': 0, 
    'tortuga': 0
    }

def registrarMascota(animales):
    while True:
        mascota = input('Ingrese nombre de la mascota: ').strip()
        if len(mascota) > 30:
            print('Nombre demasiado largo.')
        if all(palabra.isalpha() for palabra in mascota.split()):
            break
        else:
            print('Debe contener solo letras por favor.')

    while True:
        print("""
            ANIMALES PERMITIDOS:
            -PERRO
            -GATO
            -CONEJO
            -LORO
            -HAMSTER
            -CERDO
            -TORTUGA""")
        tipo = input('Ingrese el tipo de animal: ').strip().lower()
        if tipo not in animales:
            print('Por favor ingrese un animal permitido.')
        else:
            animales[tipo] += 1
            break

    while True:
        edad = input('Ingrese la edad de su mascota: ')
        if not edad.isdigit() or len(edad) > 3:
            print('Ingrese una edad válida por favor.')  
        else:
            break  

    while True:
        dueño = input('Ingrese nombre del dueño: ').strip().lower()
        if dueño not in diccMascota:
            if all(palabra.isalpha() for palabra in dueño.split()) and (3 < len(dueño) < 50):
                break 
            else:
                print('Ingrese un nombre válido por favor.')    

    while True:
        rut = input('Ingrese el RUT del dueño(sin puntos ni guion): ').strip() 
        if len(rut) != 9 or not rut.isdigit():
            print('RUT inválido.') 
        else:
            break                

    historial = []
    print('\n***** Nota Salud Mascota *****')
    for i in range(3):
        while True:
            try:
                nota = float(input(f'Ingrese la nota de la visita No {i + 1}: '))
                if 1.0 <= nota <= 7.0:
                    historial.append(nota)
                    break
                else:
                    print('Ingrese una nota entre 1.0 - 7.0.')
            except:
                print('Por favor ingrese un número válido.')            

    diccMascota[mascota] = {
        'tipo': tipo,
        'edad': edad,
        'dueño': dueño,
        'rut': rut,
        'historial': historial} 
    print('Mascota registrada con éxito!')  
    return    
     
def listarMascotas():
    if not diccMascota:
        print('No hay mascotas registradas.')
        return
    dueñoBuscado = input('Ingrese el nombre del dueño: ').strip()   
    encontrados = False
    for mascota, datos in diccMascota.items():
        if datos['dueño'].lower() == dueñoBuscado.lower():
            encontrados = True
            print('\n***** DATOS MASCOTA *****')
            print(f"MASCOTA: {mascota}")
            print(f"TIPO MASCOTA: {datos['tipo']}")
            print(f"EDAD MASCOTA: {datos['edad']}")
            print(f"DUEÑO: {datos['dueño']}")
            print(f"RUT: {datos['rut']}")
            print(f"HISTORIAL: {datos['historial']}")
            print('*' * 40)   
    if not encontrados:
        print('No se encontraron mascotas para ese dueño.')

def tipoMascota(animales):
    if not diccMascota:
        print('No hay mascotas registradas.')
        return 
    print('\n***** TIPOS DE ANIMALES REGISTRADOS *****')
    total = 0    
    for tipo, cantidad in animales.items():
        print(f'{tipo.capitalize()}: {cantidad}')
        total += cantidad   
    print(f'Total de mascotas registradas: {total}')  
      
def calcularPromedio():
    while True:
        mascota = input('Ingrese el nombre de la mascota: ').strip()
        if mascota not in diccMascota:
            print('Por favor ingrese a la mascota en el registro.')
            return
        else:
            break
    
    historial = diccMascota[mascota]['historial']    
    promedio = historial[0] * 0.3
    promedio += historial[1] * 0.3
    promedio += historial[2] * 0.4 
    print(f'El promedio de salud de la mascota {mascota} es: {promedio:.2f}')     

def mejorMascota():
    if len(diccMascota) < 2:
        print('Deben haber al menos dos mascotas.') 
        return
    mejorPromedio = 0
    mejorMascota = ''
    for mascota, datos in diccMascota.items(): 
        historial = datos['historial']
        promedio = historial[0] * 0.3
        promedio += historial[1] * 0.3
        promedio += historial[2] * 0.4  
        if promedio > mejorPromedio:
            mejorPromedio = promedio
            mejorMascota = mascota
    print(f'El mejor estudiante es {mejorMascota} con promedio {mejorPromedio:.2f}')

def eliminarMascota():
    mascota = input('Ingrese el nombre de la mascota: ').strip() 
    if mascota not in diccMascota:
        print('La mascota no estáá ingresada aún.')
        return
    else:
        del diccMascota[mascota]
        print('Mascota eliminada.')
             
def menu():
    while True:
        try:
            print('\n***** MENÚ MASCOTAS *****')
            print('1. Registra Nueva Mascota.')
            print('2. Buscar Mascota por Dueño.')
            print('3. Ver Mascotas por Tipo.')
            print('4. Calcular Promedio de Salud por Mascota.')
            print('5. Mostrar Mascota Mejor Evaluada.')
            print('6. Eliminar Mascota del Sistema.')
            print('7. Salir.')
            op = input('Seleccione una opción: ')
            if op == '1':
                registrarMascota(animales)
            elif op == '2':
                listarMascotas()
            elif op == '3':
                tipoMascota(animales)
            elif op == '4':
                calcularPromedio()
            elif op == '5':
                mejorMascota()
            elif op == '6':
                eliminarMascota()
            elif op == '7':
                print('Saliendo del Sistema...')
                break
            else:
                print('Opción No Válida.')              
        except: 
            print('Valores ingresados NO VÁLIDOS.', e) 

try: 
    menu()   
except Exception as e:
    print('Ocurrió un error: ', e)    