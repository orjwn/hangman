# Import the pandas library for data manipulation
import pandas

# Import the os library for operating system-related functions
import os

# Import the tkinter library for creating GUI applications
import tkinter as tk

# Import the messagebox module from tkinter for displaying message boxes
from tkinter import messagebox

# Import the random module for generating random values
import random

# Create a list of animals
animals = ['dog', 'cat', 'fish', 'bird', 'lion', 'tiger', 'elephant', 'monkey', 'zebra', 'panda']


# Define the function to run the hangman game, taking the score as an input
def run_hangman(score):
    # Choose a random animal word from the 'animals' list
    word = random.choice(animals)

    # Initialize a list to store the guessed word with underscores for unguessed letters
    guessed_word = ['_'] * len(word)

    # Create a set to store the guessed letters
    guessed_letters = set()

    # Create a Tkinter window for the hangman game
    root = tk.Tk()
    root.title('Hangman')

    # Create a Tkinter variable to store the score and set its initial value
    score_var = tk.IntVar()
    score_var.set(score)

    # Create a Tkinter variable to store the number of attempts remaining and set its initial value to 6
    attempts_var = tk.IntVar()
    attempts_var.set(6)

    # Create a Tkinter canvas with a size of 300x300 to draw the hangman
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    # List of lambda functions to draw different parts of the hangman on the canvas
    hangman_parts = [
        lambda: canvas.create_line(150, 250, 150, 50),  # Vertical line for the gallows
        lambda: canvas.create_line(150, 50, 100, 50),  # Horizontal line for the gallows
        lambda: canvas.create_line(100, 50, 100, 70),  # Rope
        lambda: canvas.create_oval(90, 70, 110, 90),  # Head
        lambda: canvas.create_line(100, 90, 100, 170),  # Body
        lambda: canvas.create_line(100, 100, 80, 120) and canvas.create_line(100, 100, 120, 120),  # Arms
        lambda: canvas.create_line(100, 170, 80, 200) and canvas.create_line(100, 170, 120, 200)  # Legs
    ]

    # Define the function to update the GUI based on the player's guess
    def update_gui(guess):
        # Check if the guess is not a single letter
        if len(guess) != 1:
            messagebox.showinfo("Error!", "Please enter only one letter.")
            return

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            messagebox.showinfo("Error!", "You've already guessed this letter.")
            return

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guess is correct and update the guessed word accordingly
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            label.config(text=' '.join(guessed_word))
        else:
            # If the guess is incorrect, draw the appropriate part of the hangman and decrement the attempts
            hangman_parts[6 - attempts_var.get()]()
            attempts_var.set(attempts_var.get() - 1)

        # Check if the word has been completely guessed
        if '_' not in guessed_word:
            messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
            score_var.set(score_var.get() + 1)
            root.destroy()
        # Check if the player has run out of attempts
        elif attempts_var.get() == 0:
            messagebox.showinfo("Sorry!", "You didn't guess the word correctly.")
            root.destroy()

    # Create a Tkinter entry widget for the player to enter their guess
    entry = tk.Entry(root)
    entry.pack()

    # Create a Tkinter button labeled 'Guess' to submit the player's guess and call the update_gui function
    button = tk.Button(root, text='Guess', command=lambda: update_gui(entry.get()))
    button.pack()

    # Clear the entry widget after each guess
    entry.delete(0, 'end')

    # Create a Tkinter label to display the guessed word with underscores for unguessed letters
    label = tk.Label(root, text=' '.join(guessed_word))
    label.pack()

    # Start the Tkinter main loop to run the hangman game
    root.mainloop()

    # Return the final score after the game ends
    return score_var.get()


# Function to validate the password
def valid_password(password):
    while True:
        if len(password) < 6 or len(password) > 12:
            print("Make sure your password is between 6 and 12 characters long.")
            password = input("Enter password: ")
        else:
            return password



# Print the main menu options
print("MAIN MENU")
print("Choose 1 or 2 or 3")
main_menu = input("1: Play_game \n2: View Scores \n3: TEST_PROGRAM\n: ")
print('\n' * 50)

