def escribir_triangulo_ascii(triangulo_doc, bloque, longitud_lado):
    """ (Archivo abierto para escribir, str, int) -> NoneType
    
    Precondicion: len(bloque) == 1
    
    Escribe un triangulo rectangulo isosceles de caracteres bloque que es
    longitud_lado caracteres de ancho y alto en triangulo_doc. El angulo recto
    debe estar en la esquina superior izquierda. Por ejemplo, dado
    bloque="@" y longitud_lado=4, lo siguiente debe escribirse en triangulo_doc:
    
    @@@@
    @@@
    @@
    @
    """