# Importamos el módulo csv para trabajar con archivos CSV
import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV con formato específico
    """
    # Validamos que el inventario no esté vacío
    if not inventario:
        print("Error: No se puede guardar un inventario vacío.")
        return False  # Retornamos False indicando que falló
    
    try:
        # Abrimos el archivo en modo escritura ('w')
        # newline='' evita líneas en blanco extra en Windows
        # encoding='utf-8' permite caracteres especiales (tildes, ñ, etc.)
        with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
            # Creamos un objeto escritor CSV
            escritor = csv.writer(archivo)
            
            # Si se solicita, escribimos el encabezado
            if incluir_header:
                # Escribimos la primera fila con los nombres de las columnas
                escritor.writerow(["nombre", "precio", "cantidad"])
            
            # Recorremos cada producto del inventario
            for producto in inventario:
                # Escribimos una fila por cada producto con sus datos
                escritor.writerow([
                    producto["nombre"],    # Columna 1: nombre
                    producto["precio"],    # Columna 2: precio
                    producto["cantidad"]   # Columna 3: cantidad
                ])
        
        # Si todo salió bien, mostramos mensaje de éxito
        print(f"Inventario guardado exitosamente en: {ruta}")
        return True  # Retornamos True indicando éxito
        
    except PermissionError:
        # Error cuando no tenemos permisos para escribir en la ubicación
        print("Error: No tienes permisos para escribir en esta ubicación.")
        return False
    except Exception as e:
        # Capturamos cualquier otro error inesperado
        print(f"Error inesperado al guardar: {e}")
        return False

def cargar_csv(ruta):
    """
    Carga un inventario desde un archivo CSV con validaciones exhaustivas
    """
    # Inicializamos lista para productos válidos
    inventario_cargado = []
    # Contador para filas con errores
    filas_invalidas = 0
    
    try:
        # Abrimos el archivo en modo lectura ('r')
        with open(ruta, 'r', encoding='utf-8') as archivo:
            # Creamos un objeto lector CSV
            lector = csv.reader(archivo)
            
            # Leemos la primera fila (encabezado) - next() avanza una fila
            encabezado = next(lector, None)  # None es valor por defecto si no hay filas
            
            # Validamos que el encabezado sea correcto
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: El archivo CSV no tiene el formato correcto.")
                print(f"Encabezado esperado: nombre,precio,cantidad")
                # Mostramos qué encabezado encontramos (si existe)
                print(f"Encabezado encontrado: {','.join(encabezado) if encabezado else 'Ninguno'}")
                return None  # Retornamos None indicando error grave
            
            # Recorremos cada fila del archivo (empezando desde la fila 2)
            # enumerate(lector, start=2) numera las filas desde 2 (fila 1 es encabezado)
            for numero_fila, fila in enumerate(lector, start=2):
                # Validamos que la fila tenga exactamente 3 columnas
                if len(fila) != 3:
                    print(f"Fila {numero_fila} inválida: debe tener 3 columnas, tiene {len(fila)}")
                    filas_invalidas += 1  # Incrementamos contador de errores
                    continue  # Saltamos a la siguiente fila
                
                # Desempaquetamos la fila en tres variables
                nombre, precio_str, cantidad_str = fila
                
                try:
                    # Convertimos precio de string a float
                    precio = float(precio_str)
                    # Validamos que el precio no sea negativo
                    if precio < 0:
                        print(f"Fila {numero_fila} inválida: precio no puede ser negativo")
                        filas_invalidas += 1
                        continue  # Saltamos a la siguiente fila
                    
                    # Convertimos cantidad de string a int
                    cantidad = int(cantidad_str)
                    # Validamos que la cantidad no sea negativa
                    if cantidad < 0:
                        print(f"Fila {numero_fila} inválida: cantidad no puede ser negativa")
                        filas_invalidas += 1
                        continue  # Saltamos a la siguiente fila
                    
                    # Creamos el diccionario del producto
                    producto = {
                        "nombre": nombre.strip(),  # .strip() elimina espacios al inicio/final
                        "precio": precio,
                        "cantidad": cantidad
                    }
                    # Agregamos el producto válido a la lista
                    inventario_cargado.append(producto)
                    
                except ValueError as e:
                    # Error al convertir string a número (float o int)
                    print(f"Fila {numero_fila} inválida: datos numéricos incorrectos - {e}")
                    filas_invalidas += 1
                    continue  # Saltamos a la siguiente fila
        
        # Mostramos resumen de la carga
        print(f"Archivo cargado: {len(inventario_cargado)} productos válidos, {filas_invalidas} filas inválidas omitidas")
        return inventario_cargado  # Retornamos la lista de productos válidos
        
    except FileNotFoundError:
        # Error cuando el archivo no existe
        print(f"Error: El archivo '{ruta}' no existe.")
        return None
    except UnicodeDecodeError:
        # Error cuando el archivo no tiene codificación UTF-8 válida
        print("Error: El archivo tiene problemas de codificación (no es UTF-8 válido).")
        return None
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"Error inesperado al cargar el archivo: {e}")
        return None

def fusionar_inventarios(inventario_actual, inventario_nuevo):
    """
    Fusiona dos inventarios: actualiza productos existentes y agrega nuevos
    """
    # Creamos una copia del inventario actual para no modificar el original
    inventario_fusionado = inventario_actual.copy()
    
    # Creamos un diccionario para búsqueda rápida por nombre
    # Convertimos nombres a minúsculas para búsqueda case-insensitive
    productos_actuales = {prod["nombre"].lower(): prod for prod in inventario_fusionado}
    
    # Recorremos cada producto del inventario nuevo
    for producto_nuevo in inventario_nuevo:
        nombre = producto_nuevo["nombre"]
        nombre_lower = nombre.lower()  # Convertimos a minúsculas para comparar
        
        # Verificamos si el producto ya existe en el inventario actual
        if nombre_lower in productos_actuales:
            # Producto existe - actualizamos precio y cantidad
            producto_actual = productos_actuales[nombre_lower]
            # Actualizamos al nuevo precio (reemplazamos el anterior)
            producto_actual["precio"] = producto_nuevo["precio"]
            # Sumamos la nueva cantidad a la existente
            producto_actual["cantidad"] += producto_nuevo["cantidad"]
            # Informamos al usuario de la actualización
            print(f"Actualizado: {nombre} - Nuevo precio: ${producto_nuevo['precio']:.2f}, Cantidad añadida: {producto_nuevo['cantidad']}")
        else:
            # Producto nuevo - lo agregamos al inventario
            inventario_fusionado.append(producto_nuevo)
            print(f"Agregado: {nombre}")
    
    # Retornamos el inventario fusionado
    return inventario_fusionado