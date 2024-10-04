def mystere(liste, valeur):
    """Trouve la quatrième valeur de liste égale à valeur

    Args:
        liste ([list]): une liste d'entier dans laquelle on va chercher la valeur
        valeur ([int]): l'entier que nous allons chercher dans liste

    Returns:
        [int]: l'indice de la quatrième occurence de valeur dans la liste
    """
    xxx = 0
    yyy = 0
    for elem in liste:
        #Au début de chaque tour de boucle, xxx à la valeur de l'indice de la valeur actuellement observée
        #Au début de chaque tour de boucle, y à la valeur du nombre d'élement de la liste égale à la valeur cherchée
        if elem == valeur:
            yyy += 1
            if yyy > 3:
                #l'instruction est exécutée si on rencontre la 4e valeur de la liste égale à valeur
                return xxx
        xxx += 1
    return None


k=mystere([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20)
print(k)
# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]

# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
