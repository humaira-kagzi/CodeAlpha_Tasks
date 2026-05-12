import random
words=["mango","bmw","rose","seven","travel"]
word=random.choice(words)

guessed_letters=[]
wrong_guesses=0
max_attempts=6

print("^^^ Welcome To Hangman! ^^^")

while wrong_guesses<max_attempts:
    display =""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display+="_"
    print("word:",display)

    if display==word:
        print("Congratulations You Guessed The Word!")
        break
    
    guess=input("Enter a Letter:").lower()

    if guess in guessed_letters:
        print("Already Guessed!")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        guessed_letters.append(guess)
        wrong_guesses += 1
        print("Wrong! Attempts Left:",max_attempts-wrong_guesses)
    
    if wrong_guesses == max_attempts:
        print("Game Over! Word Was:",word)



