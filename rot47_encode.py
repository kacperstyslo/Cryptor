import os
import cryptor
import password_manager


class ROT47:

    def __init__(self):
        self.encode_password_rot_47: str = ''
        self.characters_given_from_User: str = ''

    def rot47_menu(self):
        cryptor.Clear.clear()
        print(31 * '=', " ROT-47 ", 31 * '=')
        self.characters_given_from_User = str(input("Enter the password to encode: "))
        self.encode_rot47(characters_from_user=self.characters_given_from_User, is_encrypted=None)

    def encode_rot47(self, characters_from_user, is_encrypted=None, tests=False):
        x = []
        for i in range(len(characters_from_user)):
            j = ord(characters_from_user[i])
            if 33 <= j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(characters_from_user[i])
        self.encode_password_rot_47 = ''.join(x)

        if tests or is_encrypted:
            return self.encode_password_rot_47
        else:
            print(f"Given password: {characters_from_user} ====> {self.encode_password_rot_47}")
            os.system('pause') if os.name == 'nt' else input('Press enter to continue ...')
            password_manager.PasswordSave().save_encrypted_password(cipher_type='ROT-47',
                                                                    password_from_user=self.encode_password_rot_47)

