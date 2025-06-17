import random
import os
import time

WALLET = 10_000
SP = False

# Define suits and ranks
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11  # Ace initially counts as 11
}

def create_deck():
    """Creates a full deck of 52 shuffled cards."""
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_make(rank, suit):
    """Formats a card as ASCII art."""
    top = "┌─────────┐"
    middle = f"│ {rank.ljust(2)}      │"  # Left align rank
    middle2 = "│         │"
    middle3 = f"│    {suit}    │"
    middle4 = "│         │"
    middle5 = f"│      {rank.rjust(2)} │"  # Right align rank
    bottom = "└─────────┘"

    return "\n".join([top, middle, middle2, middle3, middle4, middle5, bottom])

def print_hand(cards, hide_first=False):
    """Prints the player's or dealer's hand with optional card hiding."""
    card_parts = list(zip(*[
        (card_make(rank, suit) if not (hide_first and i == 0) else card_make("?", "?")).splitlines()
        for i, (rank, suit) in enumerate(cards)
    ]))
    for part in card_parts:
        print("  ".join(part))

def calculate_hand_value(cards):
    """Calculates the total hand value, adjusting Aces if necessary."""
    value = 0
    ace_count = 0

    for rank, _ in cards:
        if rank == "A":
            ace_count += 1
            value += 11  # Assume Ace is 11 initially
        else:
            value += card_values[rank]

    # Convert Aces from 11 to 1 if needed
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1

    return value

# Main game loop
while True:
    deck = create_deck()  # Start with a fresh shuffled deck
    # Initial two cards for player and dealer
    player_hand = [deck.pop(),deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    #users bet
    while True:
        try:
            os.system('clear')
            print("Balence: ",WALLET)
            users_bet = int(input("Enter your bet: "))
            if users_bet > WALLET or users_bet <= 0:
                print("Invalid bet! Bet must be within your wallet amount.")
                time.sleep(2)
                continue
            WALLET -= users_bet 
            break
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(2)


    # Show hands (hiding one of dealer's cards)
    print("\nYour hand:")
    print_hand(player_hand)

    print("\nDealer's hand:")
    print_hand(dealer_hand, hide_first=True)

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        if player_hand[0][0] == player_hand[1][0]:
            action = input("\nDo you want to (h)it, (s)tand, (d)ouble or (sp)lit:  ").lower()
        else:
            action = input("\nDo you want to (h)it, (s)tand, (d)ouble: ").lower()
        if action == "h":
            os.system('clear')
            player_hand.append(deck.pop())
            print("\nYour hand:")
            print_hand(player_hand)
            time.sleep(2)
        elif action == "s":
            break
        elif action == "d":
            if WALLET < users_bet:  # Prevent doubling if funds are insufficient
                print("Not enough funds to double down!")
                continue
            os.system('clear')
            WALLET -= users_bet  # Deduct the extra bet amount
            users_bet *= 2
            player_hand.append(deck.pop())
            print("\nYour hand:")
            print_hand(player_hand)
            time.sleep(2)
            break

        elif action == "sp" and player_hand[0][0] == player_hand[1][0]:
            SP = True
            if WALLET >= users_bet:
                os.system("clear")
                WALLET -= users_bet
                hand1 = [player_hand[0], deck.pop()]
                hand2 = [player_hand[1], deck.pop()]
                hands = [hand1,hand2]
                bets = [users_bet, users_bet]
            else:
                os.system('clear')
                print("Not enough money to split")
                time.sleep(2)
                SP = False
                continue
            
            for i, hand in enumerate(hands):
                print(f"Playing hand {i + 1}")
                print_hand(hand)

                while calculate_hand_value(hand) < 21 :
                    action =  input("\nDo you want to (h)it or (s)tand: ").lower()
                    if action == "h":
                        os.system('clear')
                        hand.append(deck.pop())
                        print("Your hand: ")
                        print_hand(hand)    
                        time.sleep(2)
                    elif action == "s":
                        break

            os.system('clear')
            print("\nDealer's hand:")
            print_hand(dealer_hand)
            time.sleep(2)

            while calculate_hand_value(dealer_hand) < 17:
                os.system('clear')
                dealer_hand.append(deck.pop())
                print("\nDealer hits:")
                print_hand(dealer_hand)
                time.sleep(2)
            
            dealer_value = calculate_hand_value(dealer_hand)

            for i, hand in enumerate(hands):
                hand_value = calculate_hand_value(hand)
                print(f"\nHand {i+1} total: {hand_value}")
                if hand_value > 21:
                    print("Bust! Dealer wins this hand.")
                elif dealer_value > 21 or hand_value > dealer_value:
                    print("You win this hand!")
                    WALLET += bets[i] * 2
                elif hand_value == dealer_value:
                    print("It's a tie for this hand!")
                    WALLET += bets[i]
                else:
                    print("Dealer wins this hand.")
                time.sleep(2)
            break
        print(WALLET)
        
    if SP != False:
        pass  
    else:            
        player_value = calculate_hand_value(player_hand)

        if player_value > 21:
            users_bet = 0
            print("\nYou bust! Dealer wins.")
        else:
            # Dealer's turn
            os.system('clear')
            print("\nDealer's hand:")
            print_hand(dealer_hand)
            time.sleep(2)

            while calculate_hand_value(dealer_hand) < 17:
                os.system('clear')
                dealer_hand.append(deck.pop())
                print("\nDealer hits:")
                print_hand(dealer_hand)
                time.sleep(2)

            dealer_value = calculate_hand_value(dealer_hand)
            os.system('clear')
            # Determine winner
            print(f"\nYour total: {player_value}")
            print(f"Dealer's total: {dealer_value}")

            if dealer_value > 21 or player_value > dealer_value:
                print("\nYou win!")
                users_bet = users_bet * 2 
                print(f"Money won = {users_bet}")
                WALLET += users_bet
            elif player_value == 21 and len(player_value) == 2:
                print("BLACKJACK!!!!")
                users_bet = int(users_bet * 2.5)  # Correct 3:2 payout
                print(f"Money won = {users_bet}")
                WALLET += users_bet
            elif player_value == dealer_value:
                print("\nIt's a tie!")
                print(f"Money returned = {users_bet}")
                WALLET += users_bet
            else:
                print("\nDealer wins!")
                print(f"Money lost = {users_bet}")
    
    print(f"Balence = {WALLET}")
    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
