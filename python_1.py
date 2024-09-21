import random
print("I'm thinking of a number between 1 and 10, can you guess it?!!")

def guess_game():
    secret_number = random.randint(1,10)
    attempts = 0

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        match guess:
            case _ if guess == secret_number:
                print(f"Congratulations! you guessed the number in {attempts} attempts")
                break
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
        
    play_again = input("Do you want to play again (yes/no)").lower()
    if play_again == "yes":
        guess_game()
    else:
        print("Thank you for playing")

guess_game()
        
            

