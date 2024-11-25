def evaluar_alumno(notas):
    # Validamos que las notas ingresadas esten entre los parametros del sistema 0 y 10
    for nota in notas:
        if nota < 0 or nota > 10:
            return "Error: Nota inválida"

    # Validamos de que todas las notas sean enteras
    for nota in notas:
        if nota % 1 != 0:
            return "Error: Nota inválida"

    # Cálculo del promedio
    promedio = sum(notas) / len(notas)

    # Evaluación según las condiciones
    if promedio < 5:
        return "ALUMNO REPROBADO"
    elif promedio < 7:
        return "ALUMNO REGULAR"
    elif promedio >= 7 and all(nota >= 7 for nota in notas):
        return "ALUMNO PROMOCIONADO"
    else:
        return "ALUMNO REGULAR"


# Definismos casos de pruebas para cubrir las sentencias
casos_prueba = [
    ([4, 4, 4, 4, 4, 4], "ALUMNO REPROBADO"),
    ([5, 5, 5, 5, 5, 5], "ALUMNO REGULAR"),
    ([6, 5, 6, 5, 6, 5], "ALUMNO REGULAR"),
    ([7, 7, 7, 7, 7, 6], "ALUMNO REGULAR"),
    ([8, 8, 8, 8, 8, 8], "ALUMNO PROMOCIONADO"),
    ([5, -1, 6, 7, 8, 9], "Error: Nota inválida"),
    ([5, 6, 11, 7, 8, 9], "Error: Nota inválida"),
    ([5.5, 6, 11, 7, 8, 9], "Error: Nota inválida"),
]

# Ejecutamos las pruebas
for i, (notas, esperado) in enumerate(casos_prueba, 1):
    resultado = evaluar_alumno(notas)
    print(
        f"Prueba {i}: {resultado == esperado} (Esperado: {esperado}, Resultado: {resultado})"
    )
