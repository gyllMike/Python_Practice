#Game Name: Black Jack
#Author: Mike Yulin Guo
#Date: December24 2023
#Game Rule:

#You will get 2 number at beginning (one is original number, one is new number), your rival as well
#Then, you need to input "hit" or "stand", remember your number can not bigger than 21
#if your number bigger than 21, you will loss.
#If rival's number biiger than 21, you win. If your rival's and your number both lower than 21, but your number is
#bigger than your rival's number you win. Conversely, you loss.
#You will get a ramdom money at first, then you need to input how much money you want to bet.
#If you win, your money will be: initial money + bet money
#if you loss, your money will be : initial money  - bet money
#When you input stand, you have entered the comparative stage
#When you input hit, you can hit always untill you input stand
#NOTICE: You can only stand twice at most, and the second input of stand will enter the comparison stage

#HAVE A GOOD GAME10
#=======================================================================================================================

import random

class BlackJackGame:

    def __init__(self):
        self.player_card = self.let_random_cards()
        self.player_fcard = self.let_random_cards()
        self.computer_card = self.let_random_cards()
        self.computer_fcard = self.let_random_cards()
        self.player_money = self.let_random_money()

    def let_random_cards(self):
        return random.randint(1, 13)

    def let_random_money(self):
        return random.randint(10, 100)

    def is_hit(self, bet):
        new_card = self.let_random_cards()
        print("HH you get a new number", new_card)
        self.player_card += new_card
        print("HH your number now is", self.player_card)

        if self.player_card > 21:
            print("You lose")
            self.player_money -= bet
            if self.player_money < 0:
                self.player_money = 0
            print("Now your money is", self.player_money)
            play_again = input("If you want to play again please input yes / no")
            if play_again.lower() == "yes":
                self.__init__()
                self.begin()
            else:
                print("YOU OUT OF GAME")
                return False

        print("HH This is your final number", self.player_card,
              "if you want to continue please put hit, if you don't want to continue please put stand")
        return True

    def is_stand(self, bet):
        while True:
            rival_new_card = self.let_random_cards()
            print("SS Your rival gets a new number", rival_new_card)
            self.computer_card += rival_new_card
            print("SS Now your rival's final number is", self.computer_card)

            if self.computer_card > 21:
                print("You win")
                self.player_money += 2 * bet
                print("Your money now is", self.player_money)
                play_again = input("If you want to play again please input yes / no")
                if play_again.lower() == "yes":
                    self.__init__()
                    self.begin()
                else:
                    print("YOU OUT OF GAME")
                return False

            print("SS Your number now is", self.player_card)

            next_move = input("if you want to continue please put hit, if you don't want to continue please put stand")

            if next_move.lower() == "hit":
                self.is_hit(bet)
            elif next_move.lower() == "stand":
                continue

            if self.computer_card > 21 or (self.computer_card < self.player_card and self.computer_card < 21):
                print("You win")
                self.player_money += 2 * bet
                print("Your money now is", self.player_money)
                play_again = input("If you want to play again please input yes / no")
                if play_again.lower() == "yes":
                    self.__init__()
                    self.begin()
                else:
                    print("YOU OUT OF GAME")
                return False

            elif self.player_card > 21 or (self.computer_card > self.player_card and self.computer_card < 21):
                print("You lose")
                self.player_money -= bet
                if self.player_money < 0:
                    self.player_money = 0
                print("Now your money is", self.player_money)
                play_again = input("If you want to play again please input yes / no")
                if play_again.lower() == "yes":
                    self.__init__()
                    self.begin()
                else:
                    print("YOU OUT OF GAME")
                return False

    def begin(self):
        print("Now your money is", self.player_money)
        bet = 0
        bet = int(input("Please put the money you want to bet"))

        if bet > self.player_money:
            print("You can't bet more than you have.")
            self.begin()
            return

        self.player_money -= bet
        print("After bet your money is", self.player_money)

        print("======================")
        print("Now your number is:", self.player_card)
        print("Now you get new number", self.player_fcard)
        print("======================")

        self.player_card += self.player_fcard

        print("======================")
        print("Your rival's number is", self.computer_card)
        print("Your rival got a new number", self.computer_fcard)
        print("======================")

        self.computer_card += self.computer_fcard

        print("======================")
        print("Your rival's final number is", self.computer_card)
        print("This is your final number", self.player_card,
              "if you want to continue please put hit, if you don't want to continue please put stand")

        if self.player_card > 21:
            print("YOU LOSE")
            self.player_money -= bet
            if self.player_money < 0:
                self.player_money = 0
            print("Now your money is", self.player_money)
            play_again = input("If you want to play again please input yes / no")
            if play_again.lower() == "yes":
                self.__init__()
                self.begin()
            else:
                print("YOU OUT OF GAME")

        while True:
            next_move = input("")

            if next_move.lower() == "hit":
                if not self.is_hit(bet):
                    return
            elif next_move.lower() == "stand":
                if not self.is_stand(bet):
                    return

blackjack = BlackJackGame()
blackjack.begin()