'''
-----------------------------
 EJERCICIO N°2
 Cómo Python encuentra propiedades y métodos
-----------------------------
'''
class Super:
  def __init__(self, nombre):
    self.nombre = nombre

  def metodo1(self):
    pass

  def __str__(self):
    return "Mi nombre es " + self.nombre + "."

class Sub(Super):
  def __init__(self, nombre):
    super().__init__(nombre)
    super().metodo1()
  
obj = Sub("Andy")
print(obj)

# También puedes utilizar super().__init__(nombre)