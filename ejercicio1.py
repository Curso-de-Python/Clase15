'''
-----------------------------
 EJERCICIO N°1
 Funciones de Herencia
-----------------------------
'''
class Vehiculo:
  pass

class VehiculoTerrestre(Vehiculo):
  pass

class VehiculoOruga(VehiculoTerrestre):
  pass

'''
# issubclass()
for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
  for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    print(issubclass(cls1, cls2), end="\t")
  print()

# isinstance()
miVehiculo = Vehiculo()
miVehiculoTerrestre = VehiculoTerrestre()
miVehiculoOruga = VehiculoOruga()

for obj in [miVehiculo, miVehiculoTerrestre, miVehiculoOruga]:
  for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    print(isinstance(obj, cls), end="\t")
  print()
  
'''
# is
class ClaseMuestra:
  def __init__(self, val):
    self.val = val

ob1 = ClaseMuestra(0)
ob2 = ClaseMuestra(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary tenía un "   # Otro experimento
str2 = "Mary tenía un corderito"
str1 += "corderito"

l1 = [0,1]
l2 = l1
print(l1 is l2)