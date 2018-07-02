
#function is requesting a guess from user and checking if it is equal to the random number.
def guess(randomNumber):
    userNumber = input("Guess a number: ")

    try:
        userNumber = int (userNumber)

    except:
        print("Invalid number. So using zero in the place.")
        userNumber = 0

    win = False

    if userNumber == randomNumber:
        win = True
        print("Congratulations! you guessed it right.")

    elif userNumber < randomNumber:
        if (randomNumber - userNumber < 20):
            print("It's not the right number. The required number is greater than this number and is close to this number.")

        else:
            print("It's not the right number. The required number is far greater than this number.")

    elif userNumber > randomNumber:
        if (userNumber - randomNumber < 20):
            print("It's not the right number. The required number is less than this number and is close to this number.")

        else:
            print("It's not the right number. The required number is far less than this number.")

    return win

import random

def main():
    print("You will guess a number between 1-100. You have five tries.")

    randomNumber = random.randint(1,100)


    win = guess(randomNumber)
#if the guess is right the game ends, but if it is wrong the user gets upto 5 chance to guess right
    if win == False:

        win = guess(randomNumber)

        if win == False:

            win = guess(randomNumber)

            if win == False:


                win = guess(randomNumber)

                if win == False:


                    win = guess(randomNumber)

                    if win == False:
                        print("Sorry all you guesses were wrong.")
                        print("The correct number was", randomNumber)
#if all the answers are wrong than program ends saying "All guesses are wrong"
main()














