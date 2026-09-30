
def entero_unico(lista_numeros):
    """
    Encuentra el numero unico en una lista de numeros enteros impares.
    
    :param lista_numeros: Lista de numeros enteros
    :return: El numero unico en la lista
    """
    contador = {}
    
    for numero in lista_numeros:
        # Si el numero ya esta en el contador, incrementa su cuenta
        if numero in contador:
            contador[numero] += 1
        else:
            # Si no, inicializa su cuenta en 1
            contador[numero] = 1
    
    for numero, cuenta in contador.items():
        # Devuelve el numero cuya cuenta es 1
        if cuenta == 1:
            return numero

# Ejemplo de uso
lista = [1, 1, 2, 2, 3, 4, 4]
print(entero_unico(lista))  # Salida: 3