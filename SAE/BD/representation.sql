Drop Table Necessite_nutriment;
Drop Table Necessite_eau;
Drop Table Stocker;
Drop Table Situer;
Drop Table Plante;
Drop Table Remplacer;
Drop Table Espece;
Drop Table Famille;
Drop Table Fiche_d_arrosage;
Drop Table Jardin_botanique;
Drop Table Organisme;
Drop Table Nutriment;
Drop Table Emplacement;
Drop Table Reserve_botanique;
Drop Table Foret_protegee;






CREATE TABLE Emplacement (
  PRIMARY KEY (code_emplacement,code_reserve),
  code_emplacement  VARCHAR(42) NOT NULL,
  place_disponible  VARCHAR(42),
  fiche_information VARCHAR(42),
  code_reserve      VARCHAR(42) NOT NULL,
  situation         VARCHAR(42)
);

CREATE TABLE Espece (
  PRIMARY KEY (code_espece),
  code_espece          VARCHAR(42) NOT NULL,
  nom_scientifique     VARCHAR(42),
  nom_vulgaire         VARCHAR(42),
  description          VARCHAR(42),
  zones_geographiques  VARCHAR(42),
  nom_famille          VARCHAR(42) NOT NULL,
  code_fiche           VARCHAR(42) NOT NULL,
  quantite_eau_semaine NUMBER
);

CREATE TABLE Famille (
  PRIMARY KEY (nom_famille),
  nom_famille VARCHAR(42) NOT NULL,
  description VARCHAR(42)
);

CREATE TABLE Fiche_d_arrosage (
  PRIMARY KEY (code_fiche),
  code_fiche              VARCHAR(42) NOT NULL,
  mode_arrosage           VARCHAR(42),
  ajustements_saisonniers VARCHAR(42)
);

CREATE TABLE Foret_protegee (
  PRIMARY KEY (code_foret),
  code_foret VARCHAR(42) NOT NULL,
  superficie VARCHAR(42)
);

CREATE TABLE Jardin_botanique (
  PRIMARY KEY (code_jardin),
  code_jardin   VARCHAR(42) NOT NULL,
  description   VARCHAR(42),
  nom_organisme VARCHAR(42) NOT NULL,
  code_foret    VARCHAR(42) NULL,
  code_reserve  VARCHAR(42) NULL,
  type_reserve  VARCHAR(42),
  UNIQUE (code_foret)
);

CREATE TABLE Nutriment (
  PRIMARY KEY (code_nutriment),
  code_nutriment    VARCHAR(42) NOT NULL,
  nom               VARCHAR(42),
  formule_chimique  VARCHAR(42),
  type              VARCHAR(42),
  code_nutriment_2  VARCHAR(42) NOT NULL,
  taux_remplacement VARCHAR(42)
);

CREATE TABLE Necessite_nutriment (
  PRIMARY KEY (code_espece, code_nutriment),
  code_espece             VARCHAR(42) NOT NULL,
  code_nutriment          VARCHAR(42) NOT NULL,
  quantite_nutriment_jour NUMBER
);



CREATE TABLE Organisme (
  PRIMARY KEY (nom_organisme),
  nom_organisme     VARCHAR(42) NOT NULL,
  adresse_organisme VARCHAR(42),
  contact_organisme VARCHAR(42)
);

CREATE TABLE Plante (
  PRIMARY KEY (code_plante),
  code_plante       VARCHAR(42) NOT NULL,
  nom_vulgaire      VARCHAR(42),
  nom_scientifique  VARCHAR(42),
  date_plantation   DATE,
  couleur           VARCHAR(42),
  hauteur           VARCHAR(42),
  zone_d_origine    VARCHAR(42),
  couleur_d_origine VARCHAR(42),
  remarque          VARCHAR(42),
  code_emplacement  VARCHAR(42) NOT NULL,
  code_reserve VARCHAR(50) NOT NULL,
  code_espece       VARCHAR(42) NOT NULL
);

