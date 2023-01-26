import random


def displayCommands():
    UNDERLINE = {
        "start": "\033[4m",
        "end": "\033[0m",
    }

    print(
        f"""
{UNDERLINE["start"]}? HeyRock-Paper-Scissors Commands:{UNDERLINE["end"]}
• Press r or Type rock and press enter to play Rock.
• Press p or Type paper and press enter to play Paper.
• Press s or Type scissors and press enter to play Scissors.
• Type score and press enter to show scores.
• Type reset and press enter to reset scores.
• Press e or Type exit and press enter to exit the program.
    """
    )


def displayGameIntro():
    print(
        f"""
Welcome to Heyeso's Rock-Paper-Scissors Game - HeyRock-Paper-Scissors.

The goal is simple: win against computer. Enter you choice and see who
is the better player.

Begin!!!
    """
    )


def compareHands(player: str, compIndex: int, score: dict) -> dict:
    newScore = score.copy()
    playerIndex = ["r", "p", "s"].index(player)

    if (playerIndex < compIndex and (abs(playerIndex - compIndex) <= 1)) or (playerIndex > compIndex and (abs(playerIndex - compIndex) > 1)):
        newScore["computer"] += 1
    elif (playerIndex > compIndex and (abs(playerIndex - compIndex) <= 1)) or (playerIndex < compIndex and (abs(playerIndex - compIndex) > 1)):
        newScore["player"] += 1

    return newScore


def runGame():
    running = True
    score = {"player": 0, "computer": 0}
    HANDS = ["rock", "paper", "scissors"]

    displayGameIntro()
    displayCommands()

    while running:
        userInput = input("> ")
        command = userInput.strip().split(" ")[0].lower()

        comp = random.randint(0, 2)

        if command == "?":
            displayCommands()
        elif command == "e" or command == "exit":
            running = False
        elif command == "reset":
            score = {"player": 0, "computer": 0}
        elif command == "score":
            print(f"Player: {score['player']}\nComputer: {score['computer']}")
        elif command in HANDS or command in ["r", "p", "s"]:
            print(f"Computer played {HANDS[comp].capitalize()}.")
            score = compareHands(command, comp, score)
        else:
            print("Press ? to show a list of all available commands.")


runGame()
