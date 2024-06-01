import json
class Paciente: 
    pacientes = []
    def __init__(self, name, age, ID, lastname):
        self.__name = name
        self.__age = age
        self.__lastname = lastname
        self.__ID: ID
        self.__login = "admin123"
        self.__password = "contrasena123"
        self.cargar_pacientes_desde_archivo("pacientes.json")

    def setlogin(self, admin123):
        self.__login = admin123

    def setPassword(self, contrasena123):
        self.__password = contrasena123

    def Validar_usuario(self, admin123, contrasena123):
        if (self.__login == admin123) and (self.__password == contrasena123):
            return "BIENVENID@"
        else:
            return "USUARIO INVALIDO"
        
    def name(self):
        return self.__name

    def lastname(self):
        return self.__lastname

    def age(self):
        return self.__age

    def ID(self):
        return self.__ID
    
    def agregar_paciente(self, name, lastname, edad, ID):
        if not self.verificar_existencia(ID):
            paciente = (name, lastname, edad, ID)
            self.pacientes.append(paciente)
            self.guardar_pacientes("pacientes.json")
            return True
        else: 
             return False
        
    def verificar_existencia(self, ID):
        for paciente in self.pacientes:
            if paciente[3] == ID:
                return True
        return False

    def guardar_pacientes(self, archivo):
       pacientes_json = [
           {
               "nombre" : paciente[0],
               "apellido": paciente[1],
               "edad": paciente[2],
               "ID" : paciente[3]
           }
           for paciente in self.pacientes
       ]
       with open(archivo, 'w') as f:
           json.dump(pacientes_json, f, indent=2)


    def cargar_pacientes_desde_archivo(self, archivo):
        self.pacientes = []
        with open(archivo, 'r') as f:
            pacientes_json = json.load(f)

            for paciente_json in pacientes_json:
                paciente = (
                    paciente_json["nombre"],
                    paciente_json["apellido"],
                    paciente_json["edad"],
                    paciente_json["ID"]
                )
                self.pacientes.append(paciente)
                
    def buscar_paciente(self, buscar_nombre):
        busqueda = []
        for paciente in self.pacientes:
            if paciente[0].lower().startswith(buscar_nombre.lower()):
                busqueda.append(paciente)
        return busqueda

    
    def eliminar_paciente(self, ID):
        for paciente in self.pacientes:
            if paciente[3] == ID:
                self.pacientes.remove(paciente)
                self.guardar_pacientes("pacientes.json")
                return True
        return False
    
    
                