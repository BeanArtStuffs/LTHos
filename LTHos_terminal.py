import time
import os
import subprocess

# ANSI escape code for dark green text
DARK_GREEN = '\033[32m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.2):
    for line in text.splitlines():
        print(DARK_GREEN + line + RESET)
        time.sleep(delay)

# Clear the screen first
clear_screen()

# ASCII Art for "3 stars and a swirl"
title_screen = """
  
 /$$    /$$$$$$$$ /$$   /$$                                          
| $$   |__  $$__/| $$  | $$                                          
| $$      | $$   | $$  | $$  /$$$$$$   /$$$$$$$                      
| $$      | $$   | $$$$$$$$ /$$__  $$ /$$_____/                      
| $$      | $$   | $$__  $$| $$  \ $$|  $$$$$$                       
| $$      | $$   | $$  | $$| $$  | $$ \____  $$                      
| $$$$$$$$| $$   | $$  | $$|  $$$$$$/ /$$$$$$$/                      
|________/|__/   |__/  |__/ \______/ |_______/                       
                                                                     
                                                                     
                                                                     
 /$$$$$$$$                                /$$                     /$$
|__  $$__/                               |__/                    | $$
   | $$  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$ | $$
   | $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$| $$__  $$ |____  $$| $$
   | $$| $$$$$$$$| $$  \__/| $$ \ $$ \ $$| $$| $$  \ $$  /$$$$$$$| $$
   | $$| $$_____/| $$      | $$ | $$ | $$| $$| $$  | $$ /$$__  $$| $$
   | $$|  $$$$$$$| $$      | $$ | $$ | $$| $$| $$  | $$|  $$$$$$$| $$
   |__/ \_______/|__/      |__/ |__/ |__/|__/|__/  |__/ \_______/|__/
                                                                     
                                                                     
                                                                     

"""

footer = """
     Loading... please wait
"""

# Display the ASCII title slowly
print_with_delay(title_screen, 0.5)
print_with_delay(footer, 0.3)

# Display menu options with delay
print(DARK_GREEN + "\n\nOptions:\n" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "1. Run a Python Script" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "2. Run Game Menu" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "3. Watch a Movie?" + RESET)
time.sleep(0.5)
print(DARK_GREEN + "4. Exit\n" + RESET)

# Prompt the user for a choice
choice = input(DARK_GREEN + "Enter your choice (1, 2, 3, or 4): " + RESET)

if choice == '1':
    # Prompt for Python script name
    script_name = input(DARK_GREEN + "Enter the Python script name to run (e.g., script.py): " + RESET)
    
    # Run the specified Python script in PowerShell
    try:
        subprocess.run(["powershell", "-NoExit", "python", script_name], check=True)
    except Exception as e:
        print(DARK_GREEN + f"Error running the script: {e}" + RESET)

elif choice == '2':
    # Run the game_menu.py script
    try:
        subprocess.run(["powershell", "-NoExit", "python", "game_menu.py"], check=True)
    except Exception as e:
        print(DARK_GREEN + f"Error running the game menu: {e}" + RESET)

elif choice == '3':
    # Watch a movie via ASCII theater
    try:
        subprocess.run(["powershell", "-NoExit", "ssh -o StrictHostKeyChecking=no watch.ascii.theater"], shell=True)
    except Exception as e:
        print(DARK_GREEN + f"Error connecting to ASCII theater: {e}" + RESET)

elif choice == '4':
    # Goodbye message before exiting
    print(DARK_GREEN +""""
  
 
 /$$$$$$$                      /$$      
| $$__  $$                    | $$      
| $$  \ $$ /$$   /$$  /$$$$$$ | $$      
| $$$$$$$ | $$  | $$ /$$__  $$| $$      
| $$__  $$| $$  | $$| $$$$$$$$|__/      
| $$  \ $$| $$  | $$| $$_____/          
| $$$$$$$/|  $$$$$$$|  $$$$$$$ /$$      
|_______/  \____  $$ \_______/|__/      
           /$$  | $$                    
          |  $$$$$$/                    
           \______/                     

                                                                     
                                                                     
                                                                     

""" + RESET)
    time.sleep(10)
    os.system('exit')  # Close the terminal

else:
    print(DARK_GREEN + "Invalid choice. Exiting..." + RESET)
    os.system('exit')  # Close the terminal
