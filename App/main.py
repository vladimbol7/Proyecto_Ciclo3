import sys
sys.path.insert(2, 'H:\\MisionTIC\\Ciclo 3\\Proyecto\\Proyecto_Ciclo3\\App\\Modelo')
from AccesoEmpleados import *

Obj1 = AccesoEmpleados()
empleado = Obj1.buscarEmpleado(100000)
lista = Obj1.listarEmpleados()

user = Obj1.iniciarsesion('p@gmail.com', '1010')
print(user)
