def mezcla(diccionario1, diccionario2):
    mezclado = dict(diccionario1)  
    mezclado.update(diccionario2)
    return mezclado
    """resultado ={}
    no_repeticion = set()
    for clave, valor in mezclado.items():
        if valor not in no_repeticion:
            resultado[clave] = valor
            no_repeticion.add(valor)
    print(resultado)
    return resultado"""
    
