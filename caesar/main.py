"""
caesar.main

CLI entry point for the Caesar case-conversion utility.
Handles argument parsing and interactive session dispatch.
"""

import pyperclip
import argparse
import time
from typing import Callable

def run_session(formatter: Callable[[str], str], mode: str, is_quick: bool) -> None:

    # greet the user
    if not is_quick:
        print("Hello, I am Caesar! A variable name maker.")
        print(f"You have chosen {mode} case mode.")
        print("Type your variable, seperated with spaces. I will format it and copy it to your clipboard. Hoping you have a clipboard manager :)")
        print("Press Ctrl+C to exit at any time.\n")
    
    # main loop
    while True:
        try:
            text = input("Enter the variable: ")
            
            # strip leading and trailing whitespace, and check if the input is empty
            text = text.strip()
            if len(text) == 0:
                print("Empty input. Please try again.")
                continue
            formatted_text = formatter(text)
            pyperclip.copy(formatted_text)
            print("Copied!")
        except KeyboardInterrupt:
            break
    
    # farewell dialogue
    if not is_quick:
        dialogue = ["Veni.", "Vidi.", "Vici."]
        print("\n")
        for word in dialogue:
            print(word)
            time.sleep(0.5)

def snake_case(text: str) -> str:
    return "_".join(text.split())

def camel_case(text: str) -> str:
    if text[0].isupper():
        text = text[0].lower() + text[1:]
    
    new = text.split()
    return new[0] + "".join(word.capitalize() for word in new[1:])


def pascal_case(text: str) -> str:
    new = text.split()
    return "".join(word.capitalize() for word in new)

def main() -> None:

    parseManager = argparse.ArgumentParser(prog="caesar", description="variable name maker")

    parseManager.add_argument("--version", action="version", version="%(prog)s 0.1.1", help = "Show the version number and exit")
    parseManager.add_argument("--snake", "-s", action="store_true", help = "Start a session which returns Snake case")
    parseManager.add_argument("--camel", "-c", action="store_true", help = "Start a session which returns Camel case")
    parseManager.add_argument("--pascal", "-p", action="store_true", help = "Start a session which returns Pascal case")
    parseManager.add_argument("--quick", "-q", action="store_true", help = "Start without the greeting and farewell dialogue")

    args = parseManager.parse_args()

    modes = [args.snake, args.camel, args.pascal]
    if sum(modes) != 1:
        parseManager.error("Choose exactly one mode: -s, -c, or -p")

    if args.snake:
        run_session(snake_case, "Snake", args.quick)
    if args.camel:
        run_session(camel_case, "Camel", args.quick)
    if args.pascal:
        run_session(pascal_case, "Pascal", args.quick)
    

if __name__ == "__main__":
    main()