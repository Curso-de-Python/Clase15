'''
-----------------------------
 EJERCICIO N°6
 Overriding o anulación
-----------------------------
'''
# HERENCIA ÚNICA
class Nivel1:
  var = 100
  def fun(self):
    return 101

class Nivel2(Nivel1):
  def fun(self):
    return 201

obj = Nivel2()
print(obj.var, obj.fun())

'''
# HERENCIA MÚLTIPLE
class Izquierda:
  var = "I"
  varIzquierda = "II"
  def fun(self):
    return "Izquierda"

class Derecha:
  var = "D"
  varDerecha = "DD"
  def fun(self):
    return "Derecha"

class Sub(Derecha, Izquierda):
  pass

obj = Sub()
print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())
'''