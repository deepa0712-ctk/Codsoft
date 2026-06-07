# ==========================================
#  CHATBOT USING
# IF-ELSE + PATTERN MATCHING ONLY
# ==========================================

print("🤖 Welcome to ChatBot")
name = input("what is your name: ")

print("Hello", name, "😊")

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Mood Talk")
    print("2. Study Assistant")
    print("3. Fun Zone")
    print("4. Motivation")
    print("5. Exit")
    print("====================================")
    print("Choose an option using the numbers")
    
    choice = input("Enter your choice: ")

    # ======================================
    # 1. MOOD TALK
    # ======================================
    if choice == "1":

        mood = input("How are you feeling today? ").lower()

        match mood:

            case "happy":
                print("🤖 That's amazing 🌟 Keep smiling!")

            case "sad":
                print("🤖 Don't worry 💙 Everything will be okay.")

            case "bored":
                print("🤖 Let's make your day fun 🎉")

            case "angry":
                print("🤖 Stay calm 😌 Take a deep breath and drink a glass of water🥤.")

            case _:
                print("🤖 Thanks for sharing your feelings 😊")

    # ======================================
    # 2. STUDY ASSISTANT
    # ======================================
    elif choice == "2":

        subject = input("Which subject do you need help with? ").lower()

        match subject:

            case "python":
                print("🤖 Python is easy and powerful 🐍")
                print("🤖 Try making mini projects.")

            case "maths":
                print("🤖 Practice daily to improve maths 📘")

            case "science":
                print("🤖 Science is full of discoveries 🔬")

            case "english":
                print("🤖 Read books to improve English 📖")

            case _:
                print("🤖 Keep studying consistently. For doubts use  websites like Google , YouTube📚")

    # ======================================
    # 3. FUN ZONE
    # ======================================
    elif choice == "3":

        print("\n--- FUN ZONE ---")
        print("1. Joke")
        print("2. Riddle")
        print("3. Fun Fact")

        fun = input("Choose an option: ")

        match fun:

            case "1":

                joke_choice = input(  "Choose joke type (school/computer/general): ").lower()

                match joke_choice:

                    case "school":
                        print("🤖 Why was the math book sad?")
                        print("🤖 Because it had too many problems 😂")

                    case "computer":
                        print("🤖 Why did the computer show up late to work?")
                        print("🤖 because it had a hard drive 😂")

                    case "general":
                        print("🤖 Why don't eggs tell jokes?")
                        print("🤖 because they might crack😂")

                    case _:
                        print("🤖 Funny choice 😄")
            case "2":

                print("🤖 Riddle Time 🧠")
                print("🤖 What has hands but cannot clap?")

                answer = input("Your answer: ").lower()

                if answer == "clock":
                    print("🤖 Correct ⏰🎉")

                else:
                    print("🤖 Wrong 😅 The answer is CLOCK ⏰")

            case "3":

                fact = input(  "Choose fact type (space/animal/food): " ).lower()

                match fact:

                    case "space":
                        print("🤖 The Sun is a star ☀️")

                    case "animal":
                        print("🤖 Octopus has 3 hearts ❤️")

                    case "food":
                        print("🤖 Honey never spoils 🍯")

                    case _:
                        print("🤖 Interesting choice 😄")

            case _:
                print("🤖 Invalid option ❌")

    # ======================================
    # 4. MOTIVATION
    # ======================================
    elif choice == "4":

        motivation = input( "Choose type (study/life/success): " ).lower()

        match motivation:

            case "study":
                print("🤖 Study now and shine later 🌟")

            case "life":
                print("🤖 Every day is a new beginning ☀️")

            case "success":
                print("🤖 Success comes from consistency 🚀")

            case _:
                print("🤖 Keep believing in yourself 💪")

    # ======================================
    # 5. EXIT
    # ======================================
    elif choice == "5":

        print("🤖 Goodbye", name, "👋")
        print("🤖 It was nice talking with you 😊")
        break

    # ======================================
    # INVALID CHOICE
    # ======================================
    else:
        print("🤖 Invalid choice ❌ Please try again.")