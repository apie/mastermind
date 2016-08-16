# Mastermind - Guess the code
Available 'colors' are: 1,2,3,4,5,6.
The code consists of a combination of 4 unique colors.
You can guess 10 times before the game is over.
Input your guess like this: '1234'.

After each guess the computer returns how many items were guessed correct (this is indicated by a '2')
and how many colors were guessed correct but had an incorrect position. (this is indicated by a '1').
So if you get [2, 2, 2, 2] the guess was correct.
If you guess the code within 10 tries, you win!

Description
-----------
Main script is mastermind.py.
Interactive mode is started by just running the script. 'Savegame' mode works by providing your guess as an argument on the commandline. The status is then saved in a pickle file. The web version also works with this mode.

Files for the web version are in web/. Mastermind.php calls mastermind.py.

Todo
----
Support for multiple users by letting users enter their name and saving the name in the status file as well.

