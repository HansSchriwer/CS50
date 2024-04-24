# Flashcard Quiz Game Final Project for CS50

# This program allows users to create and study flashcards.
# Users can add new flashcards, view existing flashcards, and quiz themselves.

# Initialize an empty dictionary to store flashcards (question: answer)
flashcards = {}

def add_flashcard():
    """Add a new flashcard to the dictionary."""
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flashcards[question] = answer
    print("Flashcard added successfully!")

def view_flashcards():
    """View all existing flashcards."""
    if not flashcards:
        print("No flashcards found.")
    else:
        print("Flashcards:")
        for question, answer in flashcards.items():
            print(f"Q: {question} | A: {answer}")

def quiz():
    """Quiz the user on flashcards."""
    if not flashcards:
        print("No flashcards available for quiz.")
        return

    print("Let's start the quiz!")
    correct_count = 0
    total_count = len(flashcards)

    for question, answer in flashcards.items():
        user_answer = input(f"Q: {question} | Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            correct_count += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"Quiz completed. You got {correct_count} out of {total_count} correct.")

def main():
    print("Welcome to the Flashcard Quiz Game!")
    while True:
        print("\nMenu:")
        print("1. Add Flashcard")
        print("2. View Flashcards")
        print("3. Quiz Yourself")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_flashcard()
        elif choice == "2":
            view_flashcards()
        elif choice == "3":
            quiz()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


