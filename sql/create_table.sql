create schema timeB;

create table timeB.Imovel
(
    idImovel smallint identity,
    bloco char(1) not null,
    vagas tinyint default 4 
	check (vagas >= 0 and vagas <= 4)

    primary key (idImovel)
);

create table timeB.Estudante
(
    RA char(6) not null,
    email varchar(50) not null,
    nomeSocial varchar(80) default '',
    semestreAtual tinyint default 1
        check (semestreAtual <= 10),
    diasAusente tinyint default 0
        check (diasAusente <= 31),
    idImovel smallint not null

    primary key (RA),
    foreign key (idImovel)
        references timeB.Imovel (idImovel) 
);

create table timeB.Apontamento
(
    idApontamento int identity,
    RA char(6) not null,
    entrada datetime not null,
    saída datetime default null

    primary key (idApontamento),
    foreign key (RA)
        references timeB.Estudante (RA)
);