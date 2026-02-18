import pyperclip
import argparse
import time

def greet(is_quick: bool, mode: str) -> None:
    if not is_quick:
        print("Hello, I am Caesar! A variable name maker.")
        print(f"You have chosen {mode} case mode.")
        print("Type your variable, seperated with spaces. I will format it and copy it to your clipboard. Hoping you have a clipboard manager :)")
        print("Press Ctrl+C to exit at any time.\n")
    else:
        return

def farewell(quick: bool) -> None:
    if not quick:
        dialogue = ["Veni.", "Vidi.", "Vici."]
        for word in dialogue:
            print("\n")
            print(word)
            time.sleep(0.5)
    else:
        return

def snake_case(is_quick: bool) -> None:
    greet(is_quick, "Snake")
    while True:
        try:    
            text = input("Enter the variable: ")
            formatted_text = text.strip().replace(" ", "_")

            pyperclip.copy(formatted_text)
            print("Copied!")
        except KeyboardInterrupt:
            farewell(is_quick)
            break

def camel_case(is_quick: bool) -> None:
    greet(is_quick, "Camel")
    while True:
        try:
            text = input("Enter the variable: ")

            if len(text) == 0:
                print("Empty input. Please try again.")
                continue

            if text[0].isupper():
                text = text[0].lower() + text[1:]
            
            new = text.split()
            formatted_text = new[0] + "".join(word.capitalize() for word in new[1:])

            pyperclip.copy(formatted_text)
            print("Copied!")
        except KeyboardInterrupt:
            farewell(is_quick)
            break

def pascal_case(is_quick: bool) -> None:
    greet(is_quick, "Pascal")
    while True:
        try:
            text = input("Enter the variable: ")
                    
            new = text.split()
            formatted_text = "".join(word.capitalize() for word in new)

            pyperclip.copy(formatted_text)
            print("Copied!")
        except KeyboardInterrupt:
            farewell(is_quick)
            break

def main() -> None:

    parseManager = argparse.ArgumentParser(prog="caesar", description="variable name maker")

    parseManager.add_argument("--version", action="version", version="%(prog)s 0.1.0", help = "Show the version number and exit")
    parseManager.add_argument("--snake", "-s", action="store_true", help = "Start a session which returns Snake case")
    parseManager.add_argument("--camel", "-c", action="store_true", help = "Start a session which returns Camel case")
    parseManager.add_argument("--pascal", "-p", action="store_true", help = "Start a session which returns Pascal case")
    parseManager.add_argument("--quick", "-q", action="store_true", help = "Start without the greeting and farewell dialogue")

    args = parseManager.parse_args()

    modes = [args.snake, args.camel, args.pascal]
    if sum(modes) != 1:
        parseManager.error("Choose exactly one mode: -s, -c, or -p")

    if args.snake:
        snake_case(args.quick)
    if args.camel:
        camel_case(args.quick)
    if args.pascal:
        pascal_case(args.quick)
    

if __name__ == "__main__":
    main()