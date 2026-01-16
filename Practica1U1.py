lista_calificaciones = [8.0, 9.0, 10.0]  
tupla_ubicacion = (20.653622660566754, -100.4054156040559) #Aula        

promedio_final = sum(lista_calificaciones) / len(lista_calificaciones)

#DICCIONARIO
estudiante = {
    "nombre": "Mauricio Ferrusca",
    "Calificaciones": lista_calificaciones,
    "Aula": tupla_ubicacion,
    "promedio": promedio_final
}
cadena = (
    f"Ficha del estudiante:\n"
    f"Nombre: {estudiante['nombre']}\n"
    f"Calificaciones: {', '.join(str(x) for x in estudiante['Calificaciones'])}\n"
    f"Aula: {estudiante['Aula']}\n"
    f"Promedio: {estudiante['promedio']:.2f}"
)

print(cadena)