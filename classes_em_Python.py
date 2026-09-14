#CRIANDO UMA CLASSE PYTHON
class veiculo: #tudo o que for importante para o veiculo vai ficar dentro da classe 
#Método construtor é um método especial que é chamado quando um objeto é criado (instanciado) a partir de uma classe e permite que a classe inicialize os atributos do objeto. Em Python, o método construtor é definido usando o método __init__().
    def __init__(self, marca, modelo, cor, ano): #metodo construtor
        self.marca = marca #dentro da classe tenho o atributo marca e com a presença do self ja tenho o parametro
        self.modelo = modelo #parametros
        self.cor = cor #parametros
        self.ano = ano #parametros
        self.velocidade = 0 #atributo velocidade que inicia com 0, pois todo carro quando é criado ele inicia com 0 de velocidade

#Método das classes são funções que definem o comportamento dos objetos criados a partir da classe. 
    def acelerar(self, velocidade): #metodo acelerar que recebe a velocidade como parametro
        self.velocidade += 1 #sem o _ ele não está protegido, com o _ ele está protegido, com o __ ele está privado

    def obter_velocidade(self): #metodo obter_velocidade que retorna a velocidade do carro
        return self.velocidade #retorna a velocidade do carro

    def frear(self, velocidade): #metodo frear que recebe a velocidade como parametro
        self.velocidade -= velocidade #diminui a velocidade do carro
        if self.velocidade < 0:
            self.velocidade = 0 #não permite que a velocidade seja negativa

class carro(veiculo): #classe carro que herda da classe veiculo
        def __init__(self, marca, modelo, cor, ano, num_portas, volume_porta_mala): #metodo construtor da classe carro que recebe o parametro portas
            super().__init__(marca, modelo, cor, ano) #chama o metodo construtor da classe veiculo
            self.num_portas = num_portas #atributo que não foram definidos na classe veiculo, mas sim na classe carro
            self.volume_porta_mala = volume_porta_mala #atributo volume_porta_mala que recebe o parametro volume_porta_mala

class moto(veiculo): #classe moto que herda da classe veiculo
        def __init__(self, marca, modelo, cor, ano, num_portas, volume_porta_mala): #metodo construtor da classe moto que recebe o parametro tipo_moto
            super().__init__(marca, modelo, cor, ano) #chama o metodo construtor da classe veiculo
            self.num_rodas = 2 #atributo que não foram definidos na classe veiculo, mas sim na classe moto

meu_poize = carro("Volkswagen", "fusca", "preto", 2020, 4, 300) #instanciando a classe carro e passando os parametros   
meu_porshe = carro("Porsche", "911", "vermelho", 2022, 2, 200) #instanciando a classe carro e passando os parametros
meu_harley = moto("Harley-Davidson", "Street 750", "preto", 2021, 2, 100) #instanciando a classe moto e passando os parametros

#Deve chamar esse método do meu  objeto.
print(meu_poize.obter_velocidade()) #chamando o metodo obter_velocidade do objeto meu_poize 

print(meu_porshe.obter_velocidade()) #chamando o metodo obter_velocidade do objeto meu_porshe
while (meu_porshe.velocidade < 150): #enquanto a velocidade do meu_porshe for menor que 150
     meu_porshe.acelerar(150) #chamando o metodo acelerar do objeto meu_porshe

print(meu_harley.obter_velocidade()) #chamando o metodo obter_velocidade do objeto meu_harley

meu_poize.acelerar(10); #chamando o metodo acelerar do objeto meu_poize
print(meu_poize.obter_velocidade()); #chamando o metodo obter_velocidade do objeto meu_poize 
meu_poize.velocidade = 200;
print(meu_poize.obter_velocidade()); #chamando o metodo obter_velocidade do objeto meu_poize

meu_poize.frear(50); #chamando o metodo frear do objeto meu_poize
print(meu_poize.obter_velocidade()); #chamando o metodo obter_velocidade do objeto meu_poize    