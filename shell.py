import os
import shutil
import random

def check_if_windows():
    import platform
    if platform.system() != "Windows":
        print("NOTE: This script is mostly compatible with Windows. I do not have plans to bring it to Linux or macOS.")

def display_help():
    print("\033[95mList of available commands:\033[0m")
    print("\033[95m--------------------------\033[0m")
    print("\033[94mhead [-n <number>] <filename>\033[0m    Display first lines of a file")
    print("\033[94mtail [-n <number>] <filename>\033[0m    Display last lines of a file")
    print("\033[94mls <directory>\033[0m                   List contents of a directory")
    print("\033[94mgrep <pattern> <filename>\033[0m       Search for a pattern in a file")
    print("\033[94mcp <source> <destination>\033[0m       Copy a file or directory")
    print("\033[94mmv <source> <destination>\033[0m       Move or rename a file or directory")
    print("\033[94mfind <directory> <pattern>\033[0m     Search for files in a directory")
    print("\033[94mecho <words>\033[0m                      Echoes the user's words")
    print("\033[94mmkfile <filename>\033[0m                 Makes a new file with the given name")
    print("\033[94mrmfile <filename>\033[0m                 Removes the specified file")
    print("\033[94mcd <directory>\033[0m                    Changes the current directory")
    print("\033[94mfortune\033[0m                           Displays a random fortune")
    print("\033[94mcopy <filename>\033[0m                   Copies the specified file to a new location")
    print("\033[94mmkdir <directory>\033[0m                 Creates a new directory")
    print("\033[94mpwd\033[0m                               Prints the current directory")
    print("\033[94mclear\033[0m                             Clears the terminal screen")
    print("\033[94mexit\033[0m                              Exit the terminal")
    print("\033[94mhelp\033[0m                              Display this help message")

def echo(words):
    print(words)

def mkfile(filename):
    current_dir = os.getcwd()
    filepath = os.path.join(current_dir, filename)
    try:
        with open(filepath, 'w') as f:
            pass
        print(f"File '{filename}' created.")
    except Exception as e:
        print(f"Error creating file: {e}")

def rmfile(filename):
    filepath = os.path.join(os.getcwd(), filename)
    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            print(f"File '{filename}' removed successfully.")
        except PermissionError:
            print("File cannot be deleted. ERR: PermissionError1")
    else:
        print(f"File '{filename}' doesn't exist.")

def cd(directory):
    try:
        os.chdir(directory)
        print(f"Directory changed to {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

def fortune():
    fortunes = [
        "Your first newborn son will utter the universe's secrets and give you depression.",
        "Your keyboard will become sentient and demand coffee breaks.",
        "You will be sent back in time to remove gravity by catching the apple that fell on Isaac Newton.",
        "You will be attacked by a flock of ducks soon. Be prepared.",
        "Your gaming controller will break your spine after you broke its joysticks.",
        "Your code will become self-aware and start writing you back.",
        "You will find a bug so elusive it will make Bigfoot seem real.",
        "A rogue 3D printer will start printing philosophical questions.",
        "Your laptop will develop a taste for memes and demand fresh ones daily.",
        "The comments in your code will reveal ancient prophecies.",
        "A mystical force will align your brackets and semicolons perfectly.",
        "Your compiler will develop a sense of humor and start cracking jokes.",
        "The next USB device you plug in will have an existential crisis.",
        "You will be visited by the ghost of unclosed parentheses.",
        "A mysterious algorithm will predict your every typo."
    ]
    print(random.choice(fortunes))

def copy(filename):
    current_dir = os.getcwd()
    source_file = os.path.join(current_dir, filename)
    if os.path.exists(source_file):
        destination = input("Destination: ").strip()
        destination_path = os.path.join(current_dir, destination)
        if os.path.isdir(destination_path):
            final_destination = os.path.join(destination_path, os.path.basename(source_file))
            try:
                with open(source_file, 'r') as f:
                    content = f.read()
                with open(final_destination, 'w') as f2:
                    f2.write(content)
                print("File copied successfully.")
            except Exception as e:
                print(f"Error copying file: {e}")
        else:
            print("Invalid destination directory. ERR: InvalidDir1")
    else:
        print("File doesn't exist.")

def mkdir(directory):
    current_dir = os.getcwd()
    new_dir_path = os.path.join(current_dir, directory)
    try:
        os.makedirs(new_dir_path)
        print(f"Directory '{directory}' created.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def pwd():
    print(os.getcwd())

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def head(filename, lines=None):
    try:
        with open(filename, 'r') as f:
            if lines:
                lines = int(lines)
            else:
                lines = 10  # Default to 10 lines if -n option not provided
            for i, line in enumerate(f):
                if i < lines:
                    print(line.rstrip())
                else:
                    break
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def tail(filename, lines=None):
    try:
        with open(filename, 'r') as f:
            if lines:
                lines = int(lines)
                content = f.readlines()[-lines:]
            else:
                content = f.readlines()[-10:]  # Default to last 10 lines if -n option not provided
            for line in content:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def ls(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

def grep(pattern, filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                if pattern in line:
                    print(line.rstrip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def cp(source, destination):
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
        print(f"Copied '{source}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File or directory '{source}' not found.")
    except FileExistsError:
        print(f"File or directory '{destination}' already exists.")

def mv(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File or directory '{source}' not found.")
    except FileExistsError:
        print(f"File or directory '{destination}' already exists.")

def find(directory, pattern):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if pattern in file:
                    print(os.path.join(root, file))
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")

def main():
    while True:
        user_input = input("\033[94m>> \033[0m").strip()
        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]
        args = parts[1:]

        if command == "head" and args:
            if args[0] == "-n" and len(args) > 1:
                head(args[2], args[1])
            else:
                head(args[0])

        elif command == "tail" and args:
            if args[0] == "-n" and len(args) > 1:
                tail(args[2], args[1])
            else:
                tail(args[0])

        elif command == "ls" and args:
            ls(args[0])

        elif command == "grep" and len(args) == 2:
            grep(args[0], args[1])

        elif command == "cp" and len(args) == 2:
            cp(args[0], args[1])

        elif command == "mv" and len(args) == 2:
            mv(args[0], args[1])

        elif command == "find" and len(args) == 2:
            find(args[0], args[1])

        elif command == "echo" and args:
            echo(" ".join(args))

        elif command == "mkfile" and args:
            mkfile(args[0])

        elif command == "rmfile" and args:
            rmfile(args[0])

        elif command == "cd" and args:
            cd(args[0])

        elif command == "fortune":
            fortune()

        elif command == "copy" and args:
            copy(args[0])

        elif command == "mkdir" and args:
            mkdir(args[0])

        elif command == "pwd":
            pwd()

        elif command == "clear":
            clear()

        elif command == "help":
            display_help()

        elif command == "exit":
            print("\033[91mExiting the terminal...\033[0m")
            break

        else:
            print("\033[91mInvalid command. Type 'help' for a list of commands.\033[0m")

if __name__ == "__main__":
    check_if_windows()
    print("\033[95mWelcome to this custom Terminal! This was made for Palestine Code Championship 2024!\033[0m")
    print("\033[95mYou can use 'help' to get a list of available commands.\033[0m")
    main()
