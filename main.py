class Libro:
    def __init__(self, titulo, autor, anio):
        self.Titulo = titulo
        self.Autor = autor
        self.Anio = anio

    def mostrar_dato(self):
        print(f'Titulo: {self.Titulo} Autor: {self.Autor} Anio: {self.Anio} ')

class RegistroLibros:
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
                       if code in list(self.libros.keys()) :
                           print('Error - Este libro ya existe no puede ser añadido')
                           break
                       else:
                           titulo = input('Ingrese el titulo: ')
                           autor = input('Ingrese el autor: ')
                           anio = int(input('Ingrese el año de publicación: '))
                           libro_tmp = Libro(titulo, autor, anio)
                           self.libros[code] = {
                              "Libro" : libro_tmp
                           }
                           print(f'libro {titulo}  Agregado con exito')
                           break

                   except ValueError:
                       print('Error -Ingreso un dato incorrecto verifique nuevamente')

        except Exception as e:
            print('Error - Oucrrio un error inesperado')

    def mostrar_libros(self):

        if not self.libros:
            print('No hay libros registrados aún')
        else:
            for llave, cont in self.libros.items():
                print(f'Codigo {llave} ')
                cont["Libro"].mostrar_dato() #Llama al metodo por defecto para presentarse



class Usuario:

    def __init__(self, nombre, carrera):
        self.Nombre = nombre
        self.Carrera = carrera

    def mostrar_usuario(self):
        print(f'Nombre: {self.Nombre} Carrera: {self.Carrera}')


class RegistroUsuarios:

    def __init__(self):
        self.usuarios = {} #Se crea un diccionario vacio donde se guardan todos los usuarios creados


    def crear_usuario(self):

        while True:
            try:
                cant = int(input('Ingrese la cantidad de cuantos usuarios desea crear: '))
                for j in range(cant):
                    print(f'Ingrese los datos del {j+1} usuario')
                    carnet = input('Ingrese el numero de carnet: ')
                    if carnet in list(self.usuarios.keys()):
                        print('Error este carnet ya existe no puede ser duplicado')
                        break

                    else:
                        nombre = input('Escriba el nombre: ')
                        carrera = input('Ingrese la carreara: ')
                        usuario_tmp = Usuario(nombre, carrera)
                        self.usuarios[carnet] = {
                            "Usuario" : usuario_tmp
                        }
                        print(f'Agregado con exito!!! {carnet} ')

            except Exception as e:
                print('Error - Por favor verifique la entrada de datos y vuelva a intentarlo')

    def mostrar_usuarios(self):

        if not self.usuarios:
            print('No hay ningun usuario registrado aún')
        else:
            for llave, campo in self.usuarios.items():
                print(f'Carnet: {llave}')
                campo["Usuario"].mostrar_usuario()




class Gestion:
    registro_diarioU = RegistroUsuarios() #Se crea una instancia de registro de usuarios de ese dia u ocasion
    registro_diarioL = RegistroLibros()  #Se crea una instancia para crear la coleccion de libros
    #Si se necesita crear usuarios estos quedaran guardados desde aqui entonces luego para manipular los datos
    #Se ocupan estos metodos de abajo para realizar los procesos de gestion

    def prestamo_libro(self):
        pass

    def devolucion_libro(self):
        pass


fin_menu = True

dia = Gestion()
while fin_menu:
    try:
        print('\t\t\t¡Bienvenido a la gestion bibliotecaria!')
        print('1.Ingreso de libros\n2.Ingreso de usuarios\n3.Gestion de prestamos y devoluciones \n4.Salir')
        opcion = int(input('Ingrese la opción que desea ingresar: '))
        match opcion:
            case 1:
                print('Bienvenido al ingreso de libros y control de existencia: ')
                dia.registro_diarioL.agregar_libro()
                print('Inventario')
                dia.registro_diarioL.mostrar_libros()

            #case 2:
            #case 3:
            case 4:
                print('Gracias por usar el programa')
                fin_menu = False
            case _:
                print('Opcion inexistente por favor verificar')

    except Exception as e:
        print('Ocurrio un error - Favor de verificar la selección de opciones')



