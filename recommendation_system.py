# ==========================================
# MOVIE & BOOK RECOMMENDATION SYSTEM
# Using Content-Based + Collaborative Filtering
# ==========================================

print("\n===== RECOMMENDATION SYSTEM =====")

print("\nChoose Category")
print("1. Movies")
print("2. Books")

category = input("\nEnter choice: ")

print("\nChoose Recommendation Method")
print("1. Content-Based Filtering")
print("2. Collaborative Filtering")

method = input("Enter method: ")


# ==================================
# MOVIE RECOMMENDATION
# ==================================

if category == "1":

    if method == "1":

        print("\nMovie Genres")
        print("action")
        print("comedy")
        print("romance")
        print("thriller")

        genre = input("\nEnter genre: ").lower()

        movie_data = {

            "action": [
                "John Wick",
                "Avengers",
                "Mission Impossible"
            ],

            "comedy": [
                "Home Alone",
                "Jumanji",
                "Mr Bean"
            ],

            "romance": [
                "Titanic",
                "The Notebook",
                "La La Land"
            ],

            "thriller": [
                "Inception",
                "Shutter Island",
                "Gone Girl"
            ]
        }

        if genre in movie_data:

            print("\nRecommended Movies:")
            for movie in movie_data[genre]:
                print("→", movie)

        else:
            print("Genre not available")


    elif method == "2":

        print("\nSimilar users choices:")
        print("User A liked: Avengers")
        print("User B liked: John Wick")
        print("User C liked: Titanic")

        user = input("\nChoose user (A/B/C): ").upper()

        if user == "A":
            print("\nUsers similar to A also watched:")
            print("→ Iron Man")
            print("→ Black Panther")

        elif user == "B":
            print("\nUsers similar to B also watched:")
            print("→ Extraction")
            print("→ Fast & Furious")

        elif user == "C":
            print("\nUsers similar to C also watched:")
            print("→ Me Before You")
            print("→ The Vow")

        else:
            print("User not found")


# ==================================
# BOOK RECOMMENDATION
# ==================================

elif category == "2":

    if method == "1":

        print("\nBook Types")
        print("fiction")
        print("science")
        print("motivation")

        book = input("\nEnter type: ").lower()

        books = {

            "fiction": [
                "Harry Potter",
                "The Alchemist",
                "The Hobbit"
            ],

            "science": [
                "Cosmos",
                "A Brief History of Time",
                "The Selfish Gene"
            ],

            "motivation": [
                "Atomic Habits",
                "Think and Grow Rich",
                "Rich Dad Poor Dad"
            ]
        }

        if book in books:

            print("\nRecommended Books:")
            for i in books[book]:
                print("→", i)

        else:
            print("Type not available")


    elif method == "2":

        print("\nReader Profiles:")
        print("Reader X → Harry Potter")
        print("Reader Y → Atomic Habits")
        print("Reader Z → Cosmos")

        reader = input("\nChoose reader (X/Y/Z): ").upper()

        if reader == "X":
            print("\nSimilar readers also enjoyed:")
            print("→ Percy Jackson")
            print("→ Narnia")

        elif reader == "Y":
            print("\nSimilar readers also enjoyed:")
            print("→ Deep Work")
            print("→ The Power of Habit")

        elif reader == "Z":
            print("\nSimilar readers also enjoyed:")
            print("→ Astrophysics for People in a Hurry")
            print("→ The Elegant Universe")

        else:
            print("Reader not found")

else:
    print("\nInvalid Choice")

print("\nThank You!🙂")