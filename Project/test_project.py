# test_flashcard

import pytest
from flashcard import add_flashcard, view_flashcards, quiz

def test_add_flashcard():
    # Test adding a flashcard
    flashcards.clear()
    add_flashcard()
    assert len(flashcards) == 1

def test_view_flashcards(capsys):
    # Test viewing flashcards
    flashcards.clear()
    add_flashcard()
    view_flashcards()
    captured = capsys.readouterr()
    assert "Flashcards:" in captured.out

def test_quiz(capsys, monkeypatch):
    # Test quiz functionality
    flashcards.clear()
    flashcards["What is 2 + 2?"] = "4"
    flashcards["Capital of France?"] = "Paris"

    # Simulate user input for the quiz
    user_input = ["4", "London"]
    monkeypatch.setattr("builtins.input", lambda _: user_input.pop(0))

    quiz()
    captured = capsys.readouterr()
    assert "Correct!" in captured.out
    assert "Wrong!" in captured.out

# Add more test cases as needed

if __name__ == "__main__":
    pytest.main(["-v", "test_project.py"])
