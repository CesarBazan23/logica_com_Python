from os import system, name
system('cls') if(name == 'nt') else system('clear')
print("Média Aritmética")
n1 =float(input("Informe a 1º nota: "))
n2 =float(input("Informe a 2º nota: "))
n3 =float(input("Informe a 3º nota: "))
n4 =float(input("Informe a 4º nota: "))
media=(n1+n2+n3+n4)/4
print(f"A média de: {n1} | {n2} | {n3} | {n4}:{media:.2f}")