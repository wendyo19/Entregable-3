#Controlador
from Modelo import *
from Vista import VentanaPpal
from PyQt5.QtWidgets import QApplication
import sys 


class Coordinador:
    def __init__(self,vista,modelo):
        self.__miVista = vista
        self.__miModelo = modelo
    
    def validar(self,usuario,contraseña):
        resultado=self.__miModelo.Validar_usuario(usuario,contraseña)
        self.__miVista.mensaje(resultado)
        return resultado 
    
    def ingresarInfo(self,a,b,c,d):
        self.__miModelo.agregar_paciente(a,b,c,d)

    def verificarIde(self,IDE):
        resultado=self.__miModelo.verificar_existencia(IDE)
        self.__miVista.validar(resultado)
        return
    
    def buscar(self,nombre):
        self.__miModelo.buscar_paciente(nombre)
    
    def eliminar(self,IDE):
        self.__miModelo.eliminar_paciente(IDE)
    
def main():
    app=QApplication(sys.argv)
    vista=Login()
    modelo=Paciente("e","e","e","e")
    coordinador= Coordinador(vista,modelo)
    vista.set_coordinador(coordinador)
    vista.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()