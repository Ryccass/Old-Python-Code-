from os import system, name
import random
import time



def clear(): 
   
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

def loading():
    print("Loading.")
    time.sleep(1)
    clear()
    print("Loading. .")
    time.sleep(1)
    clear()
    print("Loading. . .")
    time.sleep(1)
    clear()

def guessing_game():
    number_of_guesses = 0
    is_playing = True
    correct_answer = random.randint(1, 9)
    clear()
    print("Welcome to the Guessing Game!")
    print("Type \"exit\" to quit the game.")
    time.sleep(0.5)
    print("Generating a random number from 1 to 9 (including!)...")
    time.sleep(1.5)
    clear()
    loading()

    while is_playing:

        
        
        print("Please enter your guess!")

        print(correct_answer)
        user_guess = input("\n")
        
        if user_guess == "exit":
            is_playing = False
            break
            
        elif int(user_guess) == correct_answer:
            print("Congratulations! You've beaten the guessing game in " + str(number_of_guesses) + " tries!")
            print("The correct answer was " + str(correct_answer) + ".")
            
            print("Do you want to play again? (y/n; yes/no)")
            play_again = input("\n")
            if play_again == 'n' or play_again == 'no':
                is_playing = False
                break
            elif play_again == 'y' or play_again == 'yes':
                guessing_game()
        
        elif int(user_guess) < 1:
            print("Please enter a number between 1 and 9 (including!). Try again.")
        elif int(user_guess) > 9:
            print("Please enter a number between 1 and 9 (including!). Try again.")
        elif int(user_guess) < correct_answer:
            print("Your guess is too low! Try again!")
            number_of_guesses += 1
        elif int(user_guess) > correct_answer:
            print("Your guess is too high! Try again!")
            number_of_guesses += 1
        
        

guessing_game()
