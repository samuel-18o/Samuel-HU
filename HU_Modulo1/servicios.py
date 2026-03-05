# =============================================
# FUNCIONES CRUD (Create, Read, Update, Delete)
# =============================================

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario
    """
    # Creamos el diccionario que representa el producto
    producto = {
        "nombre": nombre,    # String con el nombre
        "precio": precio,    # Float con el precio
        "cantidad": cantidad # Int con la cantidad en stock
    }
    # Agregamos el producto a la lista de inventario
    inventario.append(producto)
    # Confirmamos al usuario que se agregó correctamente
    print(f"Producto '{nombre}' agregado exitosamente.")

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario de forma legible
    """
    # Verificamos si el inventario está vacío
    if not inventario:
        print("El inventario está vacío.")
        return  # Salimos de la función early
    
    # Mostramos encabezado
    print("\n--- INVENTARIO ACTUAL ---")
    # enumerate(inventario, 1) nos da (índice, producto) empezando desde 1
    for i, producto in enumerate(inventario, 1):
        # Mostramos cada producto formateado
        # :.2f formatea el precio con 2 decimales
        print(f"{i}. {producto['nombre']} - Precio: ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
    print("-------------------------")

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre y lo retorna, o None si no existe
    Búsqueda case-insensitive (no distingue mayúsculas/minúsculas)
    """
    # Convertimos el nombre buscado a minúsculas para comparación
    nombre_buscado = nombre.lower()
    
    # Recorremos cada producto del inventario
    for producto in inventario:
        # Convertimos el nombre del producto a minúsculas y comparamos
        if producto["nombre"].lower() == nombre_buscado:
            return producto  # Retornamos el producto encontrado
    
    # Si llegamos aquí, no encontramos el producto
    return None  # Retornamos None indicando que no existe

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente
    """
    # Buscamos el producto primero
    producto = buscar_producto(inventario, nombre)
    
    # Si no encontramos el producto, mostramos error
    if producto is None:
        print(f"Error: Producto '{nombre}' no encontrado.")
        return False  # Retornamos False indicando fallo
    
    # Actualizamos precio si se proporcionó nuevo valor
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    
    # Actualizamos cantidad si se proporcionó nuevo valor
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad
    
    # Confirmamos la actualización
    print(f"Producto '{nombre}' actualizado exitosamente.")
    return True  # Retornamos True indicando éxito

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario
    """
    # Buscamos el producto primero
    producto = buscar_producto(inventario, nombre)
    
    # Si no encontramos el producto, mostramos error
    if producto is None:
        print(f"Error: Producto '{nombre}' no encontrado.")
        return False  # Retornamos False indicando fallo
    
    # Removemos el producto de la lista
    inventario.remove(producto)
    # Confirmamos la eliminación
    print(f"Producto '{nombre}' eliminado exitosamente.")
    return True  # Retornamos True indicando éxito

# =============================================
# FUNCIONES DE ESTADÍSTICAS
# =============================================

def calcular_estadisticas(inventario):
    """
    Calcula métricas importantes del inventario
    Retorna un diccionario con todas las estadísticas
    """
    # Verificamos si el inventario está vacío
    if not inventario:
        print("El inventario está vacío. No hay estadísticas para calcular.")
        return None  # Retornamos None si no hay datos
    
    # Inicializamos variables para los cálculos
    unidades_totales = 0      # Suma de todas las cantidades
    valor_total = 0.0         # Suma de precio * cantidad de cada producto
    producto_mas_caro = None  # Producto con mayor precio unitario
    producto_mayor_stock = None  # Producto con mayor cantidad
    
    # Definimos una lambda function para calcular subtotal de cada producto
    # Lambda es una función anónima - equivalente a:
    # def calcular_subtotal(producto): return producto["precio"] * producto["cantidad"]
    calcular_subtotal = lambda producto: producto["precio"] * producto["cantidad"]
    
    # Recorremos cada producto para calcular las estadísticas
    for producto in inventario:
        # Calculamos el valor total de este producto (precio * cantidad)
        subtotal = calcular_subtotal(producto)
        
        # Acumulamos las unidades totales
        unidades_totales += producto["cantidad"]
        # Acumulamos el valor total del inventario
        valor_total += subtotal
        
        # Buscamos el producto más caro (por precio unitario)
        # Si es el primer producto o tiene precio mayor al actual
        if producto_mas_caro is None or producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
        
        # Buscamos el producto con mayor stock
        # Si es el primer producto o tiene cantidad mayor a la actual
        if producto_mayor_stock is None or producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto
    
    # Preparamos el diccionario de resultados
    estadisticas = {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": {
            "nombre": producto_mas_caro["nombre"],
            "precio": producto_mas_caro["precio"]
        },
        "producto_mayor_stock": {
            "nombre": producto_mayor_stock["nombre"],
            "cantidad": producto_mayor_stock["cantidad"]
        }
    }
    
    return estadisticas  # Retornamos el diccionario con estadísticas

def mostrar_estadisticas(inventario):
    """
    Muestra las estadísticas de forma legible para el usuario
    """
    # Calculamos las estadísticas primero
    estadisticas = calcular_estadisticas(inventario)
    
    # Si no hay estadísticas (inventario vacío), salimos
    if estadisticas is None:
        return
    
    # Mostramos las estadísticas formateadas
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"Unidades totales en stock: {estadisticas['unidades_totales']}")
    # :.2f formatea el float con 2 decimales
    print(f"Valor total del inventario: ${estadisticas['valor_total']:.2f}")
    print(f"Producto más caro: {estadisticas['producto_mas_caro']['nombre']} - ${estadisticas['producto_mas_caro']['precio']:.2f}")
    print(f"Producto con mayor stock: {estadisticas['producto_mayor_stock']['nombre']} - {estadisticas['producto_mayor_stock']['cantidad']} unidades")
    print("-----------------------------------")

# =============================================
# FUNCIONES DE VALIDACIÓN
# =============================================

def validar_numero_positivo(valor, tipo="número"):
    """
    Valida que un string sea un número positivo
    Retorna el número convertido o None si es inválido
    """
    try:
        # Determinamos si convertimos a int o float según el tipo
        if tipo == "entero":
            numero = int(valor)   # Convertimos a entero
        else:
            numero = float(valor) # Convertimos a float
        
        # Validamos que el número no sea negativo
        if numero < 0:
            print(f"Error: El {tipo} no puede ser negativo.")
            return None  # Retornamos None si es negativo
        
        return numero  # Retornamos el número válido
        
    except ValueError:
        # Error al convertir string a número
        print(f"Error: '{valor}' no es un {tipo} válido.")
        return None  # Retornamos None indicando error

def validar_opcion_menu(opcion, min_val=1, max_val=9):
    """
    Valida que la opción del menú sea válida
    """
    try:
        # Convertimos el string a entero
        opcion_num = int(opcion)
        # Verificamos que esté en el rango permitido
        if min_val <= opcion_num <= max_val:
            return opcion_num  # Retornamos la opción válida
        else:
            # Opción fuera de rango
            print(f"Error: La opción debe estar entre {min_val} y {max_val}.")
            return None  # Retornamos None indicando error
    except ValueError:
        # Error al convertir a número
        print(f"Error: '{opcion}' no es un número válido.")
        return None  # Retornamos None indicando error