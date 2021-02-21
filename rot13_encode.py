import os
import cryptor
import password_manager


class ROT13:

    def __init__(self):
        self.password_from_user: str = ''

    def encode_rot13(self, test=False, test_word=''):
        cryptor.Clear.clear()
        print(31 * '=', " ROT-13 ", 31 * '=')
        characters_given_from_user = test_word
        if not test:
            characters_given_from_user = str(input("Enter the password to encode: "))
        self.password_from_user = str.translate(characters_given_from_user,
                                                str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                                                              "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))
        if test:
            return self.password_from_user
        print(f"Given password: {characters_given_from_user} ====> {self.password_from_user}\n")
        os.system('pause') if os.name == 'nt' else input('Press enter to continue ...')
        password_manager.PasswordSave().save_encrypted_password(cipher_type='ROT-13', password_from_user=self.password_from_user)
