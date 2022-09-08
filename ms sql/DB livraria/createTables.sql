create table AUTOR (
	Matricula int PRIMARY KEY,
	Nome varchar(80),
	CPF char(11) unique,
	Endereço varchar(80),
	DataNasc date,
	Nacionalidade varchar(30)
)

create table EDITORA (
	Editora int PRIMARY KEY,
	Nome varchar(80) 
)

create table LIVRO (
	Codigo int PRIMARY KEY,
	Titulo varchar(80),
	Preço real,
	Lançamento date, 
	Assunto varchar(50),
	Cod_editora int FOREIGN KEY REFERENCES EDITORA(Editora) ON DELETE CASCADE
)

create table AUTOR_LIVRO (
	Cod_livro int FOREIGN KEY REFERENCES LIVRO(Codigo) ON DELETE CASCADE,
	Cod_autor int FOREIGN KEY REFERENCES AUTOR(Matricula) ON DELETE CASCADE,

)