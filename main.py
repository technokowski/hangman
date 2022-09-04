import random

"""
A quick attempt at a hangman game. I'm trying to learn how to write
better comments so I can use these examples in my lesson planning. 
Much of the code is pretty verbose and unpythonic, but it's intentional;
this is supposed to be for beginners. Ideally, it would be nice to
check the user's answer to make sure it only contains one letter,
but this works well regardless. 
"""

# This will be a list containing the exact amount of characters in the
# selected choice from mix_words. Add more to make it more exciting.
secret = []
mix_of_words = ['picard','kirk','cisco','archer']
word = random.choice(mix_of_words)

# Number of guesses they can get wrong
guess_attempts = 4

# Based on the word, the * character will populate the secret list
for i in word:
    secret.append('*')

# Will display the list so the user has an idea of how many letters it is
print("Here is your Secret word:")
print(secret)
print(f"You have {guess_attempts} chances to get it wrong. Good Luck!")

# Begin loop.
while guess_attempts > 0:
    guess = input('guess a letter: ')
    num = 0
    was_it_wrong = True
    # loops through the word and checks if the guess 
    # is contained in each character. This way, if there are multiple, it 
    # checks those as well
    for i in word:
        # If guess is in the character position of the word 
        # it changes the corresponding index in the secret list
        if i == guess:
            # If the guess is correct, it changes to False
            was_it_wrong = False
            secret[num] = guess
        else:
            pass
        # Used to increment the index. There are a lot of ways to do this...
        num = num + 1

    # This checks if the guess had any successful matches. 
    # If True, it means the the guess was unsuccessful 
    # and decrements the guess_attempts by 1
    if was_it_wrong == True:
        guess_attempts = guess_attempts - 1
        print ("WRONG")
        print(f"You have {guess_attempts} chances left.")
        
    joined_word = ''.join(secret)
    
    # This will end the game if the word matches the joined_word
    if joined_word == word:
        print("Congratulations, you guessed it!")
        guess_attempts = 0
    
    print(joined_word)
    
