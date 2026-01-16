#paso 1 : Solicitar temperatura
temp = input('Ingresa la temperatura en C: ')

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



