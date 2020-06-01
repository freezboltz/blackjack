#!/usr/bin/python3
"""
Program docstring:
Author: Anant Murmu

#####################
#   BLACKJACK Game  #
#####################

Rules:

* Players are each dealt two cards, face up or down depending on the casino and the table.
* The dealer is also dealt two cards, normally one up (exposed) and one down (hidden).
* The value of cards two through ten is their pip value (2 through 10).
* Face cards (Jack, Queen, and King) are all worth ten.
* Aces can be worth one or eleven.
* A hand's value is the sum of the card values. 
* Players are allowed to draw additional cards to improve their hands. 
* A hand with an ace valued as 11 is called "soft", meaning that the hand will not bust by taking an additional card. 
* The value of the ace will become one to prevent the hand from exceeding 21. Otherwise, the hand is called "hard". 
* Once all the players have completed their hands, it is the dealer's turn. 
* The dealer hand will not be completed if all players have either busted or received blackjacks. 
* The dealer then reveals the hidden card and must hit until the cards total up to 17 points. 
* At 17 points or higher the dealer must stay. 
    (At most tables the dealer also hits on a "soft" 17, 
    i.e. a hand containing an ace and one or more other cards totaling six.) 
* You are betting that you have a better hand than the dealer. 
* The better hand is the hand where the sum of the card values is closer to 21 without exceeding 21. 
* The detailed outcome of the hand follows:
    * If the player is dealt an Ace and a ten-value card (called a "blackjack" or "natural"), and the dealer does not, the player wins and usually receives a bonus.
    * If the player exceeds a sum of 21 ("busts"); the player loses, even if the dealer also exceeds 21.
    * If the dealer exceeds 21 ("busts") and the player does not; the player wins.
    * If the player attains a final sum higher than the dealer and does not bust; the player wins.
    * If both dealer and player receive a blackjack or any other hands with the same sum, called a "push", no one wins.
* POWER OF ACE
    * By default ace is considered as 11 point
    * But if your card value count is over 21 then ace will be considered as 1 to save you from bust.
"""
import os
import random

Deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4


def deal(deck):
    hand = []
    for _ in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand


def one_or_eleven(input_num_list):
    """
    Taken care of value of ace in every situation
    """
    iterator = len(input_num_list)
    while sum(input_num_list) > 21:
        if input_num_list[iterator-1] == 11:
            input_num_list[iterator-1] = 1
        iterator -= 1
        if iterator == 0:
            break


def total(input_list):
    t = []
    for card in input_list:
        if card == "J" or card == "Q" or card == "K":
            t.append(10)
        elif card == "A":
            t.append(11)
        else:
            t.append(card)
    one_or_eleven(t)
    return sum(t)


def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        game()
    elif again != "n":
        print("Please answer in (Y/N)")
        play_again()
    else:
        print("Bye!")
        exit()


def hit(hand):
    card = Deck.pop()
    hand.append(card)
    return hand


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def print_results(dealer_hand, player_hand):
    clear()
    print("The dealer has a " + str(dealer_hand) +
          " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) +
          " for a total of " + str(total(player_hand)))


def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Congratulations. Your score is higher than the dealer. You win\n")


def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()


def game():
    choice = 0
    clear()
    print("WELCOME TO BLACKJACK!\n")
    dealer_hand = deal(Deck)
    player_hand = deal(Deck)
    while choice != "q":
        print("The dealer is showing a " + str(dealer_hand[1]))
        print("You have a " + str(player_hand) +
              " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input(
            "Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        dealer_s_turn = False
        if choice == "h":
            hit(player_hand)
            dealer_s_turn = True

        elif choice == "s":
            dealer_s_turn = True

        elif choice == "q":
            print("Bye!")
            exit()
        else:
            print(
                "Please press (H/S/Q) in your keyboard for [H]it, [S]tand or [Q]uit respectively to proceed.")

        if dealer_s_turn:
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()


if __name__ == "__main__":
    game()
