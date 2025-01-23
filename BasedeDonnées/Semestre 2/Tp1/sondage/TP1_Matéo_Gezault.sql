--Exercice 2 )
--1) 
SELECT dateNaisSond
from SONDE
WHERE prenomSond = 'Anna' and nomSond = 'SITOURIN';

--2)
Select idPan
from CONSTITUER
where numSond in (
    Select numSond
    FROM SONDE 
    WHERE prenomSond = 'Anna' and nomSond = 'SITOURIN'
    );

--3)
Select idCat
From CARACTERISTIQUE NATURAL JOIN SONDE 
WHERE prenomSond = 'Anna' and nomSond = 'SITOURIN';

--4)

Select idTR
From CARACTERISTIQUE NATURAL JOIN SONDE 
WHERE prenomSond = 'Anna' and nomSond = 'SITOURIN';


-- Exercice 3)

--1 :
--Méthode avec In
Select nompan
from PANEL
where idPan in (
    Select idPan 
    FROM CONSTITUER
    WHERE numSond in (
        Select numSond
        FROM SONDE 
        WHERE prenomSond = 'Caroline' and nomSond = 'BOURIER'));



--Méthode avec Natural JOIN
Select nompan 
From PANEL NATURAL JOIN SONDE NATURAL JOIN CONSTITUER
WHERE prenomSond = 'Caroline' and nomSond = 'BOURIER';


--Méthode avec Exists

Select nompan
from PANEL 
WHERE Exists(
    Select idPan
    from CONSTITUER
    where PANEL.idPan = CONSTITUER.idPan and EXISTS (
        Select numSond
        FROM SONDE S
        WHERE S.numSond = CONSTITUER.numSond and prenomSond = 'Caroline' and nomSond = 'BOURIER'));

-- 2) 

--Méthode avec Exists
Select distinct(nompan)
from PANEL P
WHERE Exists(
    Select idPan
    from CONSTITUER C
    where P.idPan = C.idPan AND EXISTS (
        Select numSond
        FROM SONDE S
        WHERE C.numSond = S.numSond AND EXISTS(
            Select idC
            FROM CARACTERISTIQUE C
            WHERE C.idC = S.idC AND EXISTS(
                Select idTR 
                FROM TRANCHE T
                Where T.idTR = C.idTR AND valDebut >= 70 and valFin<=120
        ))));

--Méthode avec NATURAL JOIN
Select distinct(nompan)
from PANEL NATURAL JOIN CONSTITUER NATURAL JOIN SONDE NATURAL JOIN CARACTERISTIQUE NATURAL JOIN TRANCHE
Where valDebut >= 70 and valFin <=120;

--Méthode avec IN

Select distinct(nompan)
from PANEL 
WHERE idPan in (
    Select idPan
    from CONSTITUER
    where numSond in (
        Select numSond
        FROM SONDE 
        WHERE idC in (
            Select idC
            FROM CARACTERISTIQUE
            WHERE idTR in (
                Select idTR
                FROM TRANCHE
                Where valDebut >= 70 and valFin<=120
        ))));


-- 3)

Select nomSond,prenomSond
from SONDE 
where idC in (
    Select idC
    FROM CARACTERISTIQUE
    where idTR in (Select idTR from TRANCHE where valDebut >= 70 and valFin<=120) and idCat in (select idCat FROM CATEGORIE where intituleCat = 'Ouvriers')
);

-- 4 )
Select nomSond,prenomSond
from SONDE 
where prenomSond = 'Olivier' and idC in (
    Select idC
    FROM CARACTERISTIQUE
    where  idCat in (select idCat FROM CATEGORIE where intituleCat = 'Ouvriers')
);

-- 5 )
