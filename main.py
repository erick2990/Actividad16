class Libro:
    def __init__(self, titulo, autor, anio):
        self.Titulo = titulo
        self.Autor = autor
        self.Anio = anio

    def mostrar_dato(self):
        print(f'Titulo: {self.Titulo} Autor: {self.Autor} Anio: {self.Anio} ')

class ResgitroLibros:
    def __init__(self):
        self.libros = {} #Diccionario de libros donde se almacena todos

    def agregar_libro(self):
        try:
            cantidad = int(input('¿cuantos libros desea ingresar?'))
            for i in range(cantidad):
                while True:
                   try:
                       print(f'Ingrese datos del {i + 1} libro: ')
                       code = int(input('Ingrese el codigo unico: '))
                       titulo = input('Ingrese el titulo: ')
                       autor = input('Ingrese el autor: ')
                       anio = int(input('Ingrese el año de publicación: '))
                       libro_tmp = Libro(titulo, autor, anio)
                       self.libros[code] = {libro_tmp}
                       print(f'libro {titulo}  Agregado con exito')
                       break
                   except ValueError:
                       print('Error -Ingreso un dato incorrecto verifique nuevamente')

        except Exception as e:
            print('Error - Oucrrio un error inesperado')

    def prestamo_libro(self):
        pass
    def devolucion_libro(self):
        pass

class Usuario:

    def __init__(self, nombre, carrera):
        self.Nombre = nombre
        self.Carrera = carrera

