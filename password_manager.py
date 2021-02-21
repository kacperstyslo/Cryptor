import time
import os
import cryptor
import rot47_encode


class PasswordSave:

    @staticmethod
    def save_encrypted_password(cipher_type, password_from_user):
        with open("encrypted_password.txt", 'w') as fw:
            fw.write(f"{cipher_type} ==> {password_from_user}")


class PasswordDecryptor:

    @staticmethod
    def decrypting_password_from_file():
        try:
            file_with_encrypted_password = open("encrypted_password.txt", 'r')
        except FileNotFoundError:
            print("File with encrypted passwords don't found!")
            time.sleep(2.5)
            cryptor.Clear.clear()

        content_of_file = file_with_encrypted_password.read()
        content_of_file_list = content_of_file.split(' ')
        file_with_encrypted_password.close()

        if content_of_file_list[0] == 'ROT-13':
            print(f"Encrypted password: {content_of_file_list[-1]} ====> ",
                  str.translate(content_of_file_list[-1],
                                str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                                              "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")))

        elif content_of_file_list[0] == 'ROT-47':
            print(f"Encrypted password: {content_of_file_list[-1]} ====> ",
                  rot47_encode.ROT47().encode_rot47(characters_from_user=content_of_file_list[-1], is_encrypted=1))

        os.system('pause') if os.name == 'nt' else input('Press enter to continue ...')
        cryptor.Clear.clear()


class PasswordDestroy:

    @staticmethod
    def delete_file_with_password():
        if os.path.isfile('encrypted_password.txt'):
            os.remove('encrypted_password.txt')
            print("File with password was deleted!")
        else:
            print("File does not exist!\n")
        os.system('pause') if os.name == 'nt' else input('Press enter to continue ...')
