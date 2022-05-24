-- criar as seguintes tabelas para 
-- rodar o programa em python

create table doador(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(56) NOT NULL,
	idade INT,
	sexo VARCHAR(56),
	tipo_sangue VARCHAR(56) NOT NULL
);

create table receptor(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(56) NOT NULL,
	idade INT,
	sexo VARCHAR(56),
	tipo_sangue VARCHAR(56) NOT NULL
);

create table sangue(
	fk_doadorId INT NOT NULL,
	fk_receptorId INT NOT NULL,
	FOREIGN KEY (fk_doadorId) REFERENCES doador(id),
	FOREIGN KEY (fk_receptorId) REFERENCES receptor(id)
);

create table banco_sangue(
	fk_hospitalId INT NOT NULL,
	quantidade INT,
	FOREIGN KEY (fk_hospitalId) REFERENCES hospital(id)
);
create table hospital(
	id INT PRIMARY KEY AUTO_INCREMENT,
	alas INT,
	funcionarios INT,
	nome VARCHAR(56)
);

create table enfermeiro(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cpf INT NOT NULL,
	fk_hospitalId INT NOT NULL,
	nome VARCHAR(56) NOT NULL,
	FOREIGN KEY (fk_hospitalId) REFERENCES hospital(id)
);

create table gestor_hospital(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cpf INT NOT NULL,
	fk_hospitalId INT NOT NULL,
	nome VARCHAR(56) NOT NULL,
	FOREIGN KEY (fk_hospitalId) REFERENCES hospital(id)
);