import pyperclip
import argparse


def snake_case() -> None:
    while True:
        try:    
            text = input("Enter the variable: ")
            formatted_text = text.strip().replace(" ", "_")

            pyperclip.copy(formatted_text)
            print("Copied!")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

def camel_case() -> None:
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
            print("\nExiting...")
            break

def pascal_case() -> None:
    while True:
        try:
            text = input("Enter the variable: ")
                    
            new = text.split()
            formatted_text = "".join(word.capitalize() for word in new)

            pyperclip.copy(formatted_text)
            print("Copied!")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

def main() -> None:

    parseManager = argparse.ArgumentParser(prog="caesar", description="variable name maker")

    parseManager.add_argument("--version", action="version", version="%(prog)s 0.1.0", help = "Show the version number and exit")
    parseManager.add_argument("--help", "-h", action="help", help = "Show this help message and exit")
    parseManager.add_argument("--snake", "-s", action="store_true", help = "Start a session which returns Snake case")
    parseManager.add_argument("--camel", "-c", action="store_true", help = "Start a session which returns Camel case")
    parseManager.add_argument("--pascal", "-p", action="store_true", help = "Start a session which returns Pascal case")

    args = parseManager.parse_args()

    modes = [args.snake, args.camel, args.pascal]
    if sum(modes) != 1:
        parseManager.error("Choose exactly one mode: -s, -c, or -p")

    if args.snake:
        snake_case()
    if args.camel:
        camel_case()
    if args.pascal:
        pascal_case()
    

if __name__ == "__main__":
    main()