class DictionnaireOrdonne:
        """Notre dictionnaire ordonné. L'ordre des données est maintenu
            et il peut donc, contrairement aux dictionnaires usuels, être trié
            pour voir l'ordre de ses données inversées"""              

    def __init__(self, base={}, **donnees):
    """Constructeur de notre objet. Il peut ne prendre aucun paramètre 
    (dans ce cas, le dictionnaire sera vide) ou construire un
    dictionnaire remplis grâce :
         -   au dictionnaire 'base' passé en premier paramètre ;
         -   aux valeurs que l'on retrouve dans 'donnees'."""                           
         self._cles = [] # Liste contenant nos clés                                      self._valeurs = [] # Liste contenant les valeurs correspondant à nos clés

                                                                                                    
