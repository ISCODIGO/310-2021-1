class Alumno:
    __slots__ = ['cuenta', 'nombre', 'carrera']

    def __init__(self, cuenta:str, nombre:str, carrera:str) -> None:
        self.cuenta = cuenta
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self):
        # Uso de interpolacion de cadenas
        return f"Cuenta: {self.cuenta} Nombre: {self.cuenta}\nCarrera: {self.carrera}"

if __name__ == '__main__':
    a001 = Alumno('20201001234', 'Alexa Amazon', 'Sociologia')
    print(a001)
    #a001.nota_final = 100
    print(a001.__dict__)

    a002 = Alumno('20201001235', 'Ricardo Molina', 'Filosofia')
    print(a002.__dict__)
    