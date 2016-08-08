import blackjack

def main():

    deck = blackjack.generate_deck()

    n=input("nombre de joueurs ?")

    print "n= ", n

    mains = []
    for i in range(n+1):
        mains.append([])

    # le dealer distribue une carte pour chaque joueur puis une à lui-même, puis une autre à chaque joueur au blackjack EU

    for j in range(n + 1):
            mains[j].append(deck.pop())

    for j in range( n ):
            mains[j].append(deck.pop())

    print blackjack.liste_mains(mains)

    # on veut faire évaluer au joueur les mains de chaque joueur

    v_mains = []
    for i in range(n):
        v_mains.append( input ( "evalue la main du joueur " + str(i + 1) + ":" ) )
    print v_mains


if __name__ == '__main__':
    main()
