create schema timeB;

create table timeB.Imovel
(
    idImovel smallint identity,
    bloco char(1) not null,
    vagas tinyint default 4 not null

    primary key (idImovel)
);

create table timeB.Estudante
(
    idEstudante smallint identity not null,
    RA char(6) not null,
    email varchar(50) not null,
    nomeSocial varchar(80) default null,
    semestreAtual tinyint default 1
        check (semestreAtual >= 1 and semestreAtual <= 10),
    diasAusente tinyint default 0
        check (diasAusente > 0 and diasAusente <= 31),
    idImovel smallint not null

    primary key (idEstudante),
    foreign key (idImovel)
        references timeB.Imovel (idImovel) 
);

create table timeB.Apontamento
(
    idApontamento int identity not null,
    idEstudante smallint not null,
    entrada datetime not null,
    saída datetime default null

    primary key (idApontamento),
    foreign key (idEstudante)
        references timeB.Estudante (idEstudante)
);

create table timeB.Veiculo
(
    idVeiculo smallint identity not null,
    idEstudante smallint not null,
    placa char(7) not null,
    marca varchar(10) not null,
    modelo varchar(10) not null,
    cor varchar(10) not null

    primary key (idVeiculo),
    foreign key (idEstudante)
        references timeB.Estudante (idEstudante)
);

create table timeB.Correspondencia
(
    idCorrespondencia int identity not null,
    idEstudante smallint not null,
    recebimento datetime not null,
    retirada datetime default null

    primary key (idCorrespondencia),
    foreign key (idEstudante)
        references timeB.Estudante (idEstudante)
);