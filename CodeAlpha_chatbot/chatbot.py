def chatbot():
    print("ChatBot Started! (Type,'Bye'to exit)")
    while True:
        user=input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I Am Fine,Thanks!")
        elif user == "bye":
            print("Bot: GoodBye!")
            break
        else:
            print("Bot: I Don't Understand.")
chatbot()