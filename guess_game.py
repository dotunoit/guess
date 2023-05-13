{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70e29e08",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import random module for random number to be used in the game\n",
    "import random\n",
    "#Accept player name as input\n",
    "player_name = input(\"What's your name? \")\n",
    "print(f\"Hello, {player_name}! Let's play a game.\")\n",
    "#Specify the random number (integer) to be between 1-100\n",
    "secret_number = random.randint(1, 100)\n",
    "print(\"I will pick a number between 1 and 100.\")\n",
    "print(\"You have 9 attempts to guess it.\")\n",
    "\n",
    "no_of_guesses = 0\n",
    "guesses_left = 9\n",
    "\n",
    "while no_of_guesses < 9:\n",
    "    try:\n",
    "        guess = int(input(\"Take a guess: \"))\n",
    "        if 1 <= guess <= 100:\n",
    "            if guess < secret_number:\n",
    "                print(\"Your guess is too low!\")\n",
    "            elif guess > secret_number:\n",
    "                print(\"Your guess is too high!\")\n",
    "# In a rare case where the player guesses right the first time, the system shouldn't print '1 attempts' but 'first attempt' \n",
    "            else:\n",
    "                if no_of_guesses == 0:\n",
    "                    print(f\"Yes, {player_name}! You guessed the number correctly in the first attempt.\")\n",
    "                else:\n",
    "                    print(f\"Yes, {player_name}! You guessed the number correctly in the {no_of_guesses + 1}th attempt.\")\n",
    "                break\n",
    "# The variables below are to give count of guesses left\n",
    "            no_of_guesses += 1\n",
    "            guesses_left -= 1\n",
    "            print(f\"Wrong guess! You have {guesses_left} attempts remaining.\")\n",
    "#To give error message when strings or numbers outside the range 1 and 100 are entered\n",
    "        else:\n",
    "            print(\"Please enter a number between 1 and 100.\")\n",
    "    except ValueError:\n",
    "        print(\"Please enter a number between 1 and 100.\")\n",
    "#To terminate after the 9th try\n",
    "if no_of_guesses == 9:\n",
    "    print(f\"Sorry, {player_name}. After the 9th try, you couldn't guess the number. The number was {secret_number}.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