CREATE TABLE Reserve_botanique (
  PRIMARY KEY (code_reserve),
  code_reserve    VARCHAR(42) NOT NULL,
  nom             VARCHAR(42),
  ville           VARCHAR(42),
  pays            VARCHAR(42),
  telephone       VARCHAR(42),
  email           VARCHAR(42),
  nom_responsable VARCHAR(42)
);

CREATE TABLE Stocker (
  PRIMARY KEY (code_nutriment, code_reserve),
  code_nutriment VARCHAR(42) NOT NULL,
  code_reserve   VARCHAR(42) NOT NULL,
  quantite_stock NUMBER
);

CREATE TABLE Situer (
   PRIMARY KEY (code_reserve, code_emplacement),
   code_reserve VARCHAR(50) NOT NULL,
   code_emplacement VARCHAR(50) NOT NULL,
   situation VARCHAR(100)
);

CREATE TABLE Remplacer(
   taux_remplacement VARCHAR(50),
   code_nutriment VARCHAR(50) PRIMARY KEY
);


CREATE TABLE Necessite_eau (
    PRIMARY KEY (code_espece, code_fiche),
    code_espece VARCHAR(50) NOT NULL,
    code_fiche VARCHAR(50) NOT NULL,
    quantite_eau_semaine NUMBER
);

ALTER TABLE Emplacement ADD FOREIGN KEY (code_reserve) REFERENCES Reserve_botanique (code_reserve) ON DELETE CASCADE;

ALTER TABLE Espece ADD FOREIGN KEY (code_fiche) REFERENCES Fiche_d_arrosage (code_fiche) ON DELETE CASCADE;
ALTER TABLE Espece ADD FOREIGN KEY (nom_famille) REFERENCES Famille (nom_famille) ON DELETE CASCADE;

ALTER TABLE Jardin_botanique ADD FOREIGN KEY (code_reserve) REFERENCES Reserve_botanique (code_reserve) ON DELETE CASCADE;
ALTER TABLE Jardin_botanique ADD FOREIGN KEY (code_foret) REFERENCES Foret_protegee (code_foret) ON DELETE CASCADE;
ALTER TABLE Jardin_botanique ADD FOREIGN KEY (nom_organisme) REFERENCES Organisme (nom_organisme) ON DELETE CASCADE;

ALTER TABLE Necessite_nutriment ADD FOREIGN KEY (code_nutriment) REFERENCES Nutriment (code_nutriment) ON DELETE CASCADE;
ALTER TABLE Necessite_nutriment ADD FOREIGN KEY (code_espece) REFERENCES Espece (code_espece) ON DELETE CASCADE;

ALTER TABLE Nutriment ADD FOREIGN KEY (code_nutriment_2) REFERENCES Nutriment (code_nutriment) ON DELETE CASCADE;

ALTER TABLE Plante ADD FOREIGN KEY (code_espece) REFERENCES Espece (code_espece) ON DELETE CASCADE;
ALTER TABLE Plante ADD FOREIGN KEY (code_emplacement,code_reserve) REFERENCES Emplacement(code_emplacement,code_reserve) ON DELETE CASCADE;


ALTER TABLE Stocker ADD FOREIGN KEY (code_reserve) REFERENCES Reserve_botanique (code_reserve) ON DELETE CASCADE;
ALTER TABLE Stocker ADD FOREIGN KEY (code_nutriment) REFERENCES Nutriment (code_nutriment) ON DELETE CASCADE;

ALTER TABLE Situer ADD FOREIGN KEY (code_reserve) REFERENCES Reserve_botanique(code_reserve) ON DELETE CASCADE;
ALTER TABLE Situer ADD FOREIGN KEY (code_emplacement,code_reserve) REFERENCES Emplacement(code_emplacement,code_reserve) ON DELETE CASCADE;

ALTER TABLE Necessite_eau ADD FOREIGN KEY (code_espece) REFERENCES Espece(code_espece) ON DELETE CASCADE;
ALTER TABLE Necessite_eau ADD FOREIGN KEY (code_fiche) REFERENCES Fiche_d_arrosage(code_fiche) ON DELETE CASCADE;

ALTER TABLE Remplacer ADD FOREIGN KEY (code_nutriment) REFERENCES Nutriment(code_nutriment) ON DELETE CASCADE;