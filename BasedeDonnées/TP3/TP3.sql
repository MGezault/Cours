-- @ SCRIPTS/CreateANDDropTables-Voyages
-- @ SCRIPTS/instanceVOYAGES

drop table RESERVATIONS;
drop table CLIENTS;
drop table VOYAGES;

create table CLIENTS 
(Id Number(4)  primary key, 
Nom VarChar2(20),  
Prenom  VarChar2(20),
Ville Varchar2(20));

create table VOYAGES
(Code Varchar2(6) primary key,
VilleDepart VarChar2(30),
VilleArrivee VarChar2(30),
Depart Date,
Retour Date,
Prix Number(8,2));


create table RESERVATIONS (
Id Number(4) , 
Code Varchar2(6),
DateReserv Date,
foreign key (Id) references CLIENTS(Id) on delete cascade,
foreign key (Code) references VOYAGES (Code) on delete cascade);

insert into Clients values ( 1, 'Dupont', 'Jean', 'Orleans');
insert into Clients values ( 2, 'Durand', 'Paul', 'Orleans');
insert into Clients values ( 3, 'Martin', 'Pierre', 'Paris');
insert into Clients values ( 4, 'Auger', 'Marcel', 'Paris');
insert into Clients values ( 5, 'Smith', 'Peter', 'Londres');
insert into Clients values ( 6, 'Barnes', 'Jane', 'Berlin');
insert into Clients values ( 7, 'Freud', 'Florian', 'Berlin');

insert into Voyages values ('V100', 'Paris', 'Amsterdam',  to_date('01-08-2019-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-08-2019-14:30','DD-MM-YYYY-HH24:MI'),200.00);
insert into Voyages values ('V200', 'Paris', 'Rio de Janeiro',  to_date('01-12-2019-11:30','DD-MM-YYYY-HH24:MI'), to_date('07-12-2019-16:30','DD-MM-YYYY-HH24:MI'),2000.00);
insert into Voyages values ('V300', 'Prague', 'Amsterdam',  to_date('01-10-2019-8:30','DD-MM-YYYY-HH24:MI'), to_date('10-08-2019-15:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V140', 'Paris', 'Amsterdam',  to_date('01-11-2019-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-11-2019-14:30','DD-MM-YYYY-HH24:MI'),100.00);
insert into Voyages values ('V400', 'Lisbonne', 'Madrid',  to_date('01-03-2020-12:30','DD-MM-YYYY-HH24:MI'), to_date('07-03-2020-18:30','DD-MM-YYYY-HH24:MI'),400.00);
insert into Voyages values ('V500', 'Paris', 'Madrid',  to_date('01-04-2020-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-04-2020-20:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V600', 'Berlin', 'Madrid',  to_date('01-05-2020-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-05-2020-20:30','DD-MM-YYYY-HH24:MI'),300.00);


insert into Reservations values (6, 'V100', to_date('01-07-2019-18:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V100', to_date('01-06-2019-8:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V200', to_date('01-05-2019-21:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V400', to_date('01-11-2019-18:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (2, 'V400', to_date('01-11-2019-21:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V140', to_date('01-06-2019-9:25','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (4, 'V300', to_date('01-05-2019-12:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V100', to_date('01-05-2019-19:25','DD-MM-YYYY-HH24:MI'));

SET LINESIZE 500; 

-- requete SQL DU TP 3 : 

-- 1 ) 

SELECT DISTINCT VilleArrivee FROM VOYAGES WHERE VilleDepart = 'Paris';

-- 2 ) 

SELECT * FROM VOYAGES WHERE VilleArrivee = 'Amsterdam';

-- 3 ) 

SELECT to_char(depart,'dd-mm-yy') jourdepart, to_char (depart,'hh24:mi') heureDepart

-- 4 ) 

SELECT Nom, Prenom, VilleArrivee, Prix FROM CLIENTS
NATURAL JOIN RESERVATIONS NATURAL JOIN VOYAGES ORDER BY Nom ASC, Prix DESC;


-- 5 ) 

SELECT Nom, VilleDepart, Coden FROM CLIENTS
NATURAL JOIN RESERVATIONS NATURAL JOIN VOYAGES WHERE Ville = VilleDepart;

-- 6 ) 


-- 7 ) 
SELECT VilleDepart, VilleArrivee, TO_CHAR(Depart, 'dd-mm-yy') AS JDepart, TO_CHAR(Depart, 'HH24:MI') AS HDepart
FROM VOYAGES 
WHERE (Depart - SYSDATE) / 30 > 3
ORDER BY Depart ASC;

-- 8 )

select villeArrive,Villes
from VOYAGES
union
select villeDepart,VIlles
from VOYAGES;

-- 9 )

SELECT * from clients where ville != 'Paris';

-- 10 )

(Select Id,Prenom,Nom 
from Clients NATURAL join reservations natural join Voyages
where VilleDepart = 'Paris')
minus
(select Id, Prenom, Nom
from Clients
where Ville='Paris');
-- 11 )

(SELECT id
from CLIENTS)
minus
(select id 
from Reservations);

-- 12 ) 
(select Code 
from Voyages)
minus
(Select code 
from Reservations);

-- 13 ) 

(select id 
from Clients)
minus
(select id 
from Voyages Natural join Reservations
where VilleArrivee = 'Amsterdam' and VilleDepart ='Paris');