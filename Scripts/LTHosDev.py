import time
import os
import subprocess
import getpass  # To get the current username
import random  # For random password selection

# ANSI escape code for dark green text
DARK_GREEN = '\033[32m'
RESET = '\033[0m'

# Developer usernames list
developer_usernames = ["roger", "s10095479" , "georg"]

# Hardcoded list of passwords
passwords = [
    "1215", "2342", "1232", "0329" , "23q2321" , "THsVSK", "q23AJ", "12-aw", "4a-", "k7t", "m-g8j", "rw@1fp", "cz-m8iu", "3pnb-xkv", "tf7gu-ha2s", "q1we-mnzop", "b1d7hc-fjotx", "ls2zokd-nwmp", "qfhrt1-xmnsvy", "k3jfsdc-nvz5uot" "8g-xp", "z9j0-", "2lm-k5", "pq-3v8", "0x-4ye", "7bt@12", "nq!5v-r", "jd0-bxp", "rw6f9l-", "k3z-ov1", "4c-mj9", "t8sy-kq", "x7l-2g", "f1j!0n-", "h9-3tr", "7ks@lb", "wp-8vx", "m5t2-dy", "b8-zw1q", "6r-jfo", "3ct-wy0", "nz9-8hr", "5pq!g-k", "m7u-lt3", "c4yx@0z", "9tv!6p-", "d2-jqx", "y6s-1r0", "vl7-8bq", "p9j!t3-", "b4k-wx0", "a7yf#1", "h2m-9c", "tq6-df3", "0nl-w8x", "s1k!yt9", "5b-nvp@", "mz!q4p", "jr-2sl", "kz1-d5y", "lg0x@r", "3b-lmn", "c9q8-z", "7p!t2d-", "f0k-rj6", "nl4-1ox", "vy7-d2q", "tx3v-m9", "s!8g-qz", "b0f-6pr", "c1j!v9-", "x7l@2nm", "9c-qvp!", "w2g-1tz", "8dy-jmr", "z4l@6xc", "pt5-9vf", "ql!7o-b", "m3s-0gn", "hz2-yvx", "g8f@q2", "t5kp!1-", "w3z-4xo", "y1n!ql-", "x8c@0bf", "v7r-2jp", "dm9-q!5", "p1k!t4n", "b6z-8wj", "o9y-vx2", "c5l-zn!", "j1f@3k-", "x6g-qv9", "2m!tp-y", "rz7l-5c", "4wf!m9-", "sv3-kq1", "p!6c-5b", "d7l-m2o", "a8@yr-3", "o5jv!8-", "k2n-q!6", "t3j-w4y", "z1lp@6-", "9o-gv7q", "x2d-tj8", "m5y!0c-", "t1s-k4n", "p@3xl-7", "2bf-j8o", "v5xg-q6", "c@7z1-b", "p8t-9m!", "wj0-lf2", "m9@t4q-", "yz5k-8v", "l2b@1x-", "c9jv-pq0", "s4w-m8n", "t3y-f6@", "pz!9-jk"


]

# Customizable override key
override_key = "OVERIDE_#ROGER"  # Change this to your desired override key
override_key2 = "OVERIDE_#DOWDY"
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.2):
    for line in text.splitlines():
        print(DARK_GREEN + line + RESET)
        time.sleep(delay)

def select_random_password():
    # Return a random password from the list
    return random.choice(passwords)

def verify_password(selected_password):
    # Prompt the user for the password
    entered_password = input(DARK_GREEN + "Enter Developer Password (or type override key): " + RESET)
    return entered_password == selected_password or entered_password == override_key , override_key2

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
                                                                     
                                                                     
                                                                     
 /$$$$$$$                                                            
| $$__  $$                                                           
| $$  \ $$  /$$$$$$  /$$    /$$                                      
| $$  | $$ /$$__  $$|  $$  /$$/                                      
| $$  | $$| $$$$$$$$ \  $$/$$/                                       
| $$  | $$| $$_____/  \  $$$/                                        
| $$$$$$$/|  $$$$$$$   \  $/                                         
|_______/  \_______/    \_/                                          
                                                                     
                                                                     
                                                                     
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
     Welcome back, developer!
"""

# Display the ASCII title slowly
print_with_delay(title_screen, 0.2)
print_with_delay(footer, 0.3)

# Get the current username
current_user = getpass.getuser()

# Check if current user is in the list of developers
if current_user in developer_usernames:
    # Select a random password from the list
    selected_password = select_random_password()
    print(DARK_GREEN + f"Developer access granted! (Random password selected: {selected_password})" + RESET)
    
    if verify_password(selected_password):
        print(DARK_GREEN + "Access confirmed!" + RESET)
    else:
        print(DARK_GREEN + "ERR - Incorrect password." + RESET)
        time.sleep(3)
        exit()
else:
    print(DARK_GREEN + "ERR - User is not developer." + RESET)
    time.sleep(3)
    exit()

# Developer terminal main menu options
print_with_delay("\n\nOptions:\n")
print(DARK_GREEN + "1. Customize with dev control here!" + RESET)
print(DARK_GREEN + "2. Exit\n" + RESET)

user_input = input(DARK_GREEN + "Enter your choice (1 or 2): " + RESET)

if user_input == '1':
    print(DARK_GREEN + "Customizing with developer controls... (Placeholder for your custom functionality)" + RESET)
    # Place any customization code here

elif user_input == '2':
    print(DARK_GREEN + "See you soon!" + RESET)
    time.sleep(10)
    os.system('exit')

else:
    print(DARK_GREEN + "Invalid choice. Exiting..." + RESET)
    os.system('exit')
