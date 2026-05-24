"""TABELA PARA VISUALIZACAO DO PROTOCOLO NO BANCO DE DADOS"""
CREATE TABLE protocolos (
    id_protocolo INT AUTO_INCREMENT PRIMARY KEY,
    protocolo VARCHAR(100) NOT NULL,
    tipo_voto VARCHAR(20),
   horario_voto DATETIME DEFAULT CURRENT_TIMESTAMP
);


       """COMANDO 3 PARA (CANDIDATO)"""
protocolo = gerar_protocolo(numero_candidatoB)
protocolo_cifrado = criptografar_hill(protocolo)
salvar_protocolo(protocolo)

comando_3 = """
INSERT INTO protocolos (protocolo, tipo_voto,horario_voto)
VALUES (%s, %s , %s)
"""
valores_3 = (protocolo_cifrado, "VOTO PARA CANDIDATO",horario_voto)
executar(comando_3, valores_3)

print(f"\nPROTOCOLO DO VOTO: {protocolo}")

print(f"Voto registrado no candidato: {resultado[0]} com sucesso!")

         
parte_final = 1

registrar_log(f"ALERTA: Atualizaçao de voto realizado em eleitores para realizado VOTO PARA CANDIDATO(ja_votou=1) no Banco de Dados.")         
registrar_log(f"SUCESSO: Voto realizado com sucesso para candidato {resultado[0]}")


         
       """COMANDO 3 PARA (VOTO NULO)"""

protocolo = gerar_protocolo("NULO")
protocolo_cifrado = criptografar_hill(protocolo)
salvar_protocolo(protocolo)

comando_3 = """
INSERT INTO protocolos (protocolo, tipo_voto,horario_voto)
VALUES (%s, %s , %s)
"""
valores_3 = (protocolo_cifrado, "VOTO NULO",horario_voto)
executar(comando_3, valores_3)

print(f"\nPROTOCOLO DO VOTO: {protocolo}")

print(f"Voto Nulo registrado com sucesso!")

         
parte_final = 1

         
registrar_log(f"ALERTA: Atualizaçao de voto realizado para VOTO NULO(voto_nulo=1)no Banco de Dados.")
registrar_log("SUCESSO: Voto nulo registrado com sucesso.")

