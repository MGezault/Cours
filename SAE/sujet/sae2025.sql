-- Devoir 127
-- Nom: CHER , Prenom: Naick

-- Feuille SAE2.05 Exploitation d'une base de données: Livre Express
-- 
-- Veillez à bien répondre aux emplacements indiqués.
-- Seule la première requête est prise en compte.

-- +-----------------------+--
-- * Question 127156 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les livres qui ont été commandés le 1er décembre 2024 ?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------------+--------------------------------------------+---------+-----------+-------+
-- | isbn          | titre                                      | nbpages | datepubli | prix  |
-- +---------------+--------------------------------------------+---------+-----------+-------+
-- | etc...
-- = Reponse question 127156.

Select LIVRE.isbn,LIVRE.titre,LIVRE.nbpages,LIVRE.datepubli,prix
FROM LIVRE 
join DETAILCOMMANDE on DETAILCOMMANDE.isbn = LIVRE.isbn
join COMMANDE on DETAILCOMMANDE.numcom = COMMANDE.numcom
WHERE COMMANDE.datecom = '2024-12-01';



-- +-----------------------+--
-- * Question 127202 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels clients ont commandé des livres de René Goscinny en 2021 ?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+---------+-----------+-----------------------------+------------+-------------+
-- | idcli | nomcli  | prenomcli | adressecli                  | codepostal | villecli    |
-- +-------+---------+-----------+-----------------------------+------------+-------------+
-- | etc...
-- = Reponse question 127202.

Select *
from CLIENT 
where idcli in (
    Select idcli from COMMANDE Where Year(datecom) = '2021' AND numcom in (
        Select numcom from DETAILCOMMANDE where isbn in (
            Select isbn from ECRIRE where idauteur in (Select idauteur from AUTEUR where nomauteur ='René Goscinny'))));





-- +-----------------------+--
-- * Question 127235 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les livres sans auteur et étant en stock dans au moins un magasin en quantité strictement supérieure à 8 ?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------------+-----------------------------------+-------------------------+-----+
-- | isbn          | titre                             | nommag                  | qte |
-- +---------------+-----------------------------------+-------------------------+-----+
-- | etc...
-- = Reponse question 127235.

Select isbn, titre,nommag,qte
FROM LIVRE NATURAL left join ECRIRE NATURAL JOIN POSSEDER NATURAL JOIN MAGASIN 
WHERE idauteur IS NULL AND qte > 8;

-- FAire des jointures left pour ne pas perdre les nulls

-- +-----------------------+--

-- * Question 127279 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque magasin, on veut le nombre de clients qui habitent dans la ville de ce magasin (en affichant les 0)

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-------------------------+-------+
-- | idmag | nommag                  | nbcli |
-- +-------+-------------------------+-------+
-- | etc...
-- = Reponse question 127279.

Select idmag,nommag,count(C.idcli) nbCli
from MAGASIN M left join CLIENT C on M.villemag = C.villecli
where C.villecli = M.villemag
GROUP BY nommag
Order by (idmag);

-- +-----------------------+--
-- * Question 127291 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Pour chaque magasin, on veut la quantité de livres achetés le 15/09/2022 en affichant les 0.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------+------+
-- | nommag                  | nbex |
-- +-------------------------+------+
-- | etc...
-- = Reponse question 127291.


select MAGASIN.nommag, IFNULL(sum(qte),0) nbex
FROM MAGASIN 
LEFT JOIN COMMANDE ON MAGASIN.idmag = COMMANDE.idmag  
LEFT JOIN DETAILCOMMANDE ON COMMANDE.numcom = DETAILCOMMANDE.numcom AND datecom = '2022-09-15'
group by nommag;

-- +-----------------------+--
-- * Question 127314 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Instructions d'insertion dans la base de données

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+
-- | insertions |
-- +------------+
-- | etc...
-- = Reponse question 127314.

insert into LIVRE(isbn, titre,nbpages,datepubli,prix) values
    ('9782844273765','SQL pour les Nuls',292,2002,35.5);

insert into AUTEUR(idauteur, nomauteur,anneenais,anneedeces) values
	('OL246259A', 'Allen G. Taylor', 1945, NULL),
    ('OL7670824A', 'Reinhard Engel', 1957, NULL);

insert into POSSEDER(idmag, isbn, qte) values
    ('7','9782844273765',3);

insert into ECRIRE(isbn,idauteur) values
    ('9782844273765','OL246259A'),
    ('9782844273765','OL7670824A');

insert into EDITEUR(nomedit,idedit) values
    ('First Interactive',240);

insert into EDITER(isbn,idedit) values
    ('9782844273765',240);

insert into THEMES(isbn,iddewey) values
    ('9782844273765',000);

-- +-----------------------+--
-- * Question 127369 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 1 Nombre de livres vendus par magasin et par an

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------+-------+-----+
-- | Magasin                 | Annee | qte |
-- +-------------------------+-------+-----+
-- | etc...
-- = Reponse question 127369.

select M.nommag as Magasin,YEAR(C.datecom) Annee,sum(D.qte) qte
from MAGASIN M NATURAL JOIN COMMANDE C NATURAL JOIN DETAILCOMMANDE D
group by Magasin,Annee;



-- +-----------------------+--
-- * Question 127370 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 2  Chiffre d'affaire par thème en 2024

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------------------------------------+---------+
-- | Theme                                | Montant |
-- +--------------------------------------+---------+
-- | etc...
-- = Reponse question 127370.


