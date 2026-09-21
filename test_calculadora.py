

from os import name
import unittest 
from calculadora import Calculadora 
class TestCalculadora (unittest.TestCase): 

 def test_soma_dois_numeros_positivos (self): 
  calc = Calculadora() 
# O assert é a nossa expectativa: esperamos que 2 + 3 seja 5 self.assertEqual(calc.soma (2, 3), 5) 
if name == "__main__": 
 unittest.main()

def test_divisao_por_zero_deve_lancar_erro(self): 
 calc = Calculadora() 
# Verificamos se o código levanta a exceção correta with self.assertRaises (ValueError): 
 calc.dividir (10, 0)

#Novo Teste
def test_deve_armazenar_ultimo_resultado(self): 
 calc = Calculadora() 
 calc.soma (10, 5) 
 self.assertEqual(calc.ultimo_resultado, 15) 
