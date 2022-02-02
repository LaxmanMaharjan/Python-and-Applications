import time,os
from random import randint
lifeline = 5
questions = { "Capital of Nepal?":"kathmandu",
                  "Capital of China?":"beijing",
                  "Pirates of ?":"caribbean",
                }


def load_game():
    # printing welcome greetings and starting game.
    print(f"""
{'#'*35}
    
             Welcome
               To
             Hangman

    Enter anything to continue!!
    
{'#'*35}
    """)
    input()
    os.system('clear')
    print("""
Rules for Hangman:

1. You have 5 lifelines.
2. Enter 'y' for 'yes' and 'n' for 'no', Entering anything else is considered 'no'.
3. Game is not case sensitive.
    """)
    
    choice = input("Do want to continue to play? ['y'=yes, 'n'=no]:").lower()
    os.system('clear')
    if choice == 'y':
        hangman()
    
def check_solution(question, answer, count):
    # checking character entered with answer character by character
    # i.e index by index
    if answer == questions[question][count]:
        print('\nCorrect Guess!')
        return True
    else:
        # using global lifeline variable since it is used by other function as well.
        global lifeline
        lifeline -= 1
        print(f'\nIncorrect Guess!')
        return False

def hangman():
    
    global lifeline
    # length of questions to generate random question
    length = len(questions.keys())    

    # infinite loop until player wants to play the game
    while(1):
        # counts the index 
        count = 0
        # random choice of question
        choice = randint(0,length-1)
        question = list(questions.keys())[choice]
        correct_guesses = ""
        while(lifeline>0):
            print(f"Lifeline:{lifeline}")
            print(f'\nQuestion:{question}')
            print(f"\nYour Answer so far:{correct_guesses}")
            ans = input('\nEnter the letter:').lower()
            if check_solution(question, ans, count):
                # add in correct_guesses if guess is correct and increase index
                correct_guesses += ans
                count += 1
                # solution is checked index by index and word by word
                if correct_guesses == questions[question]:
                    print(f"\nCorrect Answer:{correct_guesses}\nYou Win")
                    break

            time.sleep(1) 
            os.system('clear')
        
        if lifeline == 0:
            print("\nYour lifeline finished!\n\nYou Lose")

        choice2 = input("\nDo you want to play again ['y'=yes 'n'=no]:").lower()

        if choice2 == 'y':
            lifeline = 5
            os.system('clear')
            continue
        else:
            break

if __name__ == "__main__":
    load_game()
    
    


























