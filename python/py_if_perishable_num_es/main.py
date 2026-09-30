
# Este programa verifica si un articulo es perecedero basado en su codigo de barras
codigo_barras = 342564643  # Ejemplo de codigo de barras

# Verificar si el codigo de barras es un numero entero de 9 digitos
if len(str(codigo_barras)) == 9:
    # Obtener el ultimo digito del codigo de barras
    ultimo_digito = int(str(codigo_barras)[-1])
    
    # Verificar si el ultimo digito indica que el articulo es perecedero
    if ultimo_digito in [3, 4, 7]:
        print('SI')  # El articulo es perecedero
    else:
        print('NO')  # El articulo no es perecedero
else:
    print('Invalido')  # El codigo de barras no es valido