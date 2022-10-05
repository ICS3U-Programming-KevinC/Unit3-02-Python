# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 5, 2022
# This program tells the user to guess between 0 and 9,
# then checks if they are correct


import constants


def main():
    # ask user for their guess
    print("I'm thinking of a number between 0 and 9,")
    user_guess = int(input("What's your guess? "))

    # add extra line
    print("")

    # checks if the user's guess is correct
    if user_guess == constants.SECRET_NUMBER:

        # if it is congratulate them
        print("Congratulations!, you guessed correctly")

    # checks if the user's guess is incorrect
    elif user_guess != constants.SECRET_NUMBER:

        # if it is tell them
        print("Incorrect, try again some other time")


if __name__ == "__main__":
    main()
