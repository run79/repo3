# 1 - Instancie 3 classes diferentes com no mínimo 3 atributos cada e seus respectivos getters e setters.
# class Pessoa(object):
#     def __init__(self, nome, idade, salario):
#         self._nome = nome
#         self._idade = idade
#         self._salario = salario
#     @property
#     def nome(self):
#         print('get do nome')
#         return self._nome
#     @nome.setter
#     def nome(self, nome):
#         print('set do nome', nome)
#         self._nome = nome
#     @property
#     def idade(self):
#         print('get da idade')
#         return self._idade
#     @idade.setter
#     def idade(self, idade):
#         print('set da idade', idade)
#         self._idade = idade
#     @property
#     def salario(self):
#         print('get do salario')
#         return self._salario
#     @salario.setter
#     def salario(self, salario):
#         print('set do salario', salario)
#         self._salario = salario

# pessoa = Pessoa('Alex', 20, 2500)
# print(pessoa.__dict__) # valores iniciais
# pessoa.nome = 'Cristiano'
# pessoa.idade = 20
# pessoa.salario = 2500
# print(pessoa.nome)
# print(pessoa.idade)
# print(pessoa.salario)

# 2 - Faça 3 métodos para cada classe (não precisam ser métodos complexos).
# class gato ():
#     def __init__(self,nome, peso, idade):
#         self.nome= nome
#         self.peso = peso
#         self.idade = idade
#     def brincar (self):
#         print("Estou brincando")
#     def correr (self):
#         print("Estou correndo")
#     def dormir (self):
#         print("Vou dormir")
#     def Exibir_caracteristicas_do_gato(self):
#         print(self.nome, self.peso, self.idade)
        
# gato1 = gato("Snowbell", "2kg", "7meses")
# gato1.brincar()
# gato1.correr()
# gato1.dormir()
# gato1.Exibir_caracteristicas_do_gato()

# 3 - Ao menos 1 método de cada classe deve receber parâmetros digitados pelo usuário (input).
# class gato ():
#     def __init__(self,nome, peso, idade):
#         self.nome = nome
#         self.peso = peso
#         self.idade = idade

# nome = input("Qual o nome do gatinho? ")
# idade = input("Qual a idade do gatinho? ")
# peso = input("Qual o peso do gatinho? ")

# gato = gato(nome,peso,idade)

