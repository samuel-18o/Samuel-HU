# Importamos todas las funciones de nuestros módulos
from servicios import *
from archivos import *

def mostrar_menu():
    """
    Muestra el menú principal del sistema con formato claro
    """
    print("\n" + "="*50)  # Línea separadora
    print("          SISTEMA DE INVENTARIO")
    print("="*50)
    # Opciones numeradas del 1 al 9
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Ver estadísticas")
    print("7. Guardar en CSV")
    print("8. Cargar desde CSV")
    print("9. Salir")
    print("="*50)

def preguntar_sobrescribir():
    """
    Pregunta al usuario si quiere sobrescribir o fusionar el inventario
    """
    # Bucle infinito hasta que el usuario dé una respuesta válida
    while True:
        # Pedimos la respuesta y normalizamos (mayúsculas, sin espacios)
        respuesta = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
        # Verificamos si la respuesta es válida
        if respuesta in ['S', 'N']:
            return respuesta  # Retornamos la respuesta válida
        # Si no es válida, mostramos mensaje y repetimos
        print("Por favor, ingresa 'S' para Sobrescribir o 'N' para No sobrescribir")

def ejecutar_opcion(opcion, inventario):
    """
    Ejecuta la opción seleccionada del menú
    Retorna el inventario (puede haber cambiado por carga/fusión)
    """
    # OPCIÓN 1: Agregar producto
    if opcion == 1:
        print("\n--- AGREGAR PRODUCTO ---")
        # Pedimos el nombre y eliminamos espacios extras
        nombre = input("Nombre del producto: ").strip()
        
        # Validamos que el nombre no esté vacío
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return inventario  # Retornamos sin cambios
        
        # Validamos que el producto no exista ya
        if buscar_producto(inventario, nombre):
            print(f"Error: El producto '{nombre}' ya existe.")
            return inventario  # Retornamos sin cambios
        
        # Pedimos y validamos el precio
        precio_str = input("Precio: ")
        precio = validar_numero_positivo(precio_str, "precio")
        if precio is None:  # Si la validación falló
            return inventario
        
        # Pedimos y validamos la cantidad
        cantidad_str = input("Cantidad: ")
        cantidad = validar_numero_positivo(cantidad_str, "entero")
        if cantidad is None:  # Si la validación falló
            return inventario
        
        # Si todas las validaciones pasaron, agregamos el producto
        # .capitalize() pone la primera letra en mayúscula y el resto en minúsculas
        agregar_producto(inventario, nombre.capitalize(), precio, cantidad)
        
    # OPCIÓN 2: Mostrar inventario
    elif opcion == 2:
        mostrar_inventario(inventario)  # Llamamos la función directa
        
    # OPCIÓN 3: Buscar producto
    elif opcion == 3:
        print("\n--- BUSCAR PRODUCTO ---")
        nombre = input("Nombre del producto a buscar: ").strip()
        # Buscamos el producto
        producto = buscar_producto(inventario, nombre)
        
        # Si encontramos el producto, mostramos sus datos
        if producto:
            print(f"\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
        else:
            print(f"Producto '{nombre}' no encontrado.")
            
    # OPCIÓN 4: Actualizar producto
    elif opcion == 4:
        print("\n--- ACTUALIZAR PRODUCTO ---")
        nombre = input("Nombre del producto a actualizar: ").strip()
        
        # Buscamos el producto primero
        producto = buscar_producto(inventario, nombre)
        if not producto:
            print(f"Error: Producto '{nombre}' no encontrado.")
            return inventario
        
        # Mostramos los datos actuales del producto
        print(f"Producto actual: {producto['nombre']} - Precio: ${producto['precio']:.2f} - Cantidad: {producto['cantidad']}")
        
        # Inicializamos variables para los nuevos valores
        nuevo_precio = None
        nueva_cantidad = None
        
        # Preguntamos si quiere actualizar el precio
        actualizar_precio = input("¿Actualizar precio? (S/N): ").strip().upper()
        if actualizar_precio == 'S':
            precio_str = input("Nuevo precio: ")
            nuevo_precio = validar_numero_positivo(precio_str, "precio")
            if nuevo_precio is None:  # Si la validación falló
                return inventario
        
        # Preguntamos si quiere actualizar la cantidad
        actualizar_cantidad = input("¿Actualizar cantidad? (S/N): ").strip().upper()
        if actualizar_cantidad == 'S':
            cantidad_str = input("Nueva cantidad: ")
            nueva_cantidad = validar_numero_positivo(cantidad_str, "entero")
            if nueva_cantidad is None:  # Si la validación falló
                return inventario
        
        # Si al menos un campo se va a actualizar, llamamos la función
        if actualizar_precio == 'S' or actualizar_cantidad == 'S':
            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
        else:
            print("No se realizaron cambios.")
            
    # OPCIÓN 5: Eliminar producto
    elif opcion == 5:
        print("\n--- ELIMINAR PRODUCTO ---")
        nombre = input("Nombre del producto a eliminar: ").strip()
        eliminar_producto(inventario, nombre)
        
    # OPCIÓN 6: Estadísticas
    elif opcion == 6:
        mostrar_estadisticas(inventario)
        
    # OPCIÓN 7: Guardar CSV
    elif opcion == 7:
        print("\n--- GUARDAR INVENTARIO ---")
        # Pedimos la ruta, con valor por defecto si no se ingresa nada
        ruta = input("Ruta del archivo CSV (enter para 'inventario.csv'): ").strip()
        if not ruta:  # Si la ruta está vacía
            ruta = "inventario.csv"  # Usamos valor por defecto
        guardar_csv(inventario, ruta)
        
    # OPCIÓN 8: Cargar CSV
    elif opcion == 8:
        print("\n--- CARGAR INVENTARIO ---")
        # Pedimos la ruta, con valor por defecto si no se ingresa nada
        ruta = input("Ruta del archivo CSV (enter para 'inventario.csv'): ").strip()
        if not ruta:  # Si la ruta está vacía
            ruta = "inventario.csv"  # Usamos valor por defecto
        
        # Intentamos cargar el archivo
        inventario_cargado = cargar_csv(ruta)
        
        # Si la carga fue exitosa (no None)
        if inventario_cargado is not None:
            # Si ya hay productos en el inventario actual
            if inventario:
                print("\nInventario actual no está vacío.")
                # Preguntamos qué hacer con los datos existentes
                opcion_carga = input("¿Sobrescribir inventario actual? (S=sobrescribir, N=fusionar, C=cancelar): ").strip().upper()
                
                if opcion_carga == 'S':
                    # Reemplazamos completamente el inventario
                    inventario = inventario_cargado
                    print("Inventario reemplazado exitosamente.")
                elif opcion_carga == 'N':
                    # Fusionamos los inventarios
                    inventario = fusionar_inventarios(inventario, inventario_cargado)
                    print("Inventarios fusionados exitosamente.")
                else:
                    # Cancelamos la operación
                    print("Carga cancelada.")
            else:
                # Inventario vacío, simplemente cargamos
                inventario = inventario_cargado
                print("Inventario cargado exitosamente.")
    
    # Retornamos el inventario (puede haber cambiado)
    return inventario

def main():
    """
    Función principal del sistema - Punto de entrada del programa
    """
    # Inicializamos el inventario como lista vacía
    inventario = []
    print("¡Bienvenido al Sistema de Gestión de Inventario!")
    
    # Intentamos cargar inventario automáticamente al inicio si existe
    try:
        inventario_cargado = cargar_csv("inventario.csv")
        if inventario_cargado:
            inventario = inventario_cargado
            print("Inventario cargado automáticamente desde 'inventario.csv'")
    except:
        # Si hay error en la carga automática, comenzamos con inventario vacío
        print("No se encontró archivo de inventario previo. Comenzando con inventario vacío.")
    
    # BUCLE PRINCIPAL DEL PROGRAMA
    while True:
        try:
            # Mostramos el menú en cada iteración
            mostrar_menu()
            # Pedimos la opción al usuario
            opcion_str = input("Selecciona una opción (1-9): ").strip()
            
            # Validamos la opción del menú
            opcion = validar_opcion_menu(opcion_str)
            if opcion is None:  # Si la validación falló
                input("Presiona Enter para continuar...")
                continue  # Volvemos al inicio del bucle
            
            # OPCIÓN 9: Salir del programa
            if opcion == 9:
                # Preguntamos si quiere guardar antes de salir
                print("\n¿Deseas guardar el inventario antes de salir?")
                guardar = input("Guardar inventario antes de salir? (S/N): ").strip().upper()
                if guardar == 'S':
                    guardar_csv(inventario, "inventario.csv")
                # Mensaje de despedida
                print("¡Gracias por usar el Sistema de Inventario! ¡Hasta pronto!")
                break  # Rompemos el bucle y salimos del programa
            
            # Ejecutamos la opción seleccionada
            inventario = ejecutar_opcion(opcion, inventario)
            # Pausa para que el usuario pueda leer los resultados
            input("\nPresiona Enter para continuar...")
            
        except KeyboardInterrupt:
            # El usuario presionó Ctrl+C
            print("\n\nPrograma interrumpido por el usuario.")
            break  # Salimos del programa
        except Exception as e:
            # Capturamos cualquier error inesperado
            print(f"\nError inesperado: {e}")
            print("El programa continuará...")
            input("Presiona Enter para continuar...")

# Punto de entrada estándar en Python
# Esto asegura que main() solo se ejecute si ejecutamos este archivo directamente
if __name__ == "__main__":
    main()