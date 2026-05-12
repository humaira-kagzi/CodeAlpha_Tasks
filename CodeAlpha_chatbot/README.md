# 🤖 Simple Python ChatBot

A basic command-line chatbot made using Python 🐍.
This chatbot responds to simple user messages like greetings 👋 and exits when the user types `"bye"` 🚪.

---

## ✨ Features

* 💬 Responds to basic greetings
* 🔁 Uses loops for continuous chatting
* 🧠 Uses `if-elif-else` conditions
* 👨‍💻 Beginner-friendly project
* ⚡ Simple and easy to understand

---

## 🛠️ Technologies Used

* 🐍 Python 3

---

## 📄 Code

```python
def chatbot():
    print("🤖 ChatBot Started! (Type 'bye' to exit)")

    while True:
        user = input("🧑 You: ")

        if user == "hello":
            print("🤖 Bot: Hi!")

        elif user == "how are you":
            print("🤖 Bot: I Am Fine, Thanks!")

        elif user == "bye":
            print("🤖 Bot: GoodBye! 👋")
            break

        else:
            print("🤖 Bot: I Don't Understand ❓")

chatbot()
```

---

## ▶️ How to Run

1. 📥 Install Python on your computer
2. 💾 Save the code in a file named `chatbot.py`
3. 💻 Open Terminal / Command Prompt
4. 🚀 Run the following command:

```bash
python chatbot.py
```

---

## 🧪 Example Output

```text
🤖 ChatBot Started! (Type 'bye' to exit)

🧑 You: hello
🤖 Bot: Hi!

🧑 You: how are you
🤖 Bot: I Am Fine, Thanks!

🧑 You: bye
🤖 Bot: GoodBye! 👋
```

---

## 📚 Concepts Used

* 🧩 Functions
* 🔁 Loops (`while`)
* ⚖️ Conditional Statements (`if-elif-else`)
* ⌨️ User Input (`input()`)

---

## 🚀 Future Improvements

* ➕ Add more chatbot responses
* 🔤 Make chatbot case-insensitive
* 🧠 Add AI/NLP features
* 🖼️ Create GUI version
* 🎤 Add voice support

---

## 👩‍💻 Author
Humaira Kagzi


Made with ❤️ using Python for learning purposes.
