import blackjack

def main():

    deck = blackjack.generate_deck()

    n=input("nombre de joueurs ?")

    print "n= ", n

    mains = []
    for i in range(n+1):
        mains.append([])

    for i in range(2):
        for j in range(n + 1):
            mains[j].append(deck.pop())

    print blackjack.liste_mains(mains)

if __name__ == '__main__':
    main()
