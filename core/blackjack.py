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

def creer_mains(n):
     mains = [[] for i in range(n+1)]
     return mains

def liste_mains(n, mains):

    noms_des_mains = []

    for i in range(n+1):
        main = mains[i]
        nom_de_la_main = []
        for carte in main:
            nom_de_la_main.append(cardname(carte))
        if (i == n+1 - 1):
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

def generate_final_deck():

    sum_decks = []
    final_deck = []

    for i in range(6):

        sum_decks += generate_deck()

    #on remelange le tout

    for i in range(52*6) :

        r=random.randint(0,52*6 - 1 - i )

        final_deck.append(sum_decks[r])

        sum_decks.pop(r)



    assert len( final_deck ) == 6 * 52
    assert len( sum_decks ) == 0

    return final_deck




def evaluer_carte(n):

    v = [11,2,3,4,5,6,7,8,9,10,10,10,10][n%13]
    return v


def evaluer_main(l):

    s=0
    for i in l:
        s += evaluer_carte(i)

    return s


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


    def miser(self, min_bet) :

        while self.bankroll >= min_bet :

                if self.bankroll >= min_bet :

                    self.bet = ( input( str( self.get_name() ) + ", put your bet :") )

                    self.bankroll -= self.bet

                else :

                    print str(self.get_name() ) + ", you can't bet anymore"

                    self.bet = 0



    def play(self, i, mains):

        if evaluer_main( mains[i] ) == 21 :

            print "Blackjack for" + str( self.get_name() )

            self.bj = 1

        while evaluer_main( mains[i] ) < 21 :

            choice = input( str( self.get_name() ) + " is at " + str(evaluer_main( mains[i] )) 
                        + " and dealer is at " + str(evaluer_main(mains[n] )) + ", Hit or stay ? (1/0)")


            if choice == 1 :

                mains[i].append( draw(deck) )

                print liste_mains( mains )[i]

                print evaluer_main( mains[i] )


            elif evaluer_main( mains[i] ) > 21 :

                print str( self.get_name() ) + " Busts"

                while len(mains[i]) > 0 :

                    mains[i].pop()

                    break

            elif evaluer_main( mains[i] ) == 21 :

                print str( self.get_name() ) + " reaches 21"

            elif choice == 0 :
                
                print str( self.get_name() )+ " stops at " + str(evaluer_main( mains[i] ))
                break


def distribuer(mains, p_list) :

    n = len( mains ) - 1
    
    for j in range(n):

        if p_list[j].bet > 0 :
            mains[j].append( draw(deck) )

    mains[n].append( draw(deck) ) 

    for j in range(n):

        if p_list[j].bet > 0 :
            mains[j].append( draw(deck) )

class Dealer(Player):

    def __init__(self):
        self.name = "Dealer"
        self._bj = 0

    def play(self, i, mains):

        if evaluer_main( mains[i] ) == 21 :

            print "Blackjack for" + str( self.get_name() )

            self.bj = 1

        while evaluer_main( mains[i] ) < 17 :

            mains[i].append( draw(deck) )


            if evaluer_main( mains[i] ) > 21 :

                print str( self.get_name() ) + " Busts"

                while len(mains[i]) > 0 :

                    mains[i].pop()

                    break


            elif evaluer_main( mains[i] ) == 21 :

                print str( self.get_name() ) + " reaches 21"

            elif evaluer_main( mains[i] ) >= 17 and evaluer_main( mains[i] ) < 21 :
                
                print str( self.get_name() )+ " stops at " + str(evaluer_main( mains[i] ))
                break


def init_players(n):
    l = []
    for i in range(n):
        l.append( Player( input( "player " + str(i+1) + "'s name : (bewteen quotes)"), ))
    l.append( Dealer() )
    return l

def draw(deck):
    return deck.pop()

def comparer_scores(mains, n):

      #type arbre de decision : to do : a faire plus joliment 

    player_issue = [[] for i in range(n)]

    for i in range(n) :

        #le dealer a bust ?
        #oui
        if len( mains[n] ) == 0 :

            #le joueur a bust ?
            #oui
            if len( mains[i] ) == 0 :

                player_issue[i].append("lose")

            #non
            else :

                #le joueur a un BJ ?
                #oui
                if p_list[i].bj == 1 :

                        player_issue.append("blackjack")
                #non
                else :
                    player_issue.append("win")
        #non
        else :

            #le joueur a bust ?
            #oui
            if len( mains[i] ) == 0 :

                    player_issue[i].append("lose")

            #non
            else :

                #le joueur a un BJ ?
                #oui
                if p_list[i].bj == 1 :

                    #le dealer a un BJ ?
                    #oui
                    if p_list[n].bj == 1 :

                        player_issue[i].append("push")

                    #non   
                    else :

                        player_issue[i].append("blackjack")

                #non
                else :

                    #le joueur a t il plus que le dealer ?
                    #oui
                    if evaluer_main(mains[i]) > evaluer_main(mains[n]) :

                            player_issue[i].append("win")
                    #non            
                    else :

                        # le joueur a t il le meme score que le dealer ?
                        #oui
                        if evaluer_main(mains[i]) == evaluer_main(mains[n]) :

                            player_issue[i].append("push")

                        #non
                        else :

                            player_issue[i].append("lose")

    return player_issue

def pay(n, player_issue, p_list):

    for i in range (n) :

                if "blackjack" in player_issue[i] :

                    print str(self.get_name() ) + " is payed 3 for 2"

                    self.bankroll += 2,5 * self.bet

                elif "win" in player_issue[i] :

                    print str(self.get_name() ) + " is payed 1 for 1"

                    self.bankroll += 2 * self.bet

                elif "push" in player_issue[i] :

                    print str(self.get_name() ) + " wins nothing"

                    self.bankroll += self.bet

                else :

                    print str(self.get_name() ) + " loses his bet"


    for i in range(n):

        print str(self.get_name() ) + " has " + str( self.bankroll ) + " left"

        self.bet = 0

def creer_mains(n, p_list, deck):

    mains = [[] for i in range(n+1)]
    
    for j in range(n):

        if p_list[j].bet > 0 :
            mains[j].append( draw(deck) )

    mains[n].append( draw(deck) ) 

    for j in range(n):

        if p_list[j].bet > 0 :
            mains[j].append( draw(deck) )


