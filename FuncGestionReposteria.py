# dulce / sabor / tamaño / decoración / cantidad
reposteria = {
    'C001': ['Cupcake','vainilla','chico','frosting limón'],
    'C002': ['Cupcake','chocolate','chico','frosting vainilla'],
    'M001': ['Muffin','arandano','mediano','arandanos'],
    'M002': ['Muffin','vainilla','mediano','chispas chocolate'],
    'M003': ['Muffin','vainilla','mediano','frambuesas'],
    'T001': ['Torta','frambuesa','grande','frutas',],
    'T002': ['Torta','naranja','grande','coco rallado'],
    'G001': ['Galleta','manjar','chico','azúcar glass'],
    'B001': ['Brownie','chocolate','mediano','nueces'],
    'A001': ['Alfajor','manjar','chico','chocolate blanco']
}
# precio / cantidad
inventario = {
    'C001': [2390,20],
    'C002': [2390,20],
    'M001': [1990,25],
    'M002': [1990,25],
    'M003': [1990,20],
    'T001': [25990,4],
    'T002': [25990,5],
    'G001': [1490,50],
    'B001': [1790,40],
    'A001': [1690,40]
}

def validarNum(tipo, txtIn, txtError, txtExcep, vMin=None, vMax=None):
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
            print(txtExcep) 
    return num

def validarCodigo(codigoVal):
    tieneLetra = any(c.isalpha() for c in codigoVal)
    tieneNro = any(c.isdigit() for c in codigoVal)
    sinEspacios = ' ' not in codigoVal
    return len(codigoVal) == 4 and tieneLetra and tieneNro and sinEspacios

def verProductos():
    for clave,valor in reposteria.items():
        print('------------------------')
        print(f'{valor[0].upper()}~~')
        print('Código:',clave)
        print('Sabor:',valor[1])
        print('Tamaño:',valor[2])
        print('Decoración:',valor[3])
        print('Precio',inventario[clave][0])

def buscarxTipo():
    contador = 0
    totalDulces = 0
    dulce = input('Ingrese el producto que está buscando: ').strip().lower()
    for clave, valor in reposteria.items():
        if dulce.lower() == valor[0].lower():
            contador += 1
            totalDulces += inventario[clave][1]
    if contador != 0:
        print(f'Hay {contador} tipos de {dulce.capitalize()}')
        for clave, valor in reposteria.items():
            if dulce.lower() == valor[0].lower():
                print('------------------------')
                print(f'{valor[0].upper()}~~')
                print('Sabor:',valor[1])
                print('Tamaño:',valor[2])
                print('Decoración:',valor[3])
                print('Precio',inventario[clave][0])
                print('Stock:',inventario[clave][1])
    if totalDulces != 0:
        print(f'Hay {totalDulces} de {dulce}(s) en total.')
    else:
        print(f'No tenemos {dulce} aún.')    

def buscarxSabor():
    encontrado = False
    sabor = input('¿Qué tipo de sabor busca?: ').strip().lower()
    for lista in reposteria.values():
        if sabor.lower() == lista[1]:
            print('DULCE: ~~',lista) 
            encontrado = True     
    if not encontrado:
        print('No tenemos nada con ese sabor ):')     

def rangoxPrecio():
    encontrado = False
    pMin = validarNum(int,'Ingrese un precio (mínimo): ','Precio debe ser mayor a CERO','Precio debe ser un número',0)
    pMax = validarNum(int,'Ingrese un precio (máximo): ','Precio debe ser mayor' +str(pMin),'Precio debe ser un número',pMin)          
    for clave, valor in inventario.items():
        if valor[0] >= pMin and valor[0] <= pMax:
            print(f'VALOR: ${valor[0]} - {reposteria[clave]}')
            encontrado = True
    if not encontrado:
        print('No tenemos nada con ese precio ):')  

def mostrarxTamaño():
    encontrado = False
    tamaño = input('Ingrese qué tamaño busca\nGrande\nMediano\nChico\n-->: ').strip().lower()
    for lista in reposteria.values():
        if tamaño.lower() == lista[2]:
            print('DULCE: ~~',lista) 
            encontrado = True     
    if not encontrado:
        print('No tenemos nada con ese tamaño ):')                    

def productoMasCaro():
    precioAlto = max([valor[0] for valor in inventario.values()])

    for clave, valor in inventario.items(): 
        if valor[0] == precioAlto:  
            dulce = reposteria[clave]    
            print(f'DULCE: {dulce[0]}')
            print(f'Sabor: {dulce[1]}')
            print(f'PRECIO: ${precioAlto}')

