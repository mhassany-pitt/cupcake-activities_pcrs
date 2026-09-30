
def contiene_sin_hashtags_unicos(hashtags_tweet, hashtags_unicos):
    """
    (lista de lista de str, lista de str) -> lista de lista de str

    Devuelve una nueva lista de listas de hashtags para aquellos tweets que no pueden ser atribuidos al candidato.
    Un tweet no puede ser atribuido al candidato si no utiliza ninguno de los hashtags unicos utilizados por el candidato.
    Ejemplo entrada/salida:
    contiene_sin_hashtags_unicos([['politica', 'eleccion'], ['futbol', 'deporte'], ['eleccion', 'voto']],['voto'])  -> [['politica', 'eleccion'], ['futbol', 'deporte']]
    
    """

