import os
import json
import argparse
from dicttoxml import dicttoxml
from cryptography.fernet import Fernet


def read_json_file(file):
    try:
        if os.path.exists(file):
            with open(file) as f:
                sample_json_output = json.load(f)
            return sample_json_output
    except FileNotFoundError:
        print("File is not found, please check the at provided location.")
        exit(1)
    except Exception:
        print("Unexpected error")
        exit(1)


def convert_json_2_xml(con_file):
    try:
        j2x_file = read_json_file(con_file)
        xml_conversion = dicttoxml(j2x_file, attr_type=False, root=False)
        if xml_conversion:
            xml_decode = xml_conversion.decode()  # convert it to string
            xml_file = open("encrypted.xml", "w")
            xml_file.write(xml_decode)
            xml_file.close()
    except AttributeError:
        print("File content might be empty")
        exit(1)
    except IOError:
        print("Input output stream error")
        exit(1)


def gen_key():
    key = Fernet.generate_key()
    with open("aes_key.key", "wb") as key_file:
        key_file.write(key)


def encrypt_file(filename, key):
    try:
        fer_key = Fernet(key)
        if fer_key:
            print("Encrypting the file using key")
            with open(filename, "rb") as file:
                file_data = file.read()
                encrypted_data = fer_key.encrypt(file_data)
                if encrypted_data:
                    print("Updating the encrypted data to file")
                    with open(filename, "wb") as file:
                        file.write(encrypted_data)
        if os.path.exists(filename):
            print("Encrypted file is created")

    except FileNotFoundError:
        print("{} file is not found").format(filename)
        exit(1)
    except IOError:
        print("File Write Error")
        exit(1)


def main():
    parse = argparse.ArgumentParser(description="Provided the json file and get "
                                                "encrypted xml file")
    parse.add_argument("file", help="Mandatory to provide File to encrypt/decrypt")
    parse.add_argument("--genrate", dest="generate_key", action="store_true",
                       help="generate a new key, used for encryption")
    parse.add_argument("--encrypt", dest="encrypt", action="store_true",
                       help="encrypt the file.")

    args = parse.parse_args()

    input_file = args.file
    generate_key = args.generate_key
    encrypt = args.encrypt

    if encrypt:
        if generate_key:
            gen_key()
        convert_json_2_xml(input_file)
        read_key = open("aes_key.key", "rb").read()
        encrypt_file('encrypted.xml', read_key)
        print("Created a new encrypted xml file encrypted.xml, you can use it for decryption")


if __name__ == '__main__':
    main()
