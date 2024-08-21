sujetos =  [
        {'nombres': 'Pedro Julio', 'apellidos': 'Rodriguez', 'edad': 10},
        {'nombres': 'Laura', 'apellidos': 'Hernández', 'edad': 34},
        {'nombres': 'Ana María', 'apellidos': 'González', 'edad': 22},
        {'nombres': 'Luis', 'apellidos': 'García López', 'edad': 48},
        {'nombres': 'Sofía', 'apellidos': 'Pérez', 'edad': 27},
        {'nombres': 'Carlos', 'apellidos': 'Mendoza', 'edad': 19},
        {'nombres': 'Marta', 'apellidos': 'González', 'edad': 35},
        {'nombres': 'Jorge', 'apellidos': 'Rodriguez', 'edad': 62},
        {'nombres': 'Miguel', 'apellidos': 'Fernández', 'edad': 23},
        {'nombres': 'Isabel', 'apellidos': 'Martínez', 'edad': 41}
    ]
def personas(gente, edad_minima, edad_maxima):
    
    for persona in gente:
        edad = persona.get("edad")
        if edad_minima <= edad <= edad_maxima:
            nombres = persona.get("nombres", "Desconocido")
            apellidos = persona.get("apellidos", "Desconocido")
            print(f"Nombres: {nombres}, Apellidos: {apellidos}")

def edad():
    edad_minima = int(input("Ingrese la edad mínima del rango: "))
    edad_maxima = int(input("Ingrese la edad máxima del rango: "))
    if edad_minima > edad_maxima:
        print("La edad mínima no puede ser mayor que la edad máxima.")
        return
    personas(sujetos, edad_minima, edad_maxima)
    
