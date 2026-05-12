def gerar_protocolo(candidato):

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    letra1 = random.choice(letras) # Gera letra Ateatoria
    letra2 = random.choice(letras) # Gera letra Ateatoria

    numeros = random.randint(10000, 99999)

    protocolo = "V" + letra1 + letra2 + "26" + str(candidato) + str(numeros)

    return protocolo


#====QUANDO O VOTO FOR CONCLUIDO
candidato = int(input("\nDigite o numero do candidato: "))

    print("\nConfirmando voto...")

    time.sleep(2)

    protocolo = gerar_protocolo(candidato)

    salvar_protocolo(protocolo)

    print("\nVoto realizado com sucesso.")

    print("\nSeu protocolo de votacao:")
    print(protocolo)
