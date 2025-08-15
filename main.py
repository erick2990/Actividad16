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
            cantidad = int(input('¿cuantos libros desea ingresar?: '))
            for i in range(cantidad):
                while True:
                   try:
                       print('\n\n')
                       print(f'\t\t\tIngrese datos del {i + 1} libro: ')
                       code = int(input('Ingrese el codigo unico: '))
                       if code in list(self.libros.keys()) :
                           print('Error - Este libro ya existe no puede ser añadido')
                           print('Se guardaran los libros inscritos con anterioridad, si desea guaradar mas accede desde el menu principal')
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
                    print('\n\n')
                    print(f'\t\t\tIngrese los datos del {j+1} usuario')
                    carnet = input('Ingrese el numero de carnet: ')
                    if carnet in list(self.usuarios.keys()):
                        print('Error este carnet ya existe no puede ser duplicado')
                        print('Se guardaran los usuarios inscritos con anterioridad, si desea guaradar mas accede desde el menu principal')
                        break

                    else:
                        nombre = input('Escriba el nombre: ')
                        carrera = input('Ingrese la carrera: ')
                        usuario_tmp = Usuario(nombre, carrera)
                        self.usuarios[carnet] = {
                            "Usuario" : usuario_tmp
                        }
                        print(f'Agregado con exito!!! \n{carnet} ')
                break

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
    prestados = {} #En este diccionario se guardaran los libros prestados y junto con los datos del usuario que posee el libro

    def prestamo_libro(self):
        print('Se desplegara la informacion de libros e ingrese el carnet del usuario que realizara el prestamo juntamente con el codigo del libro: ')
        self.registro_diarioL.mostrar_libros()
        while True:
            try:
                code_prestamo = int(input('Ingrese el codigo del libro que desea prestar: ')) #Este si es un dato tipo entero
                if code_prestamo in self.registro_diarioL.libros.keys():
                    print('Encontrado!! \nPor favor vincule a un usuario para realizar el prestamo por medio de su carnet')
                    while True:
                        carnet_prestamo = input('Ingrese el carnet del usuario: ')  # Este dato es una cadena de texto
                        if carnet_prestamo in list(self.registro_diarioU.usuarios.keys()) :
                            print('Encontrado!!!')
                            #se guardan los datos del libro y el usuario en un diccionario que los vincula

                            break #Termina de buscarlo hasta que tenga un carnet valido
                        else:
                            print('No hay registro de este usuario por favor vuelva a intentarlo')

                    break #termina si se encontro y todo fue hecho correcto
                else:
                    print('El codigo no coincide con niguno de los registros')
            except ValueError:
                print('Error - vuelva a intentarlo')




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
                print('\t\t\tBienvenido al ingreso de libros y control de existencia: ')
                dia.registro_diarioL.agregar_libro()
                print('Inventario\n')
                dia.registro_diarioL.mostrar_libros()

            case 2:
                print('\t\t\tBienvenido al ingreso de usuarios y control de registros: ')
                dia.registro_diarioU.crear_usuario()
                print('Registro Actual\n')
                dia.registro_diarioU.mostrar_usuarios()
            #case 3:
            case 4:
                print('Gracias por usar el programa')
                fin_menu = False
            case _:
                print('Opcion inexistente por favor verificar')

    except Exception as e:
        print('Ocurrio un error - Favor de verificar la selección de opciones')



