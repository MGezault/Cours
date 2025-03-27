
select month(C.datecom) mois,YEAR(C.datecom) annee,sum(D.qte*D.prixvente) CA
FROM COMMANDE C NATURAL JOIN DETAILCOMMANDE D
group by mois,annee
order by annee,mois;


select sum(D.qte),sum(D.qte*D.prixvente) CA
FROM COMMANDE C NATURAL JOIN DETAILCOMMANDE D
group by month(C.datecom),YEAR(C.datecom);
