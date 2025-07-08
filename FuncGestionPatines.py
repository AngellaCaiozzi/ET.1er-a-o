#marca, talla, tipo de botas, tamaño rueda,  
patines = {
'1234PT': ['Rollerblade', 38, 'bota rígida', 80, 'aluminio', 'intermedio', 'negro con rojo', 1.6, 'trasero', 'fitness'],
'4321PT': ['Powerslide', 37, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'azul marino', 1.4, 'trasero', 'fitness'],
'1111PT': ['FR Skates', 39, 'bota rígida', 90, 'aluminio', 'avanzado', 'negro mate', 1.9, 'sin freno', 'urbano'],
'1212PT': ['Oxelo', 40, 'bota blanda', 72, 'plástico', 'principiante', 'gris con verde', 1.3, 'trasero', 'fitness'],
'2121PT': ['Rollerblade', 42, 'bota rígida', 84, 'aluminio', 'intermedio', 'negro con azul', 1.7, 'intercambiable', 'urbano'],
'2222PT': ['Fila', 36, 'bota blanda', 76, 'plástico reforzado', 'principiante', 'rosa con blanco', 1.2, 'trasero', 'fitness'],
'3131PT': ['Oxelo', 41, 'bota semirrígida', 80, 'aluminio', 'intermedio', 'gris con rojo', 1.5, 'trasero', 'fitness'],
'1313PT': ['Oxelo', 40, 'bota rígida', 100, 'aluminio', 'avanzado', 'negro con dorado', 2.0, 'sin freno', 'freestyle']
}
#precio, cantidad
inventario = {
'1234PT': [89990, 10],
'4321PT': [79990, 4],
'1111PT': [139990, 1],
'1212PT': [59990, 13],
'2121PT': [49990, 22],
'2222PT': [99990, 7],
'3131PT': [119990, 4],
'1313PT': [109990, 5]
}

def validaNro(tipo, txtIn, txtError, txtExep, vMin=None, vMax=None):
    while True:
        try:
            nro = tipo(input(txtIn))
            if vMin != None and vMax != None:
                if nro >= vMin and nro <= vMax:
                    break
                else:
                    print(txtError)
            elif vMin != None:
                if vMin <= nro:
                    break
                else:
                    print(txtError)
            elif vMax != None:
                if vMax >= nro:
                    break
                else:
                    print(txtError)
            else:
                break
        except:
            print(txtExep) 
    return nro                                 

def cantidadModelosXMarca():
    contador = 0
    marca = input('Ingrese marca que desea buscar: ').strip()
    for lista in patines.values():
        if marca.lower() == lista[0].lower():
            contador += 1
    if contador != 0:
        print(f'Hay {contador} modelo(s) de la marca {marca}.')
    else:
        print(f'No tenemos disponibles modelo(s) de la marca {marca}.')  

def cantidadPatinesXMarca():
    totalPatines = 0
    marca = input('Ingrese marca que desea buscar: ').strip()
    for clave, valor in patines.items():
        if marca.lower() == valor[0].lower():
            totalPatines += inventario[clave][1]
    if totalPatines != 0:
        print(f'Hay {totalPatines} patines de la marca {marca}.')
    else:
        print(f'No tenemos disponibles patines de la marca {marca}.')            

def cantidadPatinesXTalla():
    totalPatines = 0
    talla = validaNro(int,'Ingrese talla: ','Talla Fuera de rango [21 - 55]','Error: debe ingresar un número.',21,55)
    for clave, valor in patines.items():
        if talla == valor[1]:
            totalPatines += inventario[clave][1]
    if totalPatines != 0:
        print(f'Hay {totalPatines} patines de la talla {talla}.')
    else:
        print(f'No tenemos disponible patines de la talla {talla}.')   

def buscarXRangoPrecio() :
    encontrado = False
    pMin = validaNro(int,'Ingrese precio mínimo: ','Precio debe ser Mayor a CERO','Precio es un número',0)   
    pMax = validaNro(int,'Ingrese precio máximo: ','Precio debe ser Mayor '+str(pMin),'Precio es un número',pMin)             
    for clave, valor in inventario.items():
        if valor[0] >= pMin and valor[0] <= pMax:
            print(f'Valor Patín: ${valor[0]} - {patines[clave]}')
            encontrado = True
    if not encontrado:
        print('No se encontraron patines en el rango de precio.')  

def buscarPorRueda():
    encontrado = False
    rueda = validaNro(int,'Ingresa tamaño de rueda: ','Tamaño fuera de rango [30 - 100].','Tamaño es un número',30,100)
    for lista in patines.values():
        if rueda == lista[3]:
            print(lista)
            encontrado = True
    if not encontrado:
        print('No se encontraron patines con ese diametro de rueda.')   

def actualizar():
    opcion = validaNro(int,'1.- Actualizar Precio.\n2.- Actualizar Cantidad\n--> ','Opción NO existe.','Opción es un número',1,2)                            
    while True:
        codigo = input('Ingrese Código: ').upper()
        if codigo in inventario:
            break
        else:
            print('Código de producto NO Existe!!')

    if opcion == 1:
        newPrecio = validaNro(int,'Ingrese Nuevo Precio: ','Precio debe ser mayor a CERO.','Precio es un número',1)        
        inventario[codigo][0] = newPrecio
        print('Precio Actualizado.')
    else:
        newCant = validaNro(int,'Ingrese Nueva Cantidad: ','Cantidad No puede ser Negativo','Cantidad es un número',0)
        inventario[codigo][1] = newCant
        print('Cantidad Actualizada.')

def menu():
    while True:
        print("""
        \t***MENÚ***
        1.Cantidad de modelos por marca
        2.Cantidad de patines disponibles por marca
        3.Cantidad de patines disponible por talla
        4.Búsqueda por rango de precio
        5.Búsqueda de patines por tamaño de rueda
        6.Actualizar precio y/o cantidad
        7.Salir
        """)
        op = input('Ingrese su opción: ')
        if op == '1':
            print('1.Cantidad de modelos por marca')
            cantidadModelosXMarca()
        elif op == '2':
            print('2.Cantidad de patines disponibles por marca')
            cantidadPatinesXMarca()
        elif op == '3':
            print('3.Cantidad de patines disponible por talla')
            cantidadPatinesXTalla()
        elif op == '4':
            print('4.Búsqueda por rango de precio')
            buscarXRangoPrecio()
        elif op == '5':
            print('5.Búsqueda de patines por tamaño de rueda')
            buscarPorRueda()
        elif op == '6':
            print('6.Actualizar precio y/o cantidad')
            actualizar()
        elif op == '7':
            print('Programa Terminado!!!')    
        else:
            print('Error: Opción NO Existe!!!')
               
try: 
    menu()   
except Exception as e:
    print('Ocurrió un error: ', e)                