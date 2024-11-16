import time
import os
import subprocess
import getpass
import requests

DARK_GREEN = '\033[32m'
RESET = '\033[0m'

developer_usernames = ["roger", "s10095479", "georg"]
preinstalled_scripts = ["game_menu.py", "LTHosDev.py", "Titles.md", "snake.py", "slots.py", "Pong.py", "LTHosTerminal.py", "Dot Game.py", "Blackjack.py"]  # Add any other pre-installed scripts here
excluded_github_files = ["README.md"]  # Add any other files to exclude from GitHub here

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.2):
    for line in text.splitlines():
        print(DARK_GREEN + line + RESET)
        time.sleep(delay)

# Function to fetch scripts from the GitHub repository
def fetch_scripts(url):
    """Fetch scripts from GitHub Repository."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns a list of files and directories
    else:
        print(DARK_GREEN + "Error fetching scripts from GitHub." + RESET)
        return []

# Function to recursively gather all scripts
def gather_all_files(base_url, items, all_files):
    for item in items:
        if item['type'] == 'file' and item['name'] not in excluded_github_files:
            all_files.append({'name': item['name'], 'download_url': item['download_url']})
        elif item['type'] == 'dir':
            # If it's a directory, call the function again to get its contents
            new_url = f"{base_url}{item['path']}/"
            gathered_files = fetch_scripts(new_url)
            if gathered_files:  # Only gather files if response is successful
                gather_all_files(base_url, gathered_files, all_files)

# Function to download and save a selected script from the GitHub repository
def download_script(script_url, save_path):
    """Download and save a selected script from the GitHub repository."""
    response = requests.get(script_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(DARK_GREEN + f"Script downloaded and saved to '{save_path}'." + RESET)
    else:
        print(DARK_GREEN + "Error downloading the script." + RESET)

def list_files_in_directory():
    """List all files in the current directory, excluding pre-installed scripts and directories."""
    files = [file for file in os.listdir() if file not in preinstalled_scripts and os.path.isfile(file)]
    for index, file in enumerate(files, start=1):
        filename_without_extension = os.path.splitext(file)[0]  # Remove the file extension
        print(DARK_GREEN + f"{index + len(options)}. {filename_without_extension}" + RESET)  # Adjust index to account for pre-installed options
    return files

def display_menu():
    """Display the menu options and list files."""
    clear_screen()
    
    # ASCII Art Title
    title_screen = """
      /$$    /$$$$$$$$ /$$   /$$                      
     | $$   |__  $$__/| $$  | $$                      
     | $$      | $$   | $$  | $$  /$$$$$$   /$$$$$$$ 
     | $$      | $$   | $$$$$$$$ /$$__  $$ /$$_____/ 
     | $$      | $$   | $$__  $$| $$  \ $$|  $$$$$$  
     | $$      | $$   | $$  | $$| $$  | $$ \____  $$ 
     | $$$$$$$$| $$   | $$  | $$|  $$$$$$/ /$$$$$$$/ 
     |________/|__/   |__/  |__/ \______/ |_______/  
    """
    
    footer = """
         Loading... please wait
    """
    
    # Display the ASCII title and loading footer
    print_with_delay(title_screen, 0.1)
    print_with_delay(footer, 0.1)
    
    # Display menu options
    print(DARK_GREEN + "\n\nOptions:\n" + RESET)
    
    global options
    options = ["Run a Python Script", "Run Game Menu", "Watch a Movie?", "Exit", "Import Scripts from GitHub"]
    for i, option in enumerate(options, start=1):
        print(DARK_GREEN + f"{i}. {option}" + RESET)
    
    # List files in the current directory
    files = list_files_in_directory()
    
    # Prompt the user to enter their choice
    dev_mode_enabled = False
    user_input = input(DARK_GREEN + f"Enter your choice (1, 2, 3, 4, 5, or {5 + len(files)}): " + RESET)
    
    # Check for developer mode activation after user input
    if user_input.lower() == "dev":
        dev_mode_enabled = True
        print(DARK_GREEN + "Developer Mode Enabled!" + RESET)
        print(DARK_GREEN + "6. Developer Mode\n" + RESET)
        user_input = input(DARK_GREEN + "Enter your choice (1-6): " + RESET)
    
    return user_input, files, dev_mode_enabled

def main():
    while True:
        user_input, files, dev_mode_enabled = display_menu()
        
        def run_script(script_name):
            try:
                subprocess.run(["python", script_name], check=True)
            except FileNotFoundError:
                print(DARK_GREEN + "Error: The specified script does not exist." + RESET)
            except subprocess.CalledProcessError as e:
                print(DARK_GREEN + f"Error running the script: {e}\nReturn Code: {e.returncode}" + RESET)
            except Exception as e:
                print(DARK_GREEN + f"An unexpected error occurred: {e}" + RESET)
        
        # Process the selected option
        if user_input == '1':
            script_number = input(DARK_GREEN + "Enter the number of the script you want to run: " + RESET)
            if script_number.isdigit() and 1 <= int(script_number) <= len(files) + len(options):
                script_to_run = files[int(script_number) - len(options) - 1]
                run_script(script_to_run)
            else:
                print(DARK_GREEN + "Invalid script number." + RESET)
        
        elif user_input == '2':
            run_script("game_menu.py")
        
        elif user_input == '3':
            try:
                subprocess.run(["powershell", "-NoExit", "ssh", "-o", "StrictHostKeyChecking=no", "watch.ascii.theater"], check=True)
            except Exception as e:
                print(DARK_GREEN + f"Error connecting to ASCII theater: {e}" + RESET)
        
        elif user_input == '4':
            print(DARK_GREEN + "Goodbye! Exiting in 10 seconds..." + RESET)
            time.sleep(10)
            clear_screen()
            break
        
        elif user_input == '5':
            base_url = "https://api.github.com/repos/GeorgeDowdy/LithOsLibary/contents/"
            initial_files = fetch_scripts(base_url)
            all_files = []
            gather_all_files(base_url, initial_files, all_files)
        
            if all_files:
                print(DARK_GREEN + "Available scripts to import:\n" + RESET)
                for index, file in enumerate(all_files):
                    print(DARK_GREEN + f"{index + 1}. {file['name']}" + RESET)
        
                script_choice = int(input(DARK_GREEN + "Enter the number of the script you want to import: " + RESET)) - 1
                
                # Validate the choice
                if 0 <= script_choice < len(all_files):
                    selected_file = all_files[script_choice]
                    download_script(selected_file['download_url'], selected_file['name'])
                else:
                    print(DARK_GREEN + "Invalid selection." + RESET)
            else:
                print(DARK_GREEN + "No scripts available to import." + RESET)
        
        elif dev_mode_enabled and user_input == '6':
            current_user = getpass.getuser()
            if current_user in developer_usernames:
                print(DARK_GREEN + "Developer mode activated. Access granted." + RESET)
                run_script("LTHosDev.py")
            else:
                print(DARK_GREEN + "ERR - User is not a developer." + RESET)
        
        else:
            print(DARK_GREEN + "Invalid choice. Exiting..." + RESET)
            clear_screen()
            break

if __name__ == "__main__":
    main()
