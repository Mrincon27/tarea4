def valores_ordenados(x):
    if not x:
        print("El diccionario está vacío.")
        return
    valor = list(x.values())
    value_type = type(valor[0])
    if not all(isinstance(v, value_type) for v in valor):
        print("Los valores en el diccionario no son todos del mismo tipo.")
        return
    valor_ordenado = sorted(valor)
    print(valor_ordenado)
