# marca / modelo / pantalla / RAM / GB / SO /color
celulares = {
    'A123': ['Samsung', 'Galaxy A54', 6.5, 6, 128, 'Android', 'Negro'],
    'B456': ['Apple', 'iPhone 13', 6.1, 4, 128, 'iOS', 'Blanco'],
    'C789': ['Xiaomi', 'Redmi Note 12', 6.6, 8, 256, 'Android', 'Azul'],
    'D321': ['Motorola', 'Edge 30', 6.7, 8, 128, 'Android', 'Gris'],
    'E654': ['Apple', 'iPhone 14 Pro', 6.1, 6, 256, 'iOS', 'Negro espacial'],
    'F987': ['Samsung', 'Galaxy S23', 6.1, 8, 256, 'Android', 'Lavanda'],
    'G111': ['Realme', 'GT Neo 3', 6.7, 12, 256, 'Android', 'Celeste'],
    'H222': ['Huawei', 'P50 Pro', 6.6, 8, 256, 'Android', 'Oro']
}
# precio / stock
inventario = {
    'A123': [279990, 10],
    'B456': [699990, 5],
    'C789': [229990, 12],
    'D321': [349990, 8],
    'E654': [1099990, 3],
    'F987': [899990, 6],
    'G111': [499990, 7],
    'H222': [649990, 4]
}

def validarNro(tipo, txtIn, txtError, txtExep, vMin=None, vMax=None):
    while True:
        try:
            num = tipo(input(txtIn))
            if vMin != None and vMax != None:
                if num >= vMin and num <= vMax:
                    break
                else:
                    print(txtError)
            elif vMin != None:
                if vMin <= num:
                    break  
                else:
                    print(txtError)
            elif vMax != None:
                if vMax >= num:
                    break
                else:
                    print(txtError)
            else:
                break
        except:
            print(txtExep) 
    return num                           

def CelularesXMarca():
    contador = 0
    totalCelulares = 0
    marca = input('Ingrese la marca del celular: ').strip().lower()
    for clave, valor in celulares.items():
        if marca == valor[0].lower():
            contador += 1
            totalCelulares += inventario[clave][1]
    if contador != 0:
        print(f'Hay {contador} modelos de celulares de la marca {marca.upper()}.') 
        for clave, valor in celulares.items():
            if marca == valor[0].lower():
                print(f'Modelo: {clave} - {celulares[clave]}')
    if totalCelulares != 0:
        print(f'Hay {totalCelulares} celulares en Stock de {marca.upper()}.')      
    else:
        print(f'No tenemos disponibles celulares de la marca {marca.upper()}.')  

def CelularesXPrecio():
    encontrado = False
    pMin = validarNro(int,'Ingrese un precio (mínimo): ','Debe ser mayor a CERO','Precio debe ser un número',0)
    pMax = validarNro(int,'Ingrese un precio (máximo): ','Precio debe ser MAYOR' +str(pMin),'Precio debe ser un número',pMin)
    for clave, valor in inventario.items():
        if valor[0] >= pMin and valor[0] <= pMax:
            print(f'Valor Celular: ${valor[0]} - {celulares[clave]}')
            encontrado = True
    if not encontrado:
        print('No se encontraron celulares en el rango de precio.')   

def CelularesXPantalla():
    encontrado = False
    pulgada = validarNro(float,'Ingresa tamaño pantalla: ','Tamaño fuera de rango [6.1 - 6.7]','Tamaño es un número',6.1,6.7)
    for lista in celulares.values():
        if pulgada == lista[2]:
            print(lista)
            encontrado = True
    if not encontrado:
        print('No se encontraron celulares con ese tamaño de pantalla.')

def CelularesXRAM():
    encontrado = False
    ram = validarNro(int,'Ingresa tamaño RAM: ','Tamaño fuera de rango [4 - 12]','Tamaño es un número',4,12)
    for lista in celulares.values():
        if ram == lista[3]:
            print(lista)
            encontrado = True
    if not encontrado:
        print('No se encontraron celulares con ese tamaño de RAM.')

def CelularesXSO():
    contador = 0
    sisOp = input('Ingrese un Sistema Operativo: ').strip()
    for lista in celulares.values():
        if sisOp.lower() == lista[-2].lower():
            contador += 1
    if contador != 0:
        print(f'Hay {contador} celulares con {sisOp.upper()}')  
        for lista in celulares.values():
            if sisOp.lower() == lista[-2].lower():
                print(lista)
    else:
        print(f'No tenemos disponibles modelo(s) con {sisOp.upper()}.')       

def actualizar():
    opcion = validarNro(int,'1.- Actualizar Precio.\n2.- Actualizar Cantidad\n--> ','Opción NO existe.','Opción es un número',1,2)                            
    while True:
        codigo = input('Ingrese Código: ').upper()
        if codigo in inventario:
            break
        else:
            print('Código de producto NO Existe!!')

    if opcion == 1:
        newPrecio = validarNro(int,'Ingrese Nuevo Precio: ','Precio debe ser mayor a CERO.','Precio es un número',1)        
        inventario[codigo][0] = newPrecio
        print('Precio Actualizado.')
    else:
        newCant = validarNro(int,'Ingrese Nueva Cantidad: ','Cantidad No puede ser Negativo','Cantidad es un número',0)
        inventario[codigo][1] = newCant
        print('Cantidad Actualizada.')            

def menu():
    while True:
        print("""\n***** MENÚ CELULARES *****
              1. Mostrar Celulares por Marca.
              2. Buscar Celulares por Precio.
              3. Buscar Celulares por Pantalla.
              4. Buscar Celulares por Cantidad de RAM.
              5. Mostrar Celulares por Sistema Operativo.
              6. Actualizar Precio y/o Stock.
              7. Salir
              """)
        op = input('Ingrese una opción: ')
        if op == '1':  
            print('Celulares x Marca.')
            CelularesXMarca()
        elif op == '2':
            print('Celulares x Precio.')
            CelularesXPrecio()
        elif op == '3':
            print('Celulares x Pantalla.')
            CelularesXPantalla()    
        elif op == '4':
            print('Celulares x RAM.')
            CelularesXRAM()
        elif op == '5':
            print('Celulares x Sistema Operativo.')
            CelularesXSO()
        elif op == '6':
            print('Actualizar Precio/Stock')
            actualizar()
        elif op == '7':
            print('Programa Terminado!!!')    
        else:
            print('Error: Opción NO Existe!!!')

try:
    menu()
except Exception as e:
    print('Valor No Válido.', e)               