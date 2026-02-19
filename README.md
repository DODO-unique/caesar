# Caesar

## What it is
- Caesar is a variable name maker. 
- It is supposed to get out of your way to let you quickly create variable names in the format you want. 
- Caesar boasts intentionally rigid sessions, simple controls, and easy setup.

## How it works
1. You select a formatting mode. This starts a session
2. Type sentences separated by space
3. Formatted text is copied to your clipboard


## Installation

1. Go to your terminal and run the following command:
```powershell
pip install july-caesar
```

2. Once installed, you can run caesar with the simple command: `caesar [--flag]`


## Usage examples

- For Python variables with long names (following snake-case, as is the convention) you could follow these steps:
   1. Start terminal
   2. command: `caesar -s[q]`
   3. input: `variable name for specific task`
   4. copied output: `variable_name_for_specific_task` (fun fact, caesar formatted this here. I did not sprain my pinky by holding shift it)
   5. simply paste it in your project!

## Tips
1. Use clipboard managers, especially which feature history. Not for caesar only, but it is also very productive in general. Windows has one built in (win+V), there are many free tools (like Maccy) for Mac and Linux users can use CopyQ or Klipper (KDE)
2. Caesar does not consume resources passively, keeping it running in the background is suggested.

## Flags

v0.1.1:
- Three modes available: 
   1. Snake case : `-s`, `--snake`
   2. Camel case : `-c`, `--camel`
   3. Pascal case : `-p`, `--pascal`
- Quick flag:
   - `-q`, `--quick` 
   - No formalities.

## Version Notes

### v0.1.0:
- Primitive.
- Contained MVPs
- Fixed snake-case formatting and universal whitespace handling issues (#1 & #2)
- Featured minimal README.md

### v0.1.1:

- three modes: snake case, pascal case, camel case
- Formalities include: greeting, farewell, can be avoided with -q flag
- exit by Ctrl+C (KeyboardInterrupt)
- features README.md, working code.
   