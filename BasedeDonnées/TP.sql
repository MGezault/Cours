drop table FAIRE_PARTIE;
drop table COMPOSER;
drop table COLIS;
drop table COMMANDE;
drop table CLIENT;
drop table ARTICLE;
drop table POINT_DE_DISTRIBUTION;

create table POINT_DE_DISTRIBUTION(
    refPointDD number(5) primary key,
    adressePt Varchar(50)
);

create table CLIENT(
    referenceCL number(5) primary key,
    nomCL VARCHAR(30),
    prenomCL VARCHAR(20),
    telCL number(10),
    adresseCL  VARCHAR(50),
    refPointDD number(5),
    foreign key (refPointDD) references POINT_DE_DISTRIBUTION(refPointDD)
);


create table ARTICLE(
    referenceArt number(5) primary key,
    DesignationArt Varchar(50),
    QuantiteStockArt number(38)
);


create table COMMANDE(
    referenceCom number(5) primary key,
    dateCom Varchar(50),
    montantTotalCom number(38),
    referenceCL number(5),
    foreign key (referenceCL) references CLIENT(referenceCL)
);

create table COLIS(
    numerocolis number(5) primary key,
    indicateurRetraitColis Varchar(50),
    referenceCom number(5),
    foreign key (referenceCom) references COMMANDE(referenceCom)
);

create table FAIRE_PARTIE(
    quantiteCommandee number(38) primary key
);


create table COMPOSER(
    quantiteexp number(38),
    quantiteacceptee number(38)
);


