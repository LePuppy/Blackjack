import blackjack

def main():

    deck = blackjack.generate_final_deck()

    n=input("How many players ?")

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

    # on va demander à chaque joueur de hit ou de stay
    # to do : rajouter double, split, blackjack

    bj_case = []
    for i in range(n+1):
        bj_case.append([])

    for i in range(n):

        # cas du blackjack

        if blackjack.evaluer_main( mains[i] ) == 21 :

            print "Blackjack for player " + str(i+1)

            bj_case[i].append("bj")



        while blackjack.evaluer_main( mains[i] ) < 21 :

            choice = input("Player " + str(i+1) + " is at " + str(blackjack.evaluer_main( mains[i] )) 
                + " and dealer is at " + str(blackjack.evaluer_main(mains[n] )) + ", Hit or stay ? (1/0)")

            if choice == 1 :

                mains[i].append( deck.pop() )

                print blackjack.liste_mains( mains )[i]

                print blackjack.evaluer_main( mains[i] )


            if blackjack.evaluer_main( mains[i] ) > 21 :

                print "Player " + str(i + 1) + " Busts"

                while len(mains[i]) > 0 :

                    mains[i].pop()

            if blackjack.evaluer_main( mains[i]) == 0 :

                break

            if blackjack.evaluer_main( mains[i] ) == 21 :

                print "Player " + str(i + 1) + " reaches 21"

            if choice == 0 :
                
                print "Player " + str(i + 1) + " stops at " + str(blackjack.evaluer_main( mains[i] ))
                break


    print "It's dealer's turn"


    while blackjack.evaluer_main( mains[n] ) < 17 :

        print "Dealer hits"

        mains[n].append( deck.pop() )

        print blackjack.liste_mains( mains )[n]

        print blackjack.evaluer_main( mains[n] )

        if blackjack.evaluer_main( mains[n] ) == 21 and len(mains[n]) == 2 :

            print "Blackjack for the dealer, all players lose their bet except the ones with a blackjack"

            bj_case[n].append("bj")


        if blackjack.evaluer_main( mains[n] ) > 16 and blackjack.evaluer_main( mains[n] ) <= 20 :

            print "Dealer stops at " + str(blackjack.evaluer_main( mains[n] ))

        if blackjack.evaluer_main( mains[n] ) == 21 and len(mains[n]) > 2 :

            print "Dealer reaches 21"

        if blackjack.evaluer_main( mains[n] ) > 21 :

            while len(mains[n]) > 0 :

                    mains[n].pop()

            print "Dealer busts"
            print "Players still in are payed"

        if blackjack.evaluer_main( mains[n]) == 0 :

                break

    # comparaison des scores

    bet_res = []

    for i in range(n):
        bet_res.append([])

    for i in range(n) :

        # le dealer n'a pas bust
  
        if mains[i] != [] and mains[n] != [] :

            # cas bj juste pour le joueur

            if bj_case[i] != [] and bj_case[n] == [] :

                bet_res[i].append("win")

            # cas bj pour les deux

            if bj_case[i] != [] and bj_case[n] != [] :

                bet_res[i].append("push")

            # cas bj seulement pour le croupier

            if bj_case[i] == [] and bj_case[n] != [] :

                bet_res[i].append("lose")

            # cas aucun bj

            if bj_case[i] == [] and bj_case[n] == [] :

                if blackjack.evaluer_main(mains[i]) > blackjack.evaluer_main(mains[n]) :

                    bet_res[i].append("win")

                if blackjack.evaluer_main(mains[i]) == blackjack.evaluer_main(mains[n]) :

                    bet_res[i].append("push")


                if blackjack.evaluer_main(mains[i]) < blackjack.evaluer_main(mains[n]) :

                    bet_res[i].append("lose")

        # le dealer a bust

        if mains[i] != [] and mains[n] == [] :

                bet_res[i].append("win")

        # le joueur a bust

        if mains[i] == [] and mains[n] != [] :

            bet_res[i].append("lose")

    print bet_res


    # resultats

    for i in range(n):

        assert len(bet_res[i]) == 1

    for i in range (n) :

        if "win" in bet_res[i] :#and bj_case[i] == []

            print "Player " + str(i+1) + " is payed 1 for 1"

        if "win" in bet_res[i] and bj_case[i] != [] :

            print "Player " + str(i+1) + " is payed 3 for 2"

        if "push" in bet_res[i] :

            print "Player " + str(i+1) + " wins nothing"

        if "lose" in bet_res[i]:

            print "Player " + str(i+1) + " loses his bet"



if __name__ == '__main__':
    main()
