#### Imports et définition des variables globales
'''On importe les modules nécessaires'''
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename,  mode='r', encoding='utf8') as fichier :
        l = list(csv.reader(fichier, delimiter=';', quoting=csv.QUOTE_NONNUMERIC))
        # On ouvre et récupère les données du fichiers dans une liste de listes.
    return l

def get_list_k(data, k):
    '''Retourne la k-ème sous-liste de data'''
    return data[k]

def get_first(l):
    '''Retourne le premier élément de la liste l'''
    return l[0]

def get_last(l):
    '''Retourne le dernier élément de la liste l'''
    return l[-1]

def get_max(l):
    '''Retourne le maximum de la liste l'''
    return max(l)

def get_min(l):
    '''Retourne le minimum de la liste l'''
    return min(l)

def get_sum(l):
    '''Retourne la somme des éléments de l'''
    return sum(l)


#### Fonction principale


def main():
    '''Utilise les fonctions secondaires pour vérifier leur fonctionnement'''
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
