from os import system, name
system('cls') if(name == 'nt') else system('clear')

print("Olá Mundo!!!")
nome = input("Informe seu nome: ")
print(f"Olá {nome}!")
