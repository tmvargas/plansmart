# sintaxe 
# print (objetos, argumentos)

mensagem = 'Função print()'

nome = input('Digite seu nome: ')

print ('Ola ' + nome + ' Bem vindo')      


nome = 'Maria'
idade = 30
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
print (msg_formatada)

# F string

nome = ('Fábio')
peso = 100.00
msg = ('Olá, meu nome é {nome) e eu pedo {peso} quilos.')


# carctere de escape \t vira espaço
nome = 'João'
idade = 30
print(f'Nome:\t{nome},\t Idade:{idade}')