# Rendu de la SAE Image par Matéo Gezault

## A.0)

Voici le message d'erreur renvoyé par le terminal: 
display-im6.q16: length and filesize do not match `ImageExemple.bmp' @ error/bmp.c/ReadBMPImage/958.

La raison de l'erreur est toute bête, en effet, dans le fichier, il y a 3 octets dédiés à la mémoire dans le fichier qui permettent de noter le poids du fichier, ces trois octets dans le fichier indiquent la valeur "OC7399" <img src="Imagequestion0.png" alt="Image de réponse à la question 0" align="right" width="500" />soit 816 025 octets, sauf que le poids réel du fichier est 816 026 (on peut le savoir grâce aux propriétés du fichier). Il y a donc une incohérence qu'il faut régler, pour ceci, rien de plus simple, il suffit de modifier la valeur des octets dans Okteta et d'y écrire "OC739A".
Comme c'est en little endian, il faut modifier le premier octet et y inscrire 9A à la place de 99. 



## A.1)

Pour cette question, il fallait principalement suivre les instructions données pour créer le fichier et réaliser l'entête et le BITMAPCOREHEADER.

Puis par la suite, il fallait remplir les octets afin de colorier les pixels pour avoir les couleurs demandés, c'esst à dire un damier de couleur entre blanc et rouge. Le plus dur lors de cette question était de ne pas s'emmêler les pinceaux dans les insertions de valeurs, en effet, j'ai au début mal compris où était mon erreur et je me suis retrouvé avec des couleurs qui n'avait aucun rapport avec celles que je voulais. J'ai finalement réussis à avoir les couleurs désirées.

<img src="imagecodequ1.png" alt="Image montrant le code fourni pour la question 1" align="right" width="400" />

<img src="Image1.png" alt="Image montrant l'affichage du code de la question 1"  width="200" />






## A.2) 

Cette question-ci était plus simple que la précédente, en effet, il ne fallait que modifier les valeurs de pixels. La difficulté de la question était de ne pas oublier d'inverser les valeurs en particulier pour le bleu céruléen.
<img src="Imagecodequ2.png" alt="Image montrant le code fourni pour la question 2" align="right" width="400" />

<img src="Image2.png" alt="Image montrant l'affichage du code de la question 2"  width="200" />

## A.3)

### A.3.A)

Il y a 48 bits par pixel, on peut l'affirmer grâce aux deux octets entourés en rouge qui permettent de transmettre la quantité de bits par pixel. Comme c'est en little endian on inverse les valeurs, et 30 (base 16) en décimal vaut 48. 

<img src="Image3A.png" alt="Image de réponse à la question 3 A" width="400" />



### A.3.B)

Comme on peut le voir sur l'image, il y a 4x4 pixels sur l'image, soit 16 pixels.
Pour obtenir ces informations, j'ai fais un clique droit sur l'image, propriété, image.

<img src="Image3B.png" alt="Image de réponse à la question 3 B" width="400" />

### A.3.C)

Avant la conversion, l'image faisait 74 octets, après conversion, l'image en fait désormais 102, donc il n'y a pas de compression utilisée, au contraire, sa taille augmente.

<img src="Image3C.png" alt="Image de réponse à la question 3 C" width="400" />


### A.3.D)

Sachant qu'avant la conversion, chaque pixel était codé sur 24 bits et qu'après conversion, chaque pixel est codé sur 48 bits, alors le format de codage de bits a effectivement changé.


## A.4)

Il y a 8 bits par pixel, on peut l'affirmer grâce aux deux octets entourés en rouge qui permettent de transmettre la quantité de bits par pixel. Comme c'est en little endian on inverse les valeurs, et 30 (base 16) en décimal vaut 48. 

<img src="Image3A.png" alt="Image de réponse à la question 3 A" width="400" />