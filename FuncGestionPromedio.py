diccEstudiantes = {}


def ingresarEstudiante():
    try:
        while True:
            nombre = input('Ingrese nombre del estudiante: ').strip()
            if len(nombre) < 5:
                print('Favor ingrear NOMBRE y APELLIDO')    
            if nombre in diccEstudiantes:
                print('Estudiante ya ingresado.')  
            else:
                break

        while True:
            rut = input('Ingrese el RUT del estudiante (sin puntos ni guion): ').strip() 
            if rut in diccEstudiantes:
                print('Estudiante ya ingresado.')
            if len(rut) != 9 or not rut.isdigit():
                print('RUT inválido.')    
            else:
                break 

        notas = []        
        for i in range(3):
            while True:
                try:
                    nota = float(input(f'Ingrese la nota No {i + 1}: '))
                    if 1.0 <= nota <= 7.0:
                        notas.append(nota)
                        break
                    else:    
                        print('Nota fuera de rango -> 1.0 - 7.0')
                except Exception as e:
                    print('Número inválido', e)       

        while True:    
            try:
                examen = float(input('Ingrese la nota del éxamen: '))
                if 1.0 <= examen <= 7.0:
                    notas.append(examen)
                    break
                else:
                    print('Nota fuera de rango -> 1.0 - 7.0')   
            except Exception as e:
                    print('Número inválido', e)

        diccEstudiantes[nombre] = {
            'RUT': rut,
            'Notas': notas} 
        print('Estudiante ingresado con éxito!')                 
    except Exception as e:
        print('Error al ingresar al estudiantes', e)      
                    
def promedioNotas():
    while True:
        nombre = input('Ingrese nombre del estudiante: ').strip()
        if nombre not in diccEstudiantes:
            print('Estudiante no está ingresado!')
        else:
            break
    notas = diccEstudiantes[nombre]['Notas']
    promedio = notas[0] * 0.15
    promedio += notas[1] * 0.15
    promedio += notas[2] * 0.2
    promedio += notas[3] * 0.5
    print(f'Promedio de notas del estudiante {nombre}: {promedio:.2f}')

def mostarInformacion():
    if not diccEstudiantes:
        print('No hay estudiantes ingresados aún.')
        return
    
    for nombre, datos in diccEstudiantes.items():
        notas = datos['Notas']
        promedio = notas[0] * 0.15
        promedio += notas[1] * 0.15
        promedio += notas[2] * 0.2
        promedio += notas[3] * 0.5

        print(f'{nombre}')
        print(f'RUT: {datos["RUT"]}')
        print(f'NOTAS: {datos["Notas"]}')
        print(f'PROMEDIO: {promedio:.2f}')
        print('*' * 40)
                   
def eliminarEstudiante():
    nombre = input('Ingrese nombre del estudiante: ').strip()
    if nombre not in diccEstudiantes:
        print('Estudiante no está ingresado!')
        return
    else:
        del diccEstudiantes[nombre]
        print('Estudiante eliminado.')
    diccEstudiantes

def mejorPromedio():
    if len(diccEstudiantes) < 2:
        print('Debe Ingresar al menos 2 estudiantes.')  
        return

    notaMasAlta = 0
    mejorEstudiante = ''

    for nombre, datos in diccEstudiantes.items(): 
        notas = datos['Notas']
        promedio = notas[0] * 0.15
        promedio += notas[1] * 0.15
        promedio += notas[2] * 0.2
        promedio += notas[3] * 0.5  
        if promedio > notaMasAlta:
            notaMasAlta = promedio
            mejorEstudiante = nombre
    print(f'El mejor estudiante es {mejorEstudiante} con promedio {notaMasAlta:.2f}')        

def menu():
    promedio = 0
    while True:
        try:
            print('\n***** PROMEDIO NOTAS *****')
            print('1. Ingresar Estudiante.')
            print('2. Promediar Notas.')
            print('3. Listar Información.')
            print('4. Eliminar Estudiante..')
            print('5. Mejor Promedio')
            print('6. Salir.')
            op = input('Seleccione una opción: ')
            if op == '1':
                ingresarEstudiante()
            elif op == '2':
                promedioNotas()
            elif op == '3':
                mostarInformacion()
            elif op == '4':
                eliminarEstudiante() 
            elif op == '5':
                mejorPromedio()    
            elif op == '6':
                print('Saliendo del Sistema...')
                break
            else:
                print('Opción No Válida.')              
        except Exception as e: 
            print('Valores ingresados NO VÁLIDOS.', e) 

menu()        