# Check the user's choice
if main_menu == "1":
    # Initialize a variable 'a' to True for the while loop
    a = True
    # Start a loop for account creation or login
    while a:
        signin_or_login = input("do you want to create an account y/n: ")
        print('\n' * 50)

        if signin_or_login == "y":
            # Ask the user to input account details
            user_data = {
                'Username': [input("enter your username")],
                'Password': [input("Enter password")],
                'nickname': [input("enter your nickname")]
            }
            print("you have signed in succsefully now PLAAY AND HAVE FUN!!!")
            # Start the hangman game and store the score
            user_data['score'] = run_hangman(0)
            # Create a new DataFrame to store user data

            new_user_df = pandas.DataFrame(user_data)

            # The code provided sets up the main menu and allows the user to create an account if chosen.
            # After account creation, the user can play the hangman game and the score is stored in a DataFrame 'new_user_df'.
            # However, there is no code provided to handle the case when the user chooses option "2: View Scores".
            # Additionally, there is no code to save the user data to a file or perform any further operations with the DataFrame.


            if os.path.exists('user_data.csv'):
                existing_data_df = pandas.read_csv('user_data.csv')
                df = pandas.concat([existing_data_df, new_user_df], ignore_index=True)
            else:
                df = new_user_df

            df.to_csv('user_data.csv', index=False)
            print('\n' * 50)
            a = False
        # Check if user chose not to create an account

        elif signin_or_login == "n":
            # Ask for username and password for login

            username_input = input("Enter your username again: ")

            password_input = input("Enter your password again: ")
            # Read the existing user data from the CSV file
            df = pandas.read_csv("user_data.csv")
            # Check if the provided username and password exist in the DataFrame

            if username_input in df['Username'].values and password_input in df['Password'].values:

                print("You are logged in successfully")
                # Get the current score of the logged-in user

                current_score = df.loc[df['Username'] == username_input, 'score'].values[0]
                # Calculate the new score by playing the hangman game
                new_score = current_score + run_hangman(0)
                # Update the user's score in the DataFrame

                df.loc[df['Username'] == username_input, 'score'] = new_score
                # Save the updated DataFrame to the CSV file

                df.to_csv('user_data.csv', index=False)
                print('\n' * 50)
                a = False
            else:
                print("You entered the wrong password or username")

        else:
            print("Make sure you entered y/n")
elif main_menu == "2":
    # Read the user data from the CSV file
    df = pandas.read_csv('user_data.csv')
    # Extract only the 'nickname' and 'score' columns from the DataFrame
    nickname_and_score = df[['nickname', 'score']]
    print(nickname_and_score)

elif main_menu == "3":
    print("Starting TEST")


    # Function to test CSV file handling
    def test_csv_file():
        # Create a DataFrame with test user data and save it to a test CSV file
        user_data = {
            'Username': ['test_user'],
            'Password': ['TestPass'],
            'nickname': ['test'],
            'score': [0]
        }
        df = pandas.DataFrame(user_data)
        df.to_csv('test_data.csv', index=False)
        # Read the test CSV file and compare it with the original DataFrame


        read_df = pandas.read_csv('test_data.csv')
        assert read_df.equals(df), "CSV file test failed."
        # Remove the test CSV file after testing


        os.remove('test_data.csv')

    # Function to test the 'run_hangman' function
    def test_run_hangman():

        print("a test will start now play a game of hangman for testing purposes")
        score = run_hangman(0)

        assert type(score) == type(1), f"Expected an integer score, but got {type(score)}"
    # Function to test the 'valid_password' function
    def test_password():
        assert valid_password("A123456789") == "A123456789", 'TEST FAILED THE OUTPUT IS NOT WHAT IS EXPECTED'
    # Run the individual tests
    test_password()
    test_run_hangman()
    test_csv_file()
    # Print a message indicating that all tests passed successfully
    print("All tests passed!")
else:
    print("make sure you entered 1 or 2 or 3")
