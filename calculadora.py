
a = float("5")
b =float("3")


class Calculadora: 
 def soma (self, a, b): 
   return a + b 

 def dividir(self, a, b): 
  if b == 0: 
   raise ValueError("Não é possível dividir por zero.") 
  return a / b 

class Calculadora: 
 def __init__(self): 
  self._ultimo_resultado = None # Atributo protegido 
 def soma (self, a, b): 
  self._ultimo_resultado = a + b 
  return self._ultimo_resultado 
 def dividir(self, a, b): 
  if b == 0: 
   raise ValueError("Não é possível dividir por zero.") 
  self._ultimo_resultado = a / b 
  return self._ultimo_resultado 

 def ultimo_resultado (self): 
  return self._ultimo_resultado 

print("Resultado da soma:", Calculadora().soma(a, b))
print("Resultado da divisão:", Calculadora().dividir(a, b))
print("Último resultado:", Calculadora().ultimo_resultado())