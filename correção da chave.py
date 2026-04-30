import random

nome = input("Digite seu nome completo: ")

letras = nome[:2]# as 2 primeiras letras do nome

for i in range(len(nome)):
    if nome[i] == " ":
        letras += nome[i + 1]# soma as 2 primeiras letras,pula o espaço e junta a primeira letra do sobrenome depois do i espaço
     
chave = letras.upper() + f"{random.randint(1000, 9999)}"

print("Sua chave é:", chave)
