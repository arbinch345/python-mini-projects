# deck_game.py
# FUNCTION-BASED Deck Guessing Game
# Run: python deck_game.py

import random
import json
import os

# =========================
# CONSTANTS
# =========================

SUITS = ["♠", "♥", "♦", "♣"]

RANKS = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13
}

SAVE_FILE = "highscore.json"


# =========================
# CREATE DECK
# =========================

def create_deck():

    deck = []

    for suit in SUITS:
        for rank in RANKS:

            card = {
                "rank": rank,
                "suit": suit,
                "value": RANKS[rank]
            }

            deck.append(card)

    return deck


# =========================
# SHUFFLE DECK
# =========================

def shuffle_deck(deck):
    random.shuffle(deck)


# =========================
# DRAW CARD
# =========================

def draw_card(deck):

    if len(deck) == 0:
        return None

    return deck.pop()


# =========================
# DISPLAY CARD
# =========================

def show_card(card):

    return f"{card['rank']}{card['suit']}"


# =========================
# CARD COLOR
# =========================

def get_color(card):

    if card["suit"] in ["♥", "♦"]:
        return "red"

    return "black"


# =========================
# COMPARE CARDS
# =========================

def compare_cards(current_card, next_card):

    if next_card["value"] > current_card["value"]:
        return "higher"

    elif next_card["value"] < current_card["value"]:
        return "lower"

    else:
        return "equal"


# =========================
# LOAD HIGH SCORE
# =========================

def load_high_score():

    if not os.path.exists(SAVE_FILE):
        return 0

    with open(SAVE_FILE, "r") as file:

        data = json.load(file)

        return data.get("high_score", 0)


# =========================
# SAVE HIGH SCORE
# =========================

def save_high_score(score):

    with open(SAVE_FILE, "w") as file:

        json.dump({"high_score": score}, file)


# =========================
# SHOW GAME STATUS
# =========================

def show_status(score, lives, streak, deck, high_score):

    print("\n" + "=" * 40)

    print(f"Score      : {score}")
    print(f"Lives      : {'♥' * lives}")
    print(f"Streak     : {streak}")
    print(f"Cards Left : {len(deck)}")
    print(f"High Score : {high_score}")

    print("=" * 40)


# =========================
# CALCULATE POINTS
# =========================

def calculate_points(streak):

    base_points = 10

    if streak >= 5:
        return base_points * 3

    elif streak >= 3:
        return base_points * 2

    return base_points


# =========================
# MAIN GAME FUNCTION
# =========================

def start_game():

    # Create and shuffle deck
    deck = create_deck()
    shuffle_deck(deck)

    # Player data
    score = 0
    lives = 3
    streak = 0

    # High score
    high_score = load_high_score()

    print("\n🎴 WELCOME TO THE DECK GAME 🎴")

    # First card
    current_card = draw_card(deck)

    # Main game loop
    while lives > 0 and len(deck) > 0:

        show_status(score, lives, streak, deck, high_score)

        print(f"\nCurrent Card: {show_card(current_card)}")

        print("\nChoose:")
        print("1. Higher")
        print("2. Lower")
        print("3. Red")
        print("4. Black")
        print("5. Quit")

        choice = input("\n> ")

        # Quit game
        if choice == "5":
            break

        # Draw next card
        next_card = draw_card(deck)

        print(f"\nNext Card: {show_card(next_card)}")

        correct = False

        # =====================
        # HIGHER
        # =====================

        if choice == "1":

            result = compare_cards(current_card, next_card)

            if result == "higher":
                correct = True

        # =====================
        # LOWER
        # =====================

        elif choice == "2":

            result = compare_cards(current_card, next_card)

            if result == "lower":
                correct = True

        # =====================
        # RED
        # =====================

        elif choice == "3":

            if get_color(next_card) == "red":
                correct = True

        # =====================
        # BLACK
        # =====================

        elif choice == "4":

            if get_color(next_card) == "black":
                correct = True

        else:
            print("\nInvalid choice.")
            continue

        # =====================
        # UPDATE SCORE
        # =====================

        if correct:

            streak += 1

            points = calculate_points(streak)

            score += points

            print("\n✅ Correct!")
            print(f"+{points} points")

        else:

            lives -= 1
            streak = 0

            print("\n❌ Wrong!")
            print("-1 life")

        # Move to next round
        current_card = next_card

    # =========================
    # GAME OVER
    # =========================

    print("\n" + "=" * 40)
    print("GAME OVER")
    print(f"Final Score: {score}")

    # Save high score
    if score > high_score:

        save_high_score(score)

        print("🎉 NEW HIGH SCORE!")

    else:
        print(f"High Score: {high_score}")

    print("=" * 40)


# =========================
# START PROGRAM
# =========================

start_game()