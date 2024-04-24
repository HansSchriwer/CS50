Flashcard Quiz Game Final Project for CS50
Name: Hans Schriwer
Github and EDX username: github.com/HansSchriwer  & hansenMia
Miami – USA
https://youtu.be/uT819cPkvXU
April 25, 2024

Overview
The Flashcard Quiz project is a simple Python application that allows users to create, manage, and study digital flashcards. Whether you’re preparing for exams, learning new vocabulary, or reinforcing concepts, this project provides an interactive way to enhance your learning experience.

Features
Create Flashcards: Easily create new flashcards by adding questions and answers.
Organize Decks: Group your flashcards into decks based on topics or subjects.
Study Mode: Test your knowledge by flipping through the flashcards in study mode.
Randomization: Shuffle the order of flashcards to prevent memorization patterns.
Progress Tracking: Keep track of your progress by marking cards as mastered or needing review.
File Structure
main.py: Contains the core logic for managing flashcards and decks.
flashcard.py: Defines the Flashcard class with attributes like question, answer, and deck association.
deck.py: Implements the Deck class to organize flashcards into groups.
utils.py: Includes utility functions for reading/writing flashcards to files and handling user input.
Installation
Clone this repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run the application with python main.py.
Usage
Create a new deck using main.py.
Add flashcards to the deck with relevant questions and answers.
Start studying by running the application and selecting your desired deck.
Use the keyboard shortcuts to navigate through the flashcards (e.g., press ‘N’ for the next card).
Design Choices
Data Storage: Flashcards and decks are stored in plain text files (e.g., JSON or CSV) for simplicity and portability.
User Interface: The command-line interface was chosen to keep the project lightweight and accessible.
Future Enhancements
User Authentication: Add user accounts to save progress across sessions.
Rich Text Support: Allow formatting (e.g., bold, italics) in flashcard content.
Web Interface: Develop a web-based version for broader accessibility.
Contributing
Contributions are welcome! If you have ideas for improvements or bug fixes, feel free to submit a pull request.

