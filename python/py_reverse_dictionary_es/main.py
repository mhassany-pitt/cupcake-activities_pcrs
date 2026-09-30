def busqueda_inversa_diccionario(num_telefono, telefono_a_nombre):
    """"" (str, dict de {str: str}) -> str

    Esta funcion recibe un numero de telefono num_telefono, y un diccionario
    telefono_a_nombre en el cual cada clave es un numero de telefono y cada valor
    es el nombre asociado con ese numero de telefono.
	
    Devuelve el nombre asociado con num_telefono en telefono_a_nombre, o
    un string vacio si no hay coincidencia.
    
    >>> busqueda_inversa_diccionario("416-555-3498", {"416-555-3498": \\
        "John A. Macdonald", "647-555-9812": "Louis Riel", "416-555-6543": \\
        "Canoe Head", "905-555-6681":"Tim Horton"})
    'John A. Macdonald'   """     
