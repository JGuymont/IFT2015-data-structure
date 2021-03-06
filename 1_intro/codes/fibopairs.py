#!/usr/bin/python3

# author = "Francois Major"
# date = "11 janvier 2014"
# version = "1.0"
#
# Programme Python pour IFT2015/Mise à niveau/Initiation à Python
# Facteurs d'un entier
# Pris et modifié de Goodrich, Tamassia & Goldwasser
#   Data Structures & Algorithms in Python (c)2013

# Ce programme prend en input une valeur entière positive
# et retourne les termes pairs de la suite de Fibonacci
# jusqu'à cette valeur.
def main():
    # Prompter l'usager et
    # lire en entrée un entier
    print( "Ce programme retourne les termes pairs de la suite de Fibonacci jusqu'à un entier positif." )
    try:
        n = int( input( 'Entrez un entier positif : ' ) )
    except ValueError:
        print( "Ce n'est pas un entier !" )
        exit()

    # Ici n contient une valeur entière
    # Si n est positif, on envoit à l'usager les termes pairs de la suite
    # Sinon, on envoit un message d'erreur
    if n >= 0:
        """La compréhension de liste permet de produire
           4 types de contenant:

           [ k*k for k in range( 1, n+1 ) ] - liste
           { k*k for k in range( 1, n+1 ) } - ensemble
           ( k*k for k in range( 1, n+1 ) ) - générateur
           { k : k*k for k in range( 1, n+1 ) } - dictionnaire
           
           ATTENTION. Dans le cas où on parcourt un générateur infini,
           on doit prosuire un générateur car si on produit
           n'importe quel des 3 autres types, alors python va vouloir
           le compléter jusqu'à l'infini.
        """
        # Pour former un output de type String, on utilise
        # un iterateur et on ajoute à la String initialement
        # vide les nombres de la suite à ajouter, d'un nouveau générateur
        # pour fibo dans le générateur définit par :
        #   les valeurs de f prises dans la suite de Fibonacci
        #   ssi f se divise par 2 (vérifié avec modulo)
        s = "["
        for fibo in (f for f in fibonacci() if f % 2 == 0):
            if fibo > n:
                break
            s += str( fibo ) + ", "
        # comme c'est une suite infinie, on ajoute ... à la fin
        s += "... ]"
        print( "Les termes pairs de la suite de Fibonacci jusqu'à", n, "sont :", s )
    else:
        print( "L'entier entré n'est pas positif. " )


# Fonction fibonacci utilisant un generateur infini
def fibonacci( ):
    # la suite débute avec 0, 1
    # par la suite c'est la somme des deux nombres précédents
    # on utilise a et b pour stocker ces deux nombres
    # en débutant avec 0 et 1
    a = 0
    b = 1
    # on boucle à l'infini...
    while True:
        # on ajoute a à la suite
        yield a
        # on sauvegarde la somme des 2 derniers nombres
        portee = a + b # Fibonacci calcule des portées de lapins !
        # on avance de 2 positions dans la suite
        # a prend la valeur du nombre suivant, b
        a = b
        # b devient le nouveau nombre généré
        b = portee

# Appel de la fonction principale
main()


