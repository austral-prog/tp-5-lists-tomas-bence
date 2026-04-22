# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    l1 = lista_de_listas[0]
    l2 = lista_de_listas[1]
    l3 = lista_de_listas[2]

    return[
        l1[ :2],
        l2[1:4],
        l3[-2: ]
    ]
