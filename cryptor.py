# -*- coding: utf-8 -*-
# !/opt/local/bin/python3

import os
import sys
import time
import rot13_encode
import rot47_encode
import password_manager


class Clear:
    """Clearing screen based on lambda function"""

    if os.name == 'nt':
        clear = lambda: os.system('cls')
    else:
        clear = lambda: os.system('clear')


class CryptorExit:
    @staticmethod
    def cryptor_say_goodbye():
        print('Goodbye!')
        sys.exit(0)


class CryptorManager:

    def __init__(self):
        self.start_up_message: str = """WELCOME to Cryptor\nThis script will encrypt any keyboard characters, watch out!"""
        self.main_menu_choice: int = 0
        self.main_menu_options: list = [rot13_encode.ROT13().encode_rot13, rot47_encode.ROT47().rot47_menu,
                                        password_manager.PasswordDecryptor().decrypting_password_from_file,
                                        password_manager.PasswordDestroy().delete_file_with_password, CryptorExit().cryptor_say_goodbye]

    def start_up(self, debug=None):
        if debug:
            print(f"{password_manager.PasswordDecryptor.__mro__}\n{rot13_encode.ROT13.__mro__}\n{rot47_encode.ROT47.__mro__}\n{CryptorManager.__mro__}\n{Clear.__mro__}")
        for char in self.start_up_message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        os.system('pause') if os.name == 'nt' else input('Press enter to continue ...')
        Clear.clear()
        self.cryptor_menu()

    def cryptor_menu(self):
        main_menu_choice_again = 0
        while True:
            Clear.clear()
            if main_menu_choice_again == 3:
                print("User ... you wanted to mess up the program ...\nGoodbye!")
                sys.exit(0)
            print("""
                                    CRYPTORMAX
            |====================================================================|
            | 1.Encrypt the password with the ROT-13 cipher                      |
            | 2.Encrypt the password with the ROT-47 cipher                      |
            | 3.Decode the encrypted password                                    |
            | 4.Delete the password file                                         |
            | 5.Exit                                                             |
            |====================================================================|
                    """)
            user_main_menu_choice = int(input('> ')) - 1
            try:
                self.main_menu_options[user_main_menu_choice]()
            except IndexError:
                print("There is no such option in menu!")
                main_menu_choice_again += 1
                time.sleep(2)


if __name__ == '__main__':
    CryptorManager().start_up(None)
