import blackjack



def main():

    # initialisation

    deck = blackjack.generate_final_deck()

    #n = input( "Nombre de joueurs =")
    n = 1 # debuging

    p_list = blackjack.init_players(n)

    #min_bet = input("Fix minimum bet (2€ min) :")
    min_bet = 2


    # mises

    for i in range(n) :

        p_list[i].miser(min_bet)


    # création des mains

    mains = blackjack.creer_mains(n, p_list, deck)

    print blackjack.liste_mains(n, mains)

    # to do : rajouter double, split


    # les joueurs jouent

    for i in range(n):

        p_list[i].play(i, mains)


    # le dealer joue (tout seul)

    print "It's dealer's turn"

    p_list[n].play(mains)


    # comparaison des scores

    player_issue = blackjack.comparer_scores(mains)


    # resultats

    blackjack.pay(n, player_issue, p_list)




#j'ai definit les classes ici car j'avais un probleme pour appeler un attribut d'un joueur, 
# cela donnait : p_list[i].blackjack.bankroll
# et comme erreur : Player instance has no attribute 'blackjack'
class Player :

    def __init__(self, name) :
        self.name = name
        self._bankroll = 0
        self._bet = 0
        self._bj = 0

    def get_name(self):
        return self.name

    def _get_bankroll(self):
        return self._bankroll

    def _get_bet(self):
        return self._bet

    def _get_blackjack(self):
        return self._bj

    def _set_bet(self, bet):
        self._bet = bet

    def _set_bankroll(self, bankroll):
        self._bankroll = bankroll


    def _set_blackjack(self, blackjack):
        self._bj = blackjack


    bankroll = property(_get_bankroll, _set_bankroll)
    bet = property(_get_bet, _set_bet)
    bj = property(_get_blackjack, _set_blackjack)

    min_bet = 2


    def miser(self, min_betm) :

        while self.bankroll >= min_bet :

                if self.bankroll >= min_bet :

                    self.bet = ( input( str( self.get_name() ) + ", put your bet :") )

                    self.bankroll -= self.bet

                else :

                    print str(self.get_name() ) + ", you can't bet anymore"

                    self.bet = 0



    def play(self, i, mains):

        if blackjack.evaluer_main( mains[i] ) == 21 :

            print "Blackjack for" + str( self.get_name() )

            self.bj = 1

        while blackjack.evaluer_main( mains[i] ) < 21 :

            choice = input( str( self.get_name() ) + " is at " + str(blackjack.evaluer_main( mains[i] )) 
                        + " and dealer is at " + str(blackjack.evaluer_main(mains[n] )) + ", Hit or stay ? (1/0)")


            if choice == 1 :

                mains[i].append( draw(deck) )

                print blackjack.liste_mains( mains )[i]

                print blackjack.evaluer_main( mains[i] )


            elif blackjack.evaluer_main( mains[i] ) > 21 :

                print str( self.get_name() ) + " Busts"

                while len(mains[i]) > 0 :

                    mains[i].pop()

                    break

            elif blackjack.evaluer_main( mains[i] ) == 21 :

                print str( self.get_name() ) + " reaches 21"

            elif choice == 0 :
                
                print str( self.get_name() )+ " stops at " + str(blackjack.evaluer_main( mains[i] ))
                break

class Dealer(Player):

    def __init__(self):
        self.name = "Dealer"
        self._bj = 0

    def play(self, i, mains):

        if blackjack.evaluer_main( mains[i] ) == 21 :

            print "Blackjack for" + str( self.get_name() )

            self.bj = 1

        while blackjack.evaluer_main( mains[i] ) < 17 :

            mains[i].append( draw(deck) )


            if blackjack.evaluer_main( mains[i] ) > 21 :

                print str( self.get_name() ) + " Busts"

                while len(mains[i]) > 0 :

                    mains[i].pop()

                    break


            elif blackjack.evaluer_main( mains[i] ) == 21 :

                print str( self.get_name() ) + " reaches 21"

            elif blackjack.evaluer_main( mains[i] ) >= 17 and blackjack.evaluer_main( mains[i] ) < 21 :
                
                print str( self.get_name() )+ " stops at " + str(blackjack.evaluer_main( mains[i] ))
                break


if __name__ == '__main__':
    main()
