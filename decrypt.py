from cryptography.fernet import Fernet
import argparse


def decrypt_file(file, key):
    try:
        dec_key = Fernet(key)
        if dec_key:
            print("Decrypting the file using the previously generated key.")
            with open(file, "rb") as files:
                encrypted_data = files.read()
            decrypted_data = dec_key.decrypt(encrypted_data)
            if decrypted_data:
                print("Decrypted the file")
                with open('decrypt.xml', "wb") as file:
                    file.write(decrypted_data)

    except FileNotFoundError:
        print("{} file is not found").format(file)
        exit(1)
    except IOError:
        print("File Write Error")
        exit(1)


def main():
    parse = argparse.ArgumentParser(description="Provided the encrypted xml file and get "
                                                "decrypted xml file")
    parse.add_argument("file", help="Mandatory to provide File to encrypt/decrypt")
    parse.add_argument("--decrypt", dest="decrypt", action="store_true",
                       help="decrypt the file")

    args = parse.parse_args()

    input_file = args.file
    decrypt = args.decrypt

    if decrypt:
        read_key = open("aes_key.key", "rb").read()
        decrypt_file(input_file, read_key)


if __name__ == '__main__':
    main()

