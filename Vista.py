import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit,QWidget 
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi

class Login(QWidget):
    def __init__(self,ppal=None, ):
        super().__init__(ppal)
        loadUi("login.ui",self)
        self.setup()
       
    def setup(self):
        self.ingresar.clicked.connect(self.validar)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def validar(self):
        usuario=self.campo_usuario.text()
        contraseña=self.campo_contra.text()
        resultado_validacion=self.coordinador.validar(usuario,contraseña) 
        if resultado_validacion == "BIENVENID@" :
            ventanaopciones=Opciones(self)
            ventanaopciones.set_coordinador(self.coordinador)
            ventanaopciones.show()
            self.hide()
        
    def mensaje(self, message):
        if message != "BIENVENID@":
            QMessageBox.information(self, "Resultado de Login", message)
        else:
            pass

class Opciones(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("opciones_usuario.ui",self)
        self.setup()

    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
        
    def setup(self):
        self.ingresarP.clicked.connect(self.abrirIngresar)
        self.buscarP.clicked.connect(self.abrirBuscar)
        self.eliminarP.clicked.connect(self.abrirEliminar)
        self.salir.clicked.connect(self.cerrarSesion)
    
    def abrirIngresar(self):
        ventana_ingresar= VentanaIngreso(self)
        ventana_ingresar.set_coordinador(self.coordinador)
        self.hide()
        ventana_ingresar.show()
    
    def abrirBuscar(self):
        ventana_buscar= VentanaBuscar(self)
        ventana_buscar.set_coordinador(self.coordinador)
        self.hide()
        ventana_buscar.show()
    
    def abrirEliminar(self):
        ventana_eliminar= VentanaEliminar(self)
        ventana_eliminar.set_coordinador(self.coordinador)
        self.hide()
        ventana_eliminar.show()
    
    def cerrarSesion(self):
        self.hide()


class VentanaIngreso(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("guardar_paciente.ui",self)
        self.setup()
    
    def setup(self):
        self.GUARDAR.clicked.connect(self.validar)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def abrirOpciones(self):
        ventana_opciones= Opciones(self)
        ventana_opciones.set_coordinador(self.coordinador)
        self.hide()
        ventana_opciones.show()
    
    def validar(self):
        ide=self.ide.text()
        resultado_validacion=self.coordinador.verificarIde(ide)
        if resultado_validacion == False:
                nombre=self.nombre.text()
                apellido=self.apellido.text()
                edad=self.edad.text()
                ide=self.ide.text()
                self.coordinador.ingresarInfo(nombre,apellido,edad,ide)
                QMessageBox.information(self,"" ,"¡Paciente ingresado con éxito!")
                self.close()
                self.abrirOpciones()
        else:
            QMessageBox.information(self,"" ,"¡Ya se encuentra un paciente con esa identificación!")

class VentanaBuscar(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("buscar_paciente.ui",self)
        self.setup()
    
    def setup(self):
        self.BUSCAR.clicked.connect(self.buscar)
        self.VOLVER.clicked.connect(self.abrirOpciones)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def abrirOpciones(self):
        ventana_opciones= Opciones(self)
        ventana_opciones.set_coordinador(self.coordinador)
        self.hide()
        ventana_opciones.show()
    
    def buscar(self):
        nombre=self.nombre.text()
        resultado_validacion=self.coordinador.buscar(nombre)
        if resultado_validacion == False:
            QMessageBox.information(self,"" ,"¡No hay ningún paciente que coincida!")
        else:
            self.info.setText(str(resultado_validacion))

class VentanaEliminar(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("borrar_paciente.ui",self)
        self.setup()
    
    def setup(self):
        self.BORRAR.clicked.connect(self.validar)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def abrirOpciones(self):
        ventana_opciones= Opciones(self)
        ventana_opciones.set_coordinador(self.coordinador)
        self.hide()
        ventana_opciones.show()
    
    def validar(self):
        ide=self.ide.text()
        resultado_validacion=self.coordinador.eliminar(ide)
        if resultado_validacion == False:
            QMessageBox.information(self,"" ,"¡Paciente no encontrado!")
        else:
            QMessageBox.information(self,"" ,"¡Paciente eliminado con éxito!")
            self.close()
            self.abrirOpciones()