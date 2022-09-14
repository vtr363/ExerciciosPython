create table AUTOR (
	Matricula int PRIMARY KEY CHECK (Matricula < 1000),
	Nome varchar(80) NOT NULL,
	CPF char(11) unique NOT NULL,
	Endereço varchar(80),
	DataNasc date NOT NULL,
	Nacionalidade varchar(30) NOT NULL
)

create table EDITORA (
	Editora INT PRIMARY KEY NOT NULL,
	Nome VARCHAR(80) NOT NULL
)

ALTER TABLE EDITORA ADD CONSTRAINT ck_editora CHECK (Editora < 1000)

create table LIVRO (
	Codigo int PRIMARY KEY CHECK (Codigo < 1000),
	Titulo varchar(80) NOT NULL,
	Preço real,
	Lançamento date, 
	Assunto varchar(50),
	Cod_editora int CHECK (Cod_editora < 1000) FOREIGN KEY REFERENCES EDITORA(Editora) ON DELETE CASCADE
)

create table AUTOR_LIVRO (
	Cod_livro int FOREIGN KEY REFERENCES LIVRO(Codigo) ON DELETE CASCADE,
	Cod_autor int FOREIGN KEY REFERENCES AUTOR(Matricula) ON DELETE CASCADE,

)

ALTER TABLE AUTOR_LIVRO ADD CONSTRAINT ck_livro CHECK (Cod_livro < 1000)
ALTER TABLE AUTOR_LIVRO ADD CONSTRAINT ck_autor CHECK (Cod_autor < 1000)

ALTER TABLE LIVRO ADD Edicao INT 
ALTER TABLE LIVRO ADD CONSTRAINT ck_edicao CHECK (Edicao < 20)

ALTER TABLE LIVRO DROP CONSTRAINT ck_edicao
ALTER TABLE LIVRO DROP COLUMN Edicao

--  DROP
ALTER TABLE AUTOR_LIVRO DROP CONSTRAINT ck_livro 
ALTER TABLE AUTOR_LIVRO DROP CONSTRAINT ck_autor
DROP TABLE AUTOR_LIVRO
DROP TABLE LIVRO
ALTER TABLE LIVRO DROP CONSTRAINT ck_editora
DROP TABLE EDITORA 

-- create
create table EDITORA (
	Editora INT PRIMARY KEY NOT NULL,
	Nome VARCHAR(80) NOT NULL,
    Edicao int 
)

ALTER TABLE EDITORA ADD CONSTRAINT ck_edicao check (Edicao < 20)
ALTER TABLE EDITORA ADD CONSTRAINT ck_editora CHECK (Editora < 1000)

create table LIVRO (
	Codigo int PRIMARY KEY CHECK (Codigo < 1000),
	Titulo varchar(80) NOT NULL,
	Preço real,
	Lançamento date, 
	Assunto varchar(50),
	Cod_editora int CHECK (Cod_editora < 1000) FOREIGN KEY REFERENCES EDITORA(Editora) ON DELETE CASCADE
)

create table AUTOR_LIVRO (
	Cod_livro int FOREIGN KEY REFERENCES LIVRO(Codigo) ON DELETE CASCADE,
	Cod_autor int FOREIGN KEY REFERENCES AUTOR(Matricula) ON DELETE CASCADE,

)

ALTER TABLE AUTOR_LIVRO ADD CONSTRAINT ck_livro CHECK (Cod_livro < 1000)
ALTER TABLE AUTOR_LIVRO ADD CONSTRAINT ck_autor CHECK (Cod_autor < 1000)

-- inserts
INSERT INTO EDITORA VALUES 
(001, 'Addison', 1), 
(002, 'Globo',1), 
(003, 'Pearson',2),
(004, 'Abril',10)

INSERT INTO AUTOR VALUES
(911, 'Roberto', '12345678901', 'Rua A num 1', '1966-09-18', 'Brasileira')
(922, 'Simone', '22345678901', 'Rua B num 1', '1976-08-08', 'Brasileira')
(933, 'Fernando', '32345678901', 'Rua C num 1', '1996-07-13', 'Brasileira')
(954, 'Felipe', '42345678901', 'Rua D num 1', '1967-02-28', 'Brasileira')
(965, 'Fabio', '52345678901', 'Rua E num 1', '1988-03-08', 'Brasileira')
(976, 'Fernanda', '62345678901', 'Rua E num 1', '1988-03-08', 'Brasileira')
(997, 'Julio', '22345678901', 'Rua E num 1', '1988-03-08', 'Brasileira')
(1001, 'Dario', '21345678901', 'Rua E num 1', '1998-03-08', 'Brasileira')
-- formato errado das datas
-- cpfs duplicados
-- matricula maior que 1000

INSERT INTO LIVRO VALUES
<100; Sistemas de Banco de Dados; 99,00; 01/01/2015; Informática; 003>
<200; Rede de Computadores; 199,00; 01/05/2002; Informática; 003>
<300; Corpo Humano; 89,00; 01/09/2011; Medicina; 004>
<400; Leis da Física; 95,00; 01/10/2015; Ciência; 002>
<500; Física Quântica; 95,00; 01/10/2015; Ciência; 005>
<300; O Coração; 289,00; 01/09/1999; Medicina; 004>

INSERT INTO AUTOR_LIVRO VALUES
Roberto é autor de “Sistemas de Banco de Dados”
Fabio é autor de “O Coração”
Felipe é autor de “Sistemas de Banco de Dados”
Fernando é autor de “Redes de Computadores”
Roberto é autor de “Redes de Computadores”
Simone é autor de “Corpo Humano”
Fernanda é autor de “Leis da Física”
Fernanda é autor de “Física Quantica”
Fabio é autor de “Corpo Humano”
