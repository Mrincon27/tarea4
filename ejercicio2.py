def diccionario(dict1, dict2):
    for i, value in dict1.items():
        if dict2.get(i) != value:
            return False
        return True
    print

