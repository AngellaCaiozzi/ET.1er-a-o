diccContactos = {}

def crearContacto(contContacto):
    try:    
        while True:
            nombre = input('Nombre del Contacto (máx 50 caracteres): ').strip()
            if len(nombre) > 50:
                print('Nombre demasiado largo.')
            elif nombre in diccContactos:
                print('El contacto ya existe. Por favor ingrese uno nuevo.')    
            else:
                break   

        while True:
            telefono = []
            num = input('Ingrese el número telefónico: +569 ').strip()
            if not num.isdigit() or len(num) != 8:
                print('Número inválido.')
            elif num in diccContactos:
                print('El contacto ya existe. Por favor ingrese uno nuevo.')      
            else:
                telefono.append(num)
                break   

        while True:
            direccion = input('Direccion (máx 50 caracteres): ').strip()
            if len(direccion) > 60:
                print('Dirección demasiado larga.')
            else:
                break             

        while True:
            correo = input('Correo electrónico: ').strip()
            if len(correo) > 50 :
                print('Correo muy largo.') 
            elif '@' not in correo or '.' not in correo:
                print('El correo debe contener @ y .')
            else:
                break    
                
        diccContactos[nombre] = {
            'telefono': telefono,
            'direccion': direccion,
            'correo': correo}
        contContacto += 1
        print(f'Contacto No {contContacto} creado con éxito.')
        return contContacto 
    except Exception as e: 
        print('Error al crear el contacto.', e)      

def modificarContacto():
    while True:
        nombre = input('Ingrese el nombre del contacto que desea modificar: ').strip()
        if nombre not in diccContactos:
            print('Contacto no encontrado.')
            break
        else:
            print('Modificando contacto', nombre)
            crearContacto(diccContactos)
            break

def eliminarContacto(contContacto):
    while True:
        nombre = input('Ingrese el nombre del contacto que desea eliminar: ').strip()
        if nombre not in diccContactos:
            print('Nombre no encontrado')
        else:
            del diccContactos[nombre]
            contContacto -= 1
            print('Contacto eliminado.')
            return contContacto               

def listarContactos(contContacto):
    if not diccContactos:
        print('No hay contactos registrados.')
    for nombre, datos in diccContactos.items():
        print(f'{nombre}')
        print(f'Teléfono: {", ".join(datos["telefono"])}')
        print(f'Dirección: {datos["direccion"]}')
        print(f'Correo: {datos["correo"]}')
        print('*' * 40)
    print(f'Total contactos creados: {contContacto}.')    

def buscarContacto():
    print('\n*****SUBMENÚ DE BÚSQUEDA*****')
    print('1. Por Nombre.')
    print('2. Por Teléfono.')
    print('3. Por Dirección.')
    print('4. Por Correo.')
    op = input('Elija una opción: ')

    while True:
        try:
            if op == '1':
                nombre = input('Nombre: ').strip()
                if nombre in diccContactos:
                    print(f'{nombre}: {diccContactos[nombre]}') 
                    return
                else:
                    print('Nombre no encontrado.')
            elif op == '2':
                num = input('Ingrese el número telefónico: +569 ').strip()
                for nombre, datos in diccContactos.items():
                    if num in datos['telefono']:
                        print(f'{nombre}: {datos}')
                        return
                print('Teléfono No Encontrado.')        
            elif op == '3':
                direccion = input('Dirección: ').strip().lower()
                for nombre, datos in diccContactos.items():
                    if direccion in datos['direccion'].lower():
                        print(f'{nombre}: {datos}')  
                        return
                print('Dirección No Encontrada.')            
            elif op == '4':
                correo = input('Correo: ').strip().lower()
                for nombre, datos in diccContactos.items():
                    if correo in datos['correo'].lower():
                        print(f'{nombre}: {datos}')
                        return
                print('Correo No Encontrado.')
            else:
                print('Opción No Válida.')   
        except: 
            print('Valores ingresados NO VÁLIDOS.')  

def menu():
    contContacto = 0
    while True:
        try:
            print('\n***** MENÚ GESTIÓN DE CONTACTOS *****')
            print('1. Crear Contacto.')
            print('2. Modificar Contacto.')
            print('3. Eliminar Contacto.')
            print('4. Listar Información Contacto.')
            print('5. Buscar Contacto.')
            print('6. Salir.')
            op = input('Seleccione una opción: ')
            if op == '1':
                contContacto = crearContacto(contContacto)
            elif op == '2':
                modificarContacto()
            elif op == '3':
                contContacto = eliminarContacto(contContacto)
            elif op == '4':
                contContacto = listarContactos(contContacto)
            elif op == '5':
                buscarContacto()  
            elif op == '6':
                print('Saliendo del Sistema...')
                break
            else:
                print('Opción No Válida.')              
        except Exception as e: 
            print('Valores ingresados NO VÁLIDOS.', e) 

menu()        