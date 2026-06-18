import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
start = input("Do you want to play a game of BLACKJACK? type 'y' if yes and 'n' if no:\n").lower()
def total(cards_list):
    total = sum(cards_list)
    while total > 21 and 11 in cards_list:
        cards_list[cards_list.index(11)]=1
        total = sum(cards_list)
    return total
while True:

    if start == "y":
        your_cards =random.sample(cards,2)
        computer_cards = random.sample(cards,2)

        print(f"your card= {your_cards}")
        print(f"computer's first card= {computer_cards[0]}")
        while True:
            next_card= input("type 'y' to get another card, or type 'n' to pass:\n")
            if next_card == "y":
                your_cards.append(random.choice(cards))
                print(f"your new cards are:{total(your_cards)}")
                your_total= total(your_cards)
                if your_total > 21:
                    print("you are busted!")
                    break
            elif next_card == "n":
                your_total= total(your_cards)
                computer_total= total(computer_cards)

                print(f"your new card= {your_cards}, total= {total(your_cards)}")
                print(f"computer's cards= {computer_cards}, total= {total(computer_cards)}")

                if your_total > 21:
                    print("you are busted!")
                elif computer_total > 21:
                    print("you won!")
                elif your_total <= 21 and your_total > computer_total:
                    print("you won!")
                elif computer_total <= 21 and computer_total > your_total:
                    print("you are busted!")
                elif your_total == computer_total or your_total == computer_total == 21:
                    print("it is a tie")
                break
        play_again = input("do u want to play the game again?'y' for yes, and 'n' for no:\n").lower()
        if play_again == "n":
            break

    
    else:
        print("bye!")           
        break
        