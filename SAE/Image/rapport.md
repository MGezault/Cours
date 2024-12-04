**Rendu de la SAE Image par Matéo Gezault**
-
**A.0)**

Voici le message d'erreur renvoyé par le terminal: 
display-im6.q16: length and filesize do not match `ImageExemple.bmp' @ error/bmp.c/ReadBMPImage/958.

La raison de l'erreur est toute bête, en effet, dans le fichier, il y a 3 octets dédiés à la mémoire dans le fichier qui permettent de noter le poids du fichier, ces trois octets dans le fichier indiquent la valeur "OC7399" soit 816 025 octets, sauf que le poids réel du fichier est 816 026. Il y a donc une incohérence qu'il faut régler, pour ceci, rien de plus simple, il suffit de modifier la valeur des octets dans Okteta et d'y écrire ""OC739A". 