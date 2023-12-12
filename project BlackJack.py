#Game Name: Black Jack
#Author: Mike Yulin Guo
#Date: October4 2023
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

def is_hit(k, n, b, c, money, bet):

    while True:
        print("HH you get new number", n)
        k += n
        print("HH your number now is", k)

        if k > 21:
            print("you loss")
            money -= bet
            if money < 0:
                money = 0
            print("Now your money is", money)
            play_again = input("If you want to play again please input yes / no")
            if play_again == "yes":
                Black_Jack()
            elif play_again == "no":
                break
            return False

        print("HH This is your final number", k,
              "if you want continue please put hit, if you don't want continue please"
              "put stand")
        next_move = input("")

        if next_move == "hit":
            n = random.randint(1, 13)
        elif next_move == "stand":
            is_stand(b, c, k, n, money, bet)
            break

#=======================================================================================================================

def is_stand(b, c, k, n, money, bet):

    while True:
        b = random.randint(1, 13)
        print("SS Now your rival gets a new number", b)
        c += b
        print("SS Now your rival's final number is", c)

        if c > 21:
            print("YOU WIN")
            money = money + 2 * bet
            print("Your money now is", money)
            play_again = input("If you want to play again please input yes / no")
            if play_again == "yes":
                Black_Jack()
            elif play_again == "no":
                return False

        print("SS Your number now is", k)
        print("if you want continue please put hit, if you don't want continue please")
        next_move = input("")

        if next_move == "hit":
            n = random.randint(1, 13)
            is_hit(k, n, b, c, money, bet)
        elif next_move == "stand":
            pass

        if c > 21 or (c < k and c < 21):
            print("YOU WIN")
            money = money + 2 * bet
            print("Your money now is", money)
            play_again = input("If you want to play again please input yes / no")
            if play_again == "yes":
                Black_Jack()
            elif play_again == "no":
                return False

        elif k > 21 or (c > k and c < 21):
            print("YOU LOSS")
            money -= bet
            if money < 0:
                money = 0
            print("Now your money is", money)
            play_again = input("If you want to play again please input yes / no")
            if play_again == "yes":
                Black_Jack()
            elif play_again == "no":
                return False

#=======================================================================================================================

def Black_Jack():

    k = random.randint(1, 13)
    n = random.randint(1, 13)
    n = int(n)
    k = int(k)

    c = random.randint(1, 13)
    b = random.randint(1, 13)
    b = int(b)
    c = int(c)

    money = random.randint(1, 100)
    bet = 0
    money = int(money)
    bet = int(bet)


    while k <= 21 and c <= 21:
        print("Now your money is", money)
        bet = int(input("Please put the money you want to bet"))

        if bet > money:
            print("You can't bet more than you have.")
            continue

        money -= bet
        print("After bet your money is", money)
        print("Now your bet money is", bet)

        while True:
            print("======================")
            print("Now your number is:", k)
            print("Now you get new number", n)
            print("======================")
            k += n
            print("======================")
            print("your rival's number is", c)
            print("your rival got a new number", b)
            print("======================")
            c += b
            print("======================")
            print("your rival's final number is", c)
            print("This is your final number", k,
                  "if you want continue please put hit, if you don't want continue please"
                  "put stand")

            if k > 21:
                print("YOU LOSS")
                money -= bet
                if money < 0:
                    money = 0
                print("Now your money is", money)
                play_again = input("If you want to play again please input yes / no")
                if play_again == "yes":
                    Black_Jack()
                elif play_again == "no":
                    break


            next_move = input("")

            if next_move == "hit":
                n = random.randint(1, 13)
                is_hit(k, n, b, c, money, bet)
            elif next_move == "stand":
                is_stand(b, c, k, n, money, bet)
                break

#=======================================================================================================================

            if c > 21 or (c < k and c < 21 and k <21):
                print("YOU WIN")
                money = money + 2 * bet
                print("Your money now is", money)
                play_again = input("If you want to play again please input yes / no")
                if play_again == "yes":
                    Black_Jack()
                elif play_again == "no":
                    return False

            elif k > 21 or (c > k and c < 21):
                print("YOU LOSS")
                money -= bet
                if money < 0:
                    money = 0
                print("Now your money is", money)
                play_again = input("If you want to play again please input yes / no")
                if play_again == "yes":
                    Black_Jack()
                elif play_again == "no":
                    return False

#=======================================================================================================================

Black_Jack()