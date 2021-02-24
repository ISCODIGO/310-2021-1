class Externa:
    # Clase que este dentro de la definicion de otra.
    def __init__(self) -> None:
        # Objeto de la clase anidada
        self.objeto_interno = self.Interna()

    def revelar_clase_interna(self):
        self.objeto_interno.mostrar_interior('Esta funcion se ejecuta en la clase Externa pero se definio en la clase Interna')
        
    class Interna:
        # Clase anidada
        def mostrar_interior(self, mensaje:str):
            print(mensaje)

objeto_externo = Externa()
objeto_externo.revelar_clase_interna()