# Importar el módulo de funciones que contiene toda la lógica del negocio
import funciones

def mostrar_menu():
    """Mostrar menú principal"""
    print("\n" + "="*65)  # Línea decorativa para mejor presentación
    print("SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS")
    print("="*65)
    print("  1. Agregar nuevo producto")
    print("  2. Ver todos los productos")
    print("  3. Actualizar producto")
    print("  4. Eliminar producto")
    print("  5. Registrar nueva venta")
    print("  6. Ver historial de ventas")
    print("  7. Top 3 productos más vendidos")
    print("  8. Ventas por marca")
    print("  9. Reporte de ingresos")
    print("  10. Rendimiento del inventario")
    print("\n  0. Salir")
    print("="*65)

def main():
    """Bucle principal de la aplicación"""
    print("\n🔧 Inicializando sistema...")
    funciones.inicializar_datos()  # Cargar datos iniciales y archivos
    print("✅ ¡Sistema listo!\n")
    
    # Bucle infinito que mantiene la aplicación corriendo
    while True:
        try:
            mostrar_menu()  # Mostrar opciones al usuario
            opcion = input("\nSeleccione una opción: ").strip()  # strip() elimina espacios en blanco
            
            # Estructura if-elif para manejar todas las opciones del menú
            # Esta estructura es escalable y fácil de mantener
            if opcion == '1':
                funciones.agregar_producto()  # Llamar función específica del CRUD
            
            elif opcion == '2':
                funciones.ver_productos()  # Función de lectura/consulta
            
            elif opcion == '3':
                funciones.actualizar_producto()  # Función de actualización
            
            elif opcion == '4':
                funciones.eliminar_producto()  # Función de eliminación
            
            elif opcion == '5':
                funciones.registrar_venta()  # Función de proceso de ventas
            
            elif opcion == '6':
                funciones.ver_ventas()  # Consulta de historial
            
            elif opcion == '7':
                funciones.top_3_productos()  # Reporte analítico
            
            elif opcion == '8':
                funciones.ventas_por_marca()  # Reporte por categoría
            
            elif opcion == '9':
                funciones.calcular_ingresos()  # Reporte financiero
            
            elif opcion == '10':
                funciones.rendimiento_inventario()  # Reporte de inventario
            
            elif opcion == '0':
                print("\n👋 ¡Gracias por usar el sistema. Hasta luego!")
                break  # Romper el bucle para salir
            
            else:
                print("\n❌ Opción inválida. Por favor intente nuevamente.")
            
            # Pausa para que el usuario pueda leer los resultados
            input("\nPresione Enter para continuar...")
            
        # Manejo de interrupción por teclado (Ctrl+C)
        except KeyboardInterrupt:
            print("\n\n⚠️ Operación cancelada por el usuario")
            confirmar = input("¿Desea salir? (si/no): ").lower()
            if confirmar == 'si':
                print("\n👋 ¡Hasta luego!")
                break  # Salir confirmada
        
        # Manejo de cualquier error inesperado
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            print("El sistema continuará funcionando...")  # Sistema resiliente

# Patrón común en Python: ejecutar main() solo si es el script principal
if __name__ == "__main__":
    main()