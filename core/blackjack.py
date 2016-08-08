import random

def cardname(n):

    if n<0 or n>51 :
        return "carte invalide"
    if int(n)!=n :
        return "carte invalide"

    res = ""
    res = ["as","2","3","4","5","6","7","8","9","10","valet","dame","roi"][n%13]
    res += " de "
    res += ["trefles", "carreaux", "coeurs", "piques"][n//13]

    return res

def liste_mains(mains):

    noms_des_mains = []

    for i in range(len(mains)):
        main = mains[i]
        nom_de_la_main = []
        for carte in main:
            nom_de_la_main.append(cardname(carte))
        if (i == len(mains) - 1):
            noms_des_mains.append("main du dealer :" + str(nom_de_la_main))
        else:
            noms_des_mains.append("main du joueur " + str(i + 1) + " :" + str(nom_de_la_main))

    return noms_des_mains

def generate_deck():

    deck=[]
    ordered_deck=range(52)

    for i in range(52) :
        r=random.randint(0,51-i)
        deck.append(ordered_deck[r])
        ordered_deck.pop(r)

    return deck

def evaluer_carte(n):

    v = [11,2,3,4,5,6,7,8,9,10,10,10,10][n%13]
    return v


def evaluer_main(l):

    s=0
    for i in l:
        s += evaluer_carte(i)

    return s
