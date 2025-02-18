class Joaquin:
    usuarios = []
    
    def __init__(self, nombre, edad, tiposangre):
        self.nombre = nombre
        self.edad = edad
        self.tiposangre = tiposangre
        Joaquin.usuarios.append(self)

    def mostrarinfo(self):
        return f"El usuario {self.nombre}, tiene {self.edad} años y su tipo de sangre es {self.tiposangre}"

    @classmethod
    def mostarusuarios(cls):
        return cls.usuarios

    @classmethod
    def eliminar_usuario(cls, indice):
        if 0 <= indice < len(cls.usuarios):
            del cls.usuarios[indice]
        else:
            raise IndexError("Índice fuera de rango")

    @classmethod
    def editar_usuario(cls, indice, nombre, edad, tiposangre):
        if 0 <= indice < len(cls.usuarios):
            usuario = cls.usuarios[indice]
            usuario.nombre = nombre
            usuario.edad = edad
            usuario.tiposangre = tiposangre
        else:
            raise IndexError("Índice fuera de rango")
