def agregar_intervalo(mil, intervalo):
    # Inicializar la lista de resultados
    resultado = []
    i = 0
    n = len(mil)
    
    # Agregar todos los intervalos que vienen antes del nuevo intervalo
    while i < n and mil[i][1] < intervalo[0]:
        resultado.append(mil[i])
        i += 1
    
    # Fusionar todos los intervalos que se superponen con el nuevo intervalo
    while i < n and mil[i][0] <= intervalo[1]:
        intervalo = (min(intervalo[0], mil[i][0]), max(intervalo[1], mil[i][1]))
        i += 1
    
    # Agregar el nuevo intervalo fusionado
    resultado.append(intervalo)
    
    # Agregar los intervalos restantes
    while i < n:
        resultado.append(mil[i])
        i += 1
    
    return resultado

# Ejemplo de uso
mil = [(0, 2), (3, 6), (7, 7), (9, 12)]
intervalo = (1, 8)
print(agregar_intervalo(mil, intervalo))  # Salida: [(0, 8), (9, 12)]