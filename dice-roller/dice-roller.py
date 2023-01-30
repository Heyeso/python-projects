import random

MAX_DIE_NUM = 6
MIN_DIE_NUM = 1
DIE_FACE = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ],
}

def rollDice(num: int):
    return [random.randint(MIN_DIE_NUM, MAX_DIE_NUM) for i in range(num)]

def generateDiceFaces(faces: list[int]):
    for height in range(len(DIE_FACE[1])):
        line = ""
        for face in faces:
            line += " " + DIE_FACE[face][height]
        print(line)

def runGame():
    running = True

    while running:
        userInput = input(
            "How many dice would you like to roll? [1-6] "
        )
        
        if userInput == "e" or userInput == "exit":
            running = False
        if not userInput.isnumeric() or int(userInput) < 1 or int(userInput) > 6:
            continue
        else:
            generateDiceFaces(rollDice(int(userInput)))

        running = False

runGame()
