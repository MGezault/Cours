def annee(untuple):
    """Indique si untuple respecte les conditions d'un tuple

    Args:
        untuple (tuple): Un tuple 

    Returns:
        bool : Renvoie True si untuple respecte les conditions, False s'il ne les respecte pas
    """
    if isinstance(untuple,tuple):
        if len(untuple)==4:
            if (isinstance(untuple[0],str)) and (isinstance(untuple[1],str)) and (isinstance(untuple[3],str)):
                if (len(untuple[1])==10):
                    if (isinstance(untuple[2],(float,int))):
                        return True
    return False
liste2 = [
('Christophe', '2024-09-26', 15, 'type1'),
('David', '2024-09-26', 18, 'type1'),
('Guillaume', '2024-09-26', 17, 'type1'),
('Christophe', '2024-09-27', 19, 'type2'),
('David', '2024-09-27', 21, 'type2'),
('Guillaume', '2024-09-27', 20, 'type2'),
('Christophe', '2024-09-28', 14, 'type3'),
('David', '2024-09-28', 17, 'type3'),
('Guillaume', '2024-09-28', 16, 'type3'),
('Christophe', '2024-09-29', 20, 'type4'),
('David', '2024-09-29', 23, 'type4'),
('Guillaume', '2024-09-29', 22, 'type4'),]

('Christophe', '2024-09-26', 15, 'type1'),
('David', '2024-09-26', 18, 'type1'),
('Guillaume', '2024-09-26', 17, 'type1'),
('Christophe', '2024-09-27', 19, 'type2'),
('David', '2024-09-27', 21, 'type2'),
('Guillaume', '2024-09-27', 20, 'type2'),
('Christophe', '2024-09-28', 14, 'type3'),
('David', '2024-09-28', 17, 'type3'),
('Guillaume', '2024-09-28', 16, 'type3'),
('Christophe', '2024-09-29', 20, 'type4'),
('David', '2024-09-28', 17, 'type3'),
('Guillaume', '2024-09-28', 16, 'type3'),
('David', '2024-09-29', 23, 'type4'),
('Guillaume', '2024-09-29', 22, 'type4'),