Select nomclass as Theme, sum(prixvente*qte) as Montant
from CLASSIFICATION NATURAL JOIN THEMES NATURAL JOIN LIVRE NATURAL JOIN DETAILCOMMANDE NATURAL JOIN COMMANDE
WHERE YEAR(datecom) = '2024'
group by LEFT(iddewey,1);
-- +-----------------------+--
-- * Question 127381 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 3 Evolution chiffre d'affaire par magasin et par mois en 2024

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------+-------------------------+---------+
-- | mois | Magasin                 | CA      |
-- +------+-------------------------+---------+
-- | etc...
-- = Reponse question 127381.

select month(C.datecom) mois,M.nommag as Magasin,sum(D.qte*prixvente) CA
from MAGASIN M NATURAL JOIN COMMANDE C NATURAL JOIN DETAILCOMMANDE D
where YEAR(datecom) ='2024'
group by Magasin,mois;


-- +-----------------------+--
-- * Question 127437 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 4 Comparaison ventes en ligne et ventes en magasin

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+------------+---------+
-- | annee | typevente  | montant |
-- +-------+------------+---------+
-- | etc...
-- = Reponse question 127437.

select YEAR(datecom) annee ,(REPLACE(REPLACE(enligne,'N','En magasin'),'O','En ligne')) typevente, round(sum(qte*prixvente)) montant
from COMMANDE NATURAL JOIN DETAILCOMMANDE 
where year(datecom) != '2025'
group by annee,typevente;

-- +-----------------------+--
-- * Question 127471 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 5

-- Voici le début de ce que vous devez obtenir. 
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------+-----------+
-- | Editeur           | nbauteurs |
-- +-------------------+-----------+
-- | etc...
-- = Reponse question 127471.

select nomedit as Editeur, count(distinct(idauteur)) nbauteurs
from EDITEUR natural join EDITER natural join LIVRE natural join ECRIRE
group by nomedit
Order by nbauteurs desc
LIMIT 10;

-- +-----------------------+--
-- * Question 127516 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 6 Origine des clients ayant acheter des livres de R. Goscinny

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------+-----+
-- | ville       | qte |
-- +-------------+-----+
-- | etc...
-- = Reponse question 127516.

Select villecli ville, sum(qte) qte
from CLIENT NATURAL JOIN COMMANDE NATURAL JOIN DETAILCOMMANDE NATURAL JOIN LIVRE NATURAL JOIN ECRIRE NATURAL JOIN AUTEUR
Where nomauteur = 'René Goscinny'
group by villecli;

-- +-----------------------+--
-- * Question 127527 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Graphique 7 Valeur du stock par magasin
-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------------------------+---------+
-- | Magasin                 | total   |
-- +-------------------------+---------+
-- | etc...
-- = Reponse question 127527.
 

select nommag as Magasin, sum(qte*prix) as ValeurStock
from MAGASIN natural join POSSEDER natural join LIVRE
group by Magasin;



--Requête Graphique 8 Statistiques sur l'évolution du chiffre d'affaire total par client 
-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+---------+---------+---------+
-- | annee | maximum | minimum | moyenne |
-- +-------+---------+---------+---------+
-- | etc...


with CA as (
select idcli,Year(datecom) as annee, sum(qte*prixvente) as CA
from COMMANDE NATURAL JOIN DETAILCOMMANDE NATURAL JOIN CLIENT
group by annee,idcli)

select annee, max(CA) as maximum, min(CA) as minimum, round(AVG(CA),2) as moyenne from CA group by annee; 

-- +-----------------------+--
-- * Question 127538 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête Palmarès
-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-------+-----------------------+-------+
-- | annee | nomauteur             | total |
-- +-------+-----------------------+-------+
-- = Reponse question 127538.


With AuteurAnneeVente as (
Select nomauteur,YEAR(datecom) as annee, sum(qte) as total
from AUTEUR NATURAL JOIN ECRIRE NATURAL JOIN LIVRE NATURAL JOIN DETAILCOMMANDE NATURAL JOIN COMMANDE
Where YEAR(datecom) !='2025' 
group by idauteur,YEAR(datecom))

Select annee,nomauteur,total
From AuteurAnneeVente
Where (annee, total) in (
    select annee,MAX(total)
    from AuteurAnneeVente
    group by annee)
Order by annee;


-- +-----------------------+--
-- * Question 127572 : 2pts --
-- +-----------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Requête imprimer les commandes en considérant que l'on veut celles de février 2020
-- | etc...
-- = Reponse question 127572.


SELECT M.nommag,Cl.prenomcli,Cl.nomcli,Cl.adressecli,Cl.villecli,C.numcom,C.datecom,DC.numlig,L.isbn,L.titre,DC.qte,DC.prixvente AS prix,(DC.qte*DC.prixvente) as total
FROM MAGASIN M
JOIN COMMANDE C ON M.idmag = C.idmag
JOIN CLIENT Cl on C.idcli = Cl.idcli
JOIN DETAILCOMMANDE DC ON C.numcom = DC.numcom
JOIN LIVRE L ON DC.isbn = L.isbn
WHERE YEAR(datecom)= ? and MONTH(datecom) = ?
ORDER BY C.numcom, DC.numlig;



