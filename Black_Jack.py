import random

#/////////////////////Determine Cards/////////////////////////////

card_numbers = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
card_type = ["Clubs", "Hearts", "Spades", "Diamonds"]

def card_face():
    return random.choice(card_type)

def drawn_card():
    return random.choice(card_numbers)

dealer_count = drawn_card()
player_count = drawn_card() + drawn_card()
player_balance = 500

#/////////////////////Game Functions/////////////////////////////

def reset():
    global dealer_count
    global player_count

    dealer_count = drawn_card()
    player_count = drawn_card() + drawn_card()

def hit():
    global player_count
    temp_card = drawn_card()
    player_count += temp_card
    print("\nPlayer Got: ", temp_card, " of ", card_face())

def stand():
    global dealer_count
    dealer_temp = drawn_card()
    dealer_count += dealer_temp
    print("\nDealer Drew: ", dealer_temp, " of ", card_face())

def Win():
        global bet_amount
        global player_balance
        print("You Win! :)\n")
        player_balance += bet_amount

def Lose():
    global player_balance
    global bet_amount
    print("You Lose :(\n")
    player_balance -= bet_amount

#/////////////////////Game Begins Bellow here/////////////////////////////

while True:
    round_over = False

    print("\nWelcome To Black Jack\n")
    print("Balance: $", player_balance, "\n")
    bet_amount = int(input("How Much Do You Want To Bet?\n"))
    if bet_amount < 0:
        print("Bets Must Be $0 or More")
        break
    elif bet_amount > player_balance:
        print("You Do Not Have Enough")
        break
    
    print("\nDealer: ", dealer_count)
    print("Player: ", player_count,"\n")
    if player_count == 21:
        Win()
        reset()
        continue

    while round_over != True:
        choice = input("\nWhat Do You Want To Do?\n1: Hit\n2: Stand\n")
        
        if choice == "1":
            hit()
            print("\nDealer: ", dealer_count)
            print("Player: ", player_count,"\n")
            
            if player_count > 21: 
                Lose()
                reset()
                round_over = True
            
            elif player_count == 21:
                Win()
                reset()
                round_over = True

        elif choice == "2":
            while dealer_count < player_count:
                stand()
                print("\nDealer: ", dealer_count)
                print("Player: ", player_count,"\n")

                if dealer_count > 21:
                    Win()
                elif dealer_count >= player_count:
                    Lose()

            reset()
            round_over = True

        else:
            print("Invalid Answer. Try Agian.")
        
    ans = input("Play Again?\n1: Yes\n2: No\n")

    if ans != "1":
        break