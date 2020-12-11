'''
-----------------------------
 EJERCICIO N°3
 Probando la herencia con propiedades
-----------------------------
'''
# Variables de clase
class Super:
  supVar = 1

class Sub(Super):
  subVar = 2

obj = Sub()
print(obj.subVar)
print(obj.supVar)

'''
# Variables de instancia
class Super:
  variableClase1 = 0  # Variable de clase

  def __init__(self):   # Constructor
    self.supVar = 11    # Variable de instancia

  def metodo1(self):    # Método cualquiera
    print("soy un metodo!") 

class Sub(Super):
  def __init__(self):
    super().__init__() super().__init__()
    self.subVar = 12

obj = Sub()
print(obj.subVar)
print(obj.variableClase1)
print(obj.supVar)   # No se ha inicializado el constructor!
print(obj.metodo1())
'''