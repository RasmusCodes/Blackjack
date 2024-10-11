import random

balance = 1000
cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def main(chips):
    prevbet = 10
    while chips > 0:
        print("Current chips:", chips)
        bet = input("Bet: ");
        if bet == "": 
            bet = prevbet
        try: 
            bet = int(bet)
            prevbet = bet
        except: 
            bet = prevbet

        if (afford(bet, chips)):
            hands = initial_cards()
            hand1 = hands[0]
            hand2 = hands[1]
            chips = deal(bet, chips, hand1, hand2)
        else:
            print("Invalid bet.\n")
    
    print("Out of chips!")
    return

def afford(bet, money):
    if (bet > money):
        return False
    else:
        return True 
def initial_cards():
    p = [cards[random.randint(0,12)], cards[random.randint(0,12)]]
    d = [cards[random.randint(0,12)]]
    return p, d

def deal(bet, chips, phand, dhand):

    pvalue = value(phand)
    dvalue = value(dhand)

    printhand(phand, "Player")
    print("Dealer is showing", dhand[0])
    if not blackjack(phand):
        print("h = hit")
        
        if chips >= 2 * bet:
            print("d = double")
        
        
        if value(phand[0]) == value(phand[1]):
            print("x = split")
        
        print("any other key = stand")
        action = input("Your call: ")
        
        if action == "h":
            stop_deal = False
            while value(phand) < 21 and not stop_deal:
                
                phand.append(cards[random.randint(0,12)])
                printhand(phand, "Player")
                
                if value(phand) > 21: 
                    print("You busted! Dealer wins!")
                    return (chips - bet)
                if value(phand) != 21: 
                    print("h = hit")
                    print("any other key = stand")
                    teko = input("Your call: ")
                    
                    if teko != "h":
                        stop_deal = True
            
        elif action == "d" and chips >= 2 * bet:
            phand.append(cards[random.randint(0,12)])
            bet *= 2
            printhand(phand, "Player")
            if value(phand) > 21: 
                print("You busted! Dealer wins!")
                return (chips - bet)

        elif action == "x" and chips >= 2 * bet and value(phand[0]) == value(phand[1]):
            phand1 = [phand[0], cards[random.randint(0,12)]]
            phand2 = [phand[0], cards[random.randint(0,12)]]
            chips = deal(bet, chips, phand1, dhand) 
            chips = deal(bet, chips, phand2, dhand)
            return chips
    
        while value(dhand) < 17: 
            dhand.append(cards[random.randint(0,12)])
            printhand(dhand, "Dealer")
        if value(dhand) > 21: 
            print("Dealer busts. Player wins!")
            return chips + bet
        elif value(phand) > value(dhand):
            print("Player wins!")
            return chips + bet
        elif value(phand) == value(dhand):
            print("Push!")
            return chips
        else: 
            print("Dealer wins!")
            return chips - bet

    else: 
        print("Blackjack!")
        print("You win",bet*1.5,"chips!")
        return chips + 1.5 * bet

def value(hand):
    total = 0
    for i in range(0, len(hand)):
        try:
            total += int(hand[i])
        except: 
            if hand[i] == "A":
                if total + 11 > 21:
                    total+=1
                else:
                    total+=11
            else: 
                total+=10
    if "A" in hand and total > 21: 
        return total - 10
    return total

def printhand(hand, name):
    outstring = ""
    for i in hand:
        outstring+=i
    print(name + " has: " + outstring + " (" + str(value(hand)) + ")")

def blackjack(hand):
    if len(hand) == 2 and value(hand) == 21: 
        return True
    return False

main(balance)