# Hangman Game 🎮

A simple **Hangman word guessing game** made using Python.
The program randomly selects a word, and the player has to guess it letter by letter before running out of attempts.

---

## 📌 Features

* Random word selection using `random.choice()`
* Tracks guessed letters
* Shows hidden word using `_`
* Limits wrong attempts to 6
* Displays win or game over message

---

## 🛠 Requirements

* Python 3.x

No extra libraries are needed because the program only uses Python's built-in `random` module.

---

## ▶️ How to Run

1. Save the code in a file named `hangman.py`
2. Open terminal or command prompt
3. Run the program:

```bash
python hangman.py
```

---

## 🎯 How to Play

* The game chooses a random word.
* You enter one letter at a time.
* Correct letters appear in the word.
* Wrong guesses reduce remaining attempts.
* You win if you guess the complete word before attempts end.

---

## 📄 Example Output

```text
^^^ Welcome To Hangman! ^^^

word: _____
Enter a Letter: a
Correct!

word: _a___
Enter a Letter: z
Wrong! Attempts Left: 5
```

---

## 📚 Concepts Used

* Lists
* Loops (`while`, `for`)
* Conditional statements (`if-else`)
* String handling
* User input
* Random module

---

## 🧠 Word List Used

```python
["mango","bmw","rose","seven","travel"]
```

You can add more words to make the game more interesting.

---

## 🚀 Future Improvements

* Add difficulty levels
* Add hint system
* Use ASCII art for hangman
* Add score tracking
* Allow multiplayer mode

---

## 👨‍💻 Author
Humaira Kagzi


Python Mini Project - Hangman Game
