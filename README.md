# guess game

This code implements a simple guessing game where the player needs to guess a randomly generated number. 
Breaking it down below
The random module is imported, which allows us to generate random numbers.
The player's name is accepted as input using the input() function and stored in the variable player_name.
A welcome message is printed using the player's name previously entered.
The code generates a random integer between 1 and 100 using the random.randint() function and stores it in the variable secret_number.
Instructions for the game are printed, informing the player about the number range (1 to 100) and the number of attempts allowed (9 attempts).
The variable guesses_taken is initialized to 0 to keep track of the number of guesses the player has made.
A while loop is used to repeatedly prompt the player for a guess until they reach the maximum number of allowed attempts (9 attempts).
Inside the loop, the player's guess is obtained using the input() function and converted to an integer using int(). It is stored in the variable guess.
The code then checks the player's guess against the secret_number and provides feedback. If the guess is lower than the secret number, it prints "Your guess is too low!" If the guess is higher, it prints "Your guess is too high!"
If the player's guess is equal to the secret_number, it prints a success message, indicating the number of attempts it took to guess correctly. The loop is then terminated using break.
If the player exhausts all the attempts (reaches the maximum of 9 guesses) without guessing the correct number, it prints a failure message, revealing the secret_number.
