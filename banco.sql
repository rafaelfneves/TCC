/* ============ [CATADORES] ============ */

CREATE TABLE CATADORES (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100),
    data_nascimento DATE,
    endereco VARCHAR(255),
    cidade VARCHAR(100),
    estado VARCHAR(50),
    telefone VARCHAR(20),
    email VARCHAR(100),
    experiencia_anos INT,
    area_atuacao VARCHAR(100),
    capacidade_carga_kg NUMERIC(10, 2)
);

/* ============ [CONQUISTAS] ============ */

CREATE TABLE CONQUISTAS (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    requerimento VARCHAR(255) NOT NULL,
    pontos INT NOT NULL
);

/* ============ [EMPRESAS] ============ */

CREATE TABLE EMPRESAS (
    cnpj VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    email VARCHAR(100),
    telefone VARCHAR(20)
);

/* ============ [MATERIAIS SUSTENTÁVEIS] ============ */

CREATE TABLE MATERIAIS (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    categoria VARCHAR(50),
    peso_medio_gramas INT,
    valor_venda DECIMAL(10, 2)
);
/* ============[VEICULOS] ============ */

CREATE TABLE VEICULOS (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    ano INT,
    placa VARCHAR(10),
    fk_catadores INT,
    FOREIGN KEY (fk_catadores) REFERENCES CATADORES(id)
);

/* ============ [VOUCHERS] ============ */

CREATE TABLE VOUCHERS (
    id SERIAL PRIMARY KEY,
    fk_conquistas INT,
    fk_empresas VARCHAR(14),
    fk_catadores INT,
    codigo VARCHAR(256) NOT NULL,
    FOREIGN KEY (fk_conquistas) REFERENCES CONQUISTAS(id),
    FOREIGN KEY (fk_empresas) REFERENCES EMPRESAS(cnpj),
    FOREIGN KEY (fk_catadores) REFERENCES CATADORES(id)
);
