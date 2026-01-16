'''
#paso 1 : Solicitar temperatura
temp = input('Ingresa la temperatura en C: ')
ciudad = input('Ingresa la ciudad: ')
fecha = input('Ingresa la fecha (DD/MM/AAAA): ')


#Paso 2 : Guardar en archivo
with open('temperatura.txt', 'w') as archivo:
    archivo.write(temp + '\n')

#Paso 3 : Leer y mostrar historial ordenado
with open('temperatura.txt', 'r') as archivo:
    historial = archivo.readlines()

#Convertir los numeros y ordenarlos
historial = [float(t.strip()) for t in historial]
historial.sort()

#imprimir el historial ordenado
print('\nHistorial de temperaturas ordenadas:')
for t in historial:
    print(f'{t} C')
'''


import os

# --- CONSTANTES ---
ARCHIVO_DATOS = 'historial_temperatura.txt'
ARCHIVO_RECOMENDACIONES = 'recomendaciones.txt'

# --- FUNCIONES ---

def guardar_registro(fecha, ciudad, temperatura):
    """Guarda los datos en el archivo CSV."""
    with open(ARCHIVO_DATOS, 'a') as archivo:
        # Formato: fecha,ciudad,temperatura
        linea = "{},{},{}\n".format(fecha, ciudad, temperatura)
        archivo.write(linea)

def mostrar_estadisticas():
    """Lee el archivo y calcula promedio, máximo y mínimo."""
    if not os.path.exists(ARCHIVO_DATOS):
        print("\n[!] No hay historial de datos para analizar aún.")
        return

    temperaturas = []
    
    print("\n--- Historial Registrado ---")
    with open(ARCHIVO_DATOS, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(',')
            if len(partes) == 3:
                fecha, ciudad, temp_str = partes
                try:
                    temp_val = float(temp_str)
                    temperaturas.append(temp_val)
                    print(f"Fecha: {fecha} | Ciudad: {ciudad} | Temp: {temp_val}°C")
                except ValueError:
                    # Ignoramos líneas corruptas pero no detenemos el programa
                    continue 

    # Cálculo Estadístico
    if temperaturas:
        promedio = sum(temperaturas) / len(temperaturas)
        maximo = max(temperaturas)
        minimo = min(temperaturas)
        
        print("\n--- Resumen Estadístico ---")
        print(f"Promedio: {promedio:.2f}°C")
        print(f"Máxima:   {maximo}°C")
        print(f"Mínima:   {minimo}°C")
    else:
        print("\n[!] No se encontraron temperaturas válidas para calcular.")

def solicitar_recomendacion():
    """Pide y guarda una reflexión del usuario."""
    print("\n--- Reflexión ---")
    recomendacion = input("Basado en el clima registrado, ¿qué recomendación personal darías? ")
    
    if recomendacion.strip(): # Verifica que no esté vacío
        with open(ARCHIVO_RECOMENDACIONES, 'a') as archivo:
            archivo.write(recomendacion + '\n')
        print("¡Recomendación guardada exitosamente!")
    else:
        print("No se ingresó recomendación.")

# --- EJECUCIÓN PRINCIPAL ---

def main():
    print("=== Registro de Clima ===")

    # Paso 1: Solicitar datos con Validación
    f = input('Ingresa la fecha (DD/MM/AAAA): ')
    c = input('Ingresa la ciudad: ')
    
    # Validación: Aseguramos que la temperatura sea un número
    while True:
        t_input = input('Ingresa la temperatura en C: ')
        try:
            t = float(t_input)
            break # Si es número, salimos del ciclo
        except ValueError:
            print("Error: Por favor ingresa un número válido (ej. 25.5).")

    # Guardamos los datos
    guardar_registro(f, c, t)

    # Paso 2: Mostrar análisis
    mostrar_estadisticas()

    # Paso 3: Recomendación
    solicitar_recomendacion()

if __name__ == "__main__":
    main()