def actualizar():
    op = validarNum(int,'1. Actualizar Precio\n2. Actualizar Stock\n-->','Opción No Existe','Opción es un número',1,2)
    while True:
        codigo = input('Ingrese el código del producto: ').upper()
        if codigo in inventario:
            break
        else:
            print('No hay productos con ese código ):')
    if op == 1:
        newPrecio = validarNum(int,'Ingrese un nuevo precio: $','Precio debe ser mayor a CERO','Precio es un número',1)
        inventario[codigo][0] = newPrecio
    else:
        newStock = validarNum(int,'Ingrese un nuevo stock: ','Cantidad no puede ser menor a CERO','Stock es un número',0)
        inventario[codigo][1] = newStock

def agregarDulce():
    while True:
        codigo = input('Ingrese el codigo del producto que desea agregar (Ej.Y006): ').upper()
        if validarCodigo(codigo):
            if codigo in reposteria:
                print('Ese código ya se encuentra')
            else:
                break
        else:
            print('Código No Válido')

    tipo = input('Tipo de dulce (Ej. Cupcake, Muffin, etc): ').strip().capitalize()
    sabor = input('Sabor principal: ').strip().lower()
    tamaño = input('Tamaño (chico/mediano/grande): ')
    decoracion = input('Decoración: ').strip().lower()
    stock = int(input('Ingrese el stock del producto: '))
    precio = int(input('Precio del producto: $'))

    reposteria[codigo] = [tipo,sabor,tamaño,decoracion]
    inventario[codigo] = [precio,stock]

    print(f'Producto: ~~{codigo.upper()} - {reposteria[codigo]}~~ agregado con éxito.')

def eliminarDulce():
    codigo = input('Ingrese el código del producto que desea eliminar: ').upper()
    if codigo in inventario:
        del reposteria[codigo]
        print('Dulce eliminado.')

def comprar():
    totalCompra = 0
    totalProducto = 0
    carrito = []
    while True:
        for clave,valor in reposteria.items():
            print('------------------------')
            print(f'{valor[0].upper()}~~')
            print('Código:',clave)
            print('Sabor:',valor[1])
            print('Tamaño:',valor[2])
            print('Decoración:',valor[3])
            print('Precio',inventario[clave][0])

        codigo = input('¿Qué dulce desea llevar?: ').upper()
        if codigo in reposteria:
            if inventario[codigo][1] > 0:
                totalProducto += 1
                totalCompra += inventario[codigo][0]   
                inventario[codigo][1] -= 1
                carrito.append([reposteria[codigo][0], reposteria[codigo][1], inventario[codigo][0]])
                print(f'Dulce {reposteria[codigo][0]} agregado. Stock restante: {inventario[codigo][1]}')
                seguir = validarNum(int,'Desea seguir comprando?\n1. Si\n2. No\n-->','Opción no existe', 'Opción es un número,1,2')
                if seguir != 1:
                    print('  ~~~~~ RESUMEN COMPRA ~~~~~')
                    print(f'Total: {totalCompra}') 
                    print(f'Productos: {totalProducto}')
                    for i, producto in enumerate(carrito, 1):
                        print(f'{i}. {producto[0]} de sabor {producto[1]} - Precio: ${producto[2]}')
                    break
            else:
                print(f'No queda stock del producto {reposteria[codigo][0]} ):')    
        else:
            print('No tenemos de ese dulce aún ):')

def menu():
    while True:
        print("""
        ***** MENÚ REPOSTERÍA *****
        1. Ver productos
        2. Buscar producto por tipo (Cupcake, Muffin, etc.)     
        3. Buscar por sabor principal
        4. Buscar por rango de precio    
        5. Mostrar total de productos por tamaño
        6. Ver producto más caro
        7. Actualizar precio o stock
        8. Agregar nuevo producto
        9. Eliminar producto
        10. Comprar       
        11. Salir
""")
        op = validarNum(int,'Elija una opción: ','Opción no existe.','Opción es un número.',1,11)
        if op == 1:
            print('~~ VER PRODUCTOS ~~') 
            verProductos()  
        elif op == 2:
            print('~~ BUSCAR PRODUCTO ~~')  
            buscarxTipo()
        elif op == 3:
            print('~~ SABOR ~~')
            buscarxSabor()
        elif op == 4:
            print('~~ PRECIO ~~')
            rangoxPrecio()
        elif op == 5:
            print('~~ TAMAÑO ~~')
            mostrarxTamaño()
        elif op == 6:
            print('~~ VER PRODUCTO + CARO ~~')
            productoMasCaro()
        elif op == 7:
            print('~~ ACTUALIZAR PRECIO/STOCK ~~')
            actualizar()
        elif op == 8:
            print('~~ AGREGAR NUEVO PRODUCTO ~~')
            agregarDulce()
        elif op == 9:
            print('~~ ELIMINAR PRODUCTO ~~') 
            eliminarDulce()
        elif op == 10:
            print('Entrando al menú para comprar ~~')    
            comprar()
        elif op == 11:
            print('Saliendo ~~')    
            print('Hasta Luego!!')                          

menu()



