SELECT M.nommag,Cl.prenomcli,Cl.nomcli,Cl.adressecli,Cl.villecli,C.numcom,C.datecom,DC.numlig,L.isbn,L.titre,DC.qte,DC.prixvente AS prix,(DC.qte*DC.prixvente) as total
FROM MAGASIN M
JOIN COMMANDE C ON M.idmag = C.idmag
JOIN CLIENT Cl on C.idcli = Cl.idcli
JOIN DETAILCOMMANDE DC ON C.numcom = DC.numcom
JOIN LIVRE L ON DC.isbn = L.isbn
ORDER BY C.numcom, DC.numlig;
