import os
import time
import random

# Get the current working directory

def main():
    current_dir = os.getcwd()
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

    print("Welcome to this custom Terminal! This was made for Palestine Code Championship 2024!")
    running = True
    while running:
        user_input = input(">> ")

        if "help" in user_input:
            if "-err" in user_input:
                print("PermissionError1: Happens when the user attempts to delete a file/directory, this most likely means that said file is in use by another program.")
                print("MissingDirName1: Happens when the user attempts to make a directory without inputing a name.")
                print("MissingFileName1: Happens when the user attempts to make a file without specifying a name.")
            else:
                print("'^' Means its for comedic purposes only.")
                print("exit: Self explanatory (i.e. exits the program)")
                print("echo <words>: Echoes the user's words.")
                print("mkfile <filename>: makes a new file with the given name.")
                print("ls: lists the files in the current directory.")
                print("cd <directory>: changes the current directory to the specified one.")
                print("^fortune: displays a random fortune.")
                print("copy <filename>: copies the specified file to a new location.")
                print("rmdir <directory>: removes the specified directory.")
                print("mkdir <name>: Makes a directory.")
        
        elif user_input.startswith("echo "):
            print(user_input[5:])

        elif user_input == "exit":
            print("Exiting the terminal...")
            running = False

        elif user_input == "ls":
            for item in os.listdir(current_dir):
                print(item)

        elif user_input.startswith("mkfile "):
            filename = user_input[7:]
            if filename:
                with open(os.path.join(current_dir, filename), 'w') as f:
                    f.write("")
                print(f"File {filename} created.")
            else:
                print("Please specify a filename. ERR: MissingFileName1")

        elif user_input.startswith("rmdir "):
            directory = user_input[6:]
            directory_path = os.path.join(current_dir, directory)
            print(f"Attempting to remove directory: {directory_path}")
            if os.path.exists(directory_path):
                try:
                    os.removedirs(directory_path)
                    print(f"{directory} removed successfully.")
                except PermissionError:
                    print("File cannot be deleted. ERR: PermissionError1")
                    print("\n \n For more info about this error, run 'help -err'")
            else:
                print(f"{directory} doesn't exist.")

        elif user_input.startswith("cd "):
            new_dir = user_input[3:]
            new_dir_path = os.path.join(current_dir, new_dir)
            print(f"Attempting to change directory to: {new_dir_path}")
            if os.path.exists(new_dir_path):
                current_dir = new_dir_path
                print(f"Directory changed to {current_dir}")
            else:
                print(f"Directory {new_dir} does not exist.")

        elif user_input == "fortune":
            fortune_to_choose = random.randint(0, len(fortunes) - 1)
            print(fortunes[fortune_to_choose])

        elif user_input.startswith("copy "):
            victim_file = user_input[5:]
            victim_file_path = os.path.join(current_dir, victim_file)
            if os.path.exists(victim_file_path):
                destination = input("Destination: ")
                destination_path = os.path.join(current_dir, destination)
                if os.path.isdir(destination_path):
                    final_destination = os.path.join(destination_path, os.path.basename(victim_file_path))
                    with open(victim_file_path, 'r') as f:
                        print("Reading content...")
                        content = f.read()
                    print(f"Making {victim_file} copy at {final_destination}...")
                    with open(final_destination, 'w') as f2:
                        print("Writing content...")
                        f2.write(content)
                    print("File copied successfully.")
                else:
                    print("Destination is not a valid directory.")
            else:
                print("File doesn't exist.")
        elif user_input.startswith("mkdir "):
            name = user_input[6:].strip()  # Get the directory name and remove leading/trailing whitespace
            if not name:  # Check if the name is empty
                print("Please add a name to the directory. ERR: MissingDirName")
            else:
                new_dir_name = os.path.join(current_dir, name)
                try:
                    os.makedirs(new_dir_name)  # Create the directory
                    print(f"Created {new_dir_name} without any errors.")
                except Exception as e:
                    print(f"An error occurred while creating the directory: {e}")


        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
