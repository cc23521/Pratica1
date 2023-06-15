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
        check (semestreAtual >= 1 and semestreAtual <= 10),
    diasAusente tinyint default 0
        check (diasAusente > 0 and diasAusente <= 31),
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

create table timeB.Veiculo
(
    idVeiculo smallint identity,
    RA char(6) not null,
    placa char(7) not null,
    marca varchar(10) not null,
    modelo varchar(10) not null,
    cor varchar(10) not null

    primary key (idVeiculo),
    foreign key (RA)
        references timeB.Estudante (RA)
);

create table timeB.Correspondencia
(
    idCorrespondencia int identity,
    RA char(6) not null,
    recebimento datetime not null,
    retirada datetime default null

    primary key (idCorrespondencia),
    foreign key (RA)
        references timeB.Estudante (RA)
);
