/* ============ [ROLES] ============ */
CREATE TABLE Roles (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

/* ============ [CATEGORIES] ============ */
CREATE TABLE Categories (
    id serial PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

/* ============ [USERS] ============ */
CREATE TABLE Users (
    cpf_login VARCHAR(11) PRIMARY KEY,
    password_hash VARCHAR(255) NOT NULL,
    role INT NOT NULL CHECK (role IN (0, 1))
);

/* ============ [BRANDS] ============ */
CREATE TABLE Brands (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(255) NOT NULL
);

/* ============ [MATERIALS] ============ */
CREATE TABLE Materials (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    fk_categories INT REFERENCES Categories(id)
);

/* ============ [INVENTORIES] ============ */
CREATE TABLE Inventories (
    id SERIAL PRIMARY KEY,
    material_name VARCHAR(255) NOT NULL,
    weight_grams FLOAT NOT NULL,
    fk_materials INT REFERENCES Materials(id)
);

/* ============ [COLLECTORS] ============ */
CREATE TABLE Collectors (
    cpf VARCHAR(11) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    birth_date DATE,
    phone VARCHAR(20),
    email VARCHAR(255) UNIQUE NOT NULL,
    years_of_experience INT,
    working_area VARCHAR(255)
);

/* ============ [VEHICLES] ============ */
CREATE TABLE Vehicles (
    id SERIAL PRIMARY KEY,
    model VARCHAR(255) NOT NULL,
    year INT,
    plate VARCHAR(20),
    fk_collector VARCHAR(11) REFERENCES Collectors(cpf),
    capacity_kg FLOAT
);

/* ============ [ADDRESSES] ============ */
CREATE TABLE Addresses (
    id SERIAL PRIMARY KEY,
    entity_id INT NOT NULL,
    entity_type VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    number VARCHAR(20),
    complement VARCHAR(255),
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    zip_code VARCHAR(20) NOT NULL
);

/* ============ [VOUCHERS] ============ */
CREATE TABLE Vouchers (
    cod_voucher SERIAL PRIMARY KEY,
    fk_achievements INT REFERENCES Achievements(id),
    fk_companies VARCHAR(14) REFERENCES Companies(cnpj)
);

/* ============ [ACHIEVEMENTS] ============ */
CREATE TABLE Achievements (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    requirement VARCHAR(255),
    points INT NOT NULL,
    fk_collector VARCHAR(11) REFERENCES Collectors(cpf)
);

/* ============ [COMPANIES] ============ */
CREATE TABLE Companies (
    cnpj VARCHAR(14) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20)
);