CREATE DATABASE lad_py;
USE lad_py;

CREATE TABLE eleitores (
    id_eleitor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    titulo_eleitor CHAR(12) NOT NULL UNIQUE,
    prefixo_cpf CHAR(4) NOT NULL,
    cpf_cifrado VARCHAR(120) NOT NULL UNIQUE,
    mesario BOOLEAN NOT NULL DEFAULT FALSE,
    chave_acesso_cifrada VARCHAR(120) NOT NULL,
    ja_votou BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE partidos (
    id_partido INT AUTO_INCREMENT PRIMARY KEY,
    partido VARCHAR(50) NOT NULL,
    sigla VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE candidatos (
    id_candidato INT AUTO_INCREMENT PRIMARY KEY,
    candidato VARCHAR(100) NOT NULL,
    numero_votacao INT NOT NULL UNIQUE,
    id_partido INT NOT NULL,
    FOREIGN KEY (id_partido) REFERENCES partidos(id_partido)
);

CREATE TABLE votos (
    id_voto INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    voto_nulo BOOLEAN NOT NULL DEFAULT FALSE,
    protocolo_votacao_cifrado VARCHAR(120) NOT NULL UNIQUE,
    datetime_voto DATETIME NOT NULL,
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato)
);