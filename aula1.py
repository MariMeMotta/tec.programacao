#desenvolvimento em python
...
#comentário em bloco
...

#def soma(a,b):
#    return a+b
#print("teste")
#print("chamndo a função")

#a=int(input("Digite o primeiro valor: "))
#b=int(input("Digite o segundo valor: "))

#print(soma (a,b))

# Receba valores

###criar uma nova função que recebe a operação:
#1-soma
#2-subtração
#3-multiplicação
#4-divisão
#e recebe também os dois números, devolvendo o resultado da operação
###

#def calculadora(operacao,a,b):
#    if operacao == 1:
 #       return a+b
  #  elif operacao == 2:
   #     return a-b
    #elif operacao == 3:
    #    return a*b
   # elif operacao == 4:
    #     if b==0:
     #       return "Erro: Divisão por zero"
    # else:
      #  return a/b
#operacao = 0
#while operacao <1 or operacao >4: #enquanto for menor que 1 ou maior que 4, vai pedir 
 #   operacao = int(input("Digite a operação desejada (1-soma, 2-subtração, 3-multiplicação, 4-divisão): "))

#a=float(input("Digite o primeiro operando: "))
#b=float(input("Digite o segundo operando: "))

#print(calculadora(operacao,a,b))

#CRIE UMA FUNÇÃO QUE RECEBA UM NÚMERO E 
#  SE ELE É PRIMO OU NÃO, 
# EXIBINDO A MENSAGEM "O NÚMERO XXXX É PRIMO" OU "O NÚMERO XXXX NÃO É PRIMO".



a=int(input("Digite um número para verificar se é primo: "))

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"O número {a} {'é primo' if eh_primo(a) else 'não é primo'}")

#CRIE UMA FUNÇÃO QUE LISTE TODOS OS NÚMEROS PRIMOS ENTRE 1 E 100

def listar_primos(inicio, fim): 
    
    primos = []
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

print("Números primos entre 1 e 100:")
print(listar_primos(1, 100))

