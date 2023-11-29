from os import system, name
system('cls') if(name == 'nt') else system('clear')

print("Estoque Médio")

codigo = input('Informe o código do produto: ')
descricao = input('Informe a descrição do produto: ')
qtdmin = float(input('Informe a quantidade minima: '))
qtdmax = float(input('Informe a quatidade máxima: '))
qtdmed = (qtdmin+qtdmax)/2

print(f'A Quantidade Média é: {qtdmed:.2f}')