def minha_funcao():
    print("Essa é minha função!")

minha_funcao()

####################################################
idade = 34
def minha_funcao():
    nome = "Marina"
    print(f"Essa é minha função: {nome}! Sua idade é: {idade}")

#####################################################

def somar(n1, n2): #parametros
    resultado = n1 + n2
    print(f"O resultado da soma entre {n1} e {n2} é: {resultado}")

def somar(n1, n2): #parametros
        resultado = n1 + n2
        return resultado #aplica o valor dela para a varíavel resultado_da_soma
    
resultado_da_soma = somar(10, 5) #argumentos
print(f"O resultado da soma entre 10 e 5 é: {resultado_da_soma}")

#########################################################################

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")

###########################################################################

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
######################################################################

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

########################################################################

def calcular_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / qtd
    return media

resultado = calcular_media(10, 20, 30, 40, 50)
print(f"A média dos números é: {resultado}")

######################################################################

def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado
soma_da_lista = somar_lista(1, 2, 3, 4, 5)
print(f"A soma da lista é: {soma_da_lista}")

#########################################################################

def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

informacoes_pessoais(nome="Marina", idade=34, cidade="São Paulo")

#######################################################################

def contagem_regressiva(numero):
    while True:
        print(numero)
        numero -= 1
        if numero < 0:
            break
contagem_regressiva(10)


######################################################################

def contagem_regressiva(numero):
    for i in range(numero, -1, -1):
        print(i)

contagem_regressiva(10)

#########################################################
def maior_numero(lista_de_numeros):
    maior = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero > maior:
            maior = numero
    return maior
lista = [10, 5, 8, 20, 15]
maior_num = maior_numero(lista)
print(f"O maior número da lista é: {maior_num}")

#########################################################

def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

###################################################################

