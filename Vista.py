import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit,QWidget 
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi

class Login(QWidget):
    def __init__(self,ppal=None):
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
            ventanaopciones.show()
            self.hide()
        
    def mensaje(self, message):
        QMessageBox.information(self, "Resultado de Login", message)

class Opciones(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("opciones_usuario.ui",self)
        self.setup()

    def setup(self):
        self.ingresarP.clicked.connect(self.abrirIngresar)
        self.buscarP.clicked.connect(self.abrirBuscar)
        self.eliminarP.clicked.connect(self.abrirEliminar)
    
    def abrirIngresar(self):
        ventana_ingresar= VentanaIngreso(self)
        self.hide()
        ventana_ingresar.show()
    
    def abrirBuscar(self):
        ventana_buscar= VentanaBuscar(self)
        self.hide()
        ventana_buscar.show()
    
    def abrirEliminar(self):
        ventana_eliminar= VentanaEliminar(self)
        self.hide()
        ventana_eliminar.show()

class VentanaIngreso(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("guardar_paciente.ui",self)
        self.setup()
    
    def setup(self):
        self.GUARDAR.clicked.connect(self.validar)
    
    def set_coordinador(self, coordinador):
        self.coordinador = coordinador
    
    def validar(self):
        ide=self.ide.text()
        resultado_validacion=self.coordinador.verificarIde(ide)
        if resultado_validacion == True:
            nombre=self.nombre.text()
            apellido=self.apellido.text()
            edad=self.edad.text()
            ide=self.ide.text()
            self.coordinador.ingresarInfo(nombre,apellido,edad,ide)
        else:
            QMessageBox.information(self, "", resultado_validacion)

class VentanaBuscar(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("buscar_paciente.ui",self)
        self.__ventanaPadre=ppal
        self.setup()
    
    def setup(self):
        self.BUSCAR.clicked.connect(self.buscar)
    
    def buscar(self):
        nombre=self.nombre.text()
        resultado=self.coordinador.buscar(nombre)
        self.mostrar_resultado(resultado)
    
    def mostrar_resultado(self,resultado):
        self.info.setText(resultado)

class VentanaEliminar(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("borrar_paciente.ui",self)
        self.__ventanaPadre=ppal
        self.setup()
    
    def setup(self):
        self.BORRAR.clicked.connect(self.borrar)
    
    def borrar(self):
        ide=self.ide.text()
        self.coordinador.eliminar(ide)
