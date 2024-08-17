class Paciente:
    def __init__(self, nombre, cedula, genero, servicio):
        self.nombre = nombre
        self.cedula = cedula
        self.genero = genero
        self.servicio = servicio

    def __str__(self):
        return (f' Paciente con los siguientes datos: Nombre: {self.nombre}, Cédula: {self.cedula}, Género: {self.genero}, Servicio: {self.servicio}')
    
class Sistema: 
    def __init__(self):
        self.pacientes = {}

    def agregarPaciente(self, nombre, cedula, genero, servicio):
        if cedula in self.pacientes:
            print('El paciente con esta cédula ya está registrado.')
        else:
            self.pacientes[cedula] = Paciente(nombre, cedula, genero, servicio)
            print('El paciente se ha registrado correctamente.')

    def verDatos(self, cedula):
        paciente = self.pacientes.get(cedula)
        if paciente: 
            print(paciente)
        else: 
            print('Paciente no encontrado.')

    def numPacientes(self):
        print(f'El número de pacientes en el sistema: {len(self.pacientes)}')


miSistema = Sistema()

while True:
    opcion = int(input('1. Ingresar un nuevo paciente\n2. Ver el número de pacientes\n3. Ver los datos de un paciente\n4. Salir\n '))
    if opcion == 1:
        nombre = input('Ingrese el nombre del paciente: ')
        cedula = input('Ingrese la cédula: ')
        genero = input('Ingrese el género: Masculino o Femenino: ')
        servicio = input('Ingrese el servicio en el cual se encuentra alojado: ')

        miSistema.agregarPaciente(nombre, cedula, genero, servicio)

    elif opcion == 2:
        miSistema.numPacientes()

    elif opcion == 3:
        cedula = input('Ingrese la cédula del paciente: ')
  
        miSistema.verDatos(cedula)

    elif opcion == 4:
        print('Gracias por usar, saliendo del sistema... ')
        break

    else: 
        print('Ingrese una opción correcta.')
        