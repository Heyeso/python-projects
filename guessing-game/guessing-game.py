import random


def validateBounds(u: str, l: str) -> bool:
    """
    "Validate that the upper bound is greater than the lower bound."

    :param upper: The upper bound of the range of numbers to be generated
    :type upper: str
    :param lower: The lower bound of the range of numbers to be generated
    :type lower: str
    :return: A boolean value.
    """
    upper = int(u)
    lower = int(l)
    state = False
    if (upper != 0 and lower != 0) and upper <= lower:
        print("Upper bound can not be lower or equal to lower bound.")
    elif (upper != 0 and lower != 0) and upper - lower <= 10:
        print("Upper bound must be greater than lower bound by more than 10.")
    else:
        state = True

    return state


def processInput(command: str, bounds: list[int], arg: str = ""):
    """
    It takes in a command, a list of bounds, and an optional argument, and returns a list of bounds or a
    list of a single integer containing a status code.

    :param command: The command that the user has entered
    :type command: str
    :param bounds: list[int] - The current bounds of the game
    :type bounds: list[int]
    :param arg: The argument that the user entered
    :type arg: str
    :return: A list of integers.
    """
    newBounds = bounds.copy()

    if command == "e" or command == "exit":
        return [0]
    elif command == "r" or command == "reset":
        print("Bounds have been reset.")
        return [0, 0]
    elif command == "b" or command == "bounds":
        print(f"[Lower: {bounds[0]}, Upper: {bounds[1]}]")
    elif command == "?":
        displayCommands()
    elif arg.isnumeric() and len(arg) < 5 and arg != "":
        if (command == "upper" or command == "u") and validateBounds(arg, bounds[0]):
            newBounds[1] = int(arg)
        elif (command == "lower" or command == "l") and validateBounds(bounds[1], arg):
            newBounds[0] = int(arg)
        elif command == "guess" or command == "g":
            return [int(arg)]
        else:
            print("Please enter a positive integer number (between 1 and 9999).")
            return [-1]
        return newBounds
    else:
        print("Press ? to show a list of all available commands.")

    return [-1]


def isGuessed(guess: int, ans: int) -> bool:
    """
    `isGuessed` takes in a guess and an answer and returns True if the guess is correct, and False
    otherwise

    :param guess: the user's guess
    :type guess: int
    :param ans: the answer to the question
    :type ans: int
    :return: A boolean value.
    """
    if guess == ans:
        print("You Guessed it!")
        return True
    elif guess > ans:
        print("Too high.")
    elif guess < ans:
        print("Too low.")

    return False


def displayCommands():
    UNDERLINE = {
        "start": "\033[4m",
        "end": "\033[0m",
    }

    print(
        f"""
{UNDERLINE["start"]}? HeyGuess Commands:{UNDERLINE["end"]}

• Press u or enter upper followed by number to set upper bound (eg. > u 12).
• Press l or enter lower followed by number to set lower bound (eg. > l 12).
• Press g or enter guess followed by number to input guess (eg. > g 12).
• Press r or enter reset to reset bounds.
• Enter && between commands to enter multiple commands at once.
• Press b or enter bounds to show bounds.
• Press e or enter exit to exit the program.
    """
    )


def runGame():
    """
    It takes user input, processes it, and then returns a value based on the result of the processing
    :return: The return value is a list of integers.
    """
    guess = 0
    bounds: list[int] = [0, 0]
    userInputList: list[str] = []
    running = True

    print("Welcome to Heyeso's Guessing Game - ? HeyGuess.")
    displayCommands()

    while running:
        # Checking if the user has entered multiple commands at once, and if so, it splits the commands
        # into a list of strings, and then processes them one by one.
        userInput = input("> ") if not len(userInputList) else userInputList.pop(0)
        if "&&" in userInput:
            userInputList = userInput.split("&&")
            userInput = userInputList.pop(0)

        # Splitting the user input into a list of strings, and then passing the first element of the list to
        # the processInput function as the command, and the second element of the list as the argument.
        cmdList = userInput.strip().split(" ")
        if len(cmdList) > 1:
            inputResult = processInput(cmdList[0], bounds, cmdList[1])
        else:
            inputResult = processInput(cmdList[0], bounds)

        if len(inputResult) > 1:
            bounds = inputResult
            if bounds[0] == 0 or bounds[1] == 0:
                print("Bounds not set.", bounds)
            else:
                guess = random.randint(bounds[0], bounds[1])
            continue
        elif inputResult[0] == 0:
            return 0
        elif inputResult[0] < 0:
            continue
        elif isGuessed(inputResult[0], guess):
            bounds = processInput("r", bounds)


runGame()
