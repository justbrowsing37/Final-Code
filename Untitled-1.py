''' [Make sure to fill out the program header as follows.]

Student Name: Bhanu Sugguna
Program Title: Caesar cipher
Program Description: This si the last assignment for unit 6
Date Modified/Created: 2024-05-08
Course: G10 Dig. Tech and Inov. w/ Mr. Mah
'''

import random
import math

# Function to encrypt a message using Caesar Cipher
def caesar_cipher_encrypt(message, rotation_factor):
    encrypted_message = ''
    for char in message:
        if char.isalpha():  # Check if the character is alphabetic
            shift = 65 if char.isupper() else 97  # Determine the ASCII value for 'A' or 'a'
            encrypted_char = chr((ord(char) - shift + rotation_factor) % 26 + shift)  # Encrypt the character
            encrypted_message += encrypted_char  # Add the encrypted character to the encrypted message
        else:
            encrypted_message += char  # If the character is not alphabetic, keep it unchanged
    return encrypted_message

# Function to decrypt a message using Caesar Cipher
def caesar_cipher_decrypt(message, rotation_factor):
    return caesar_cipher_encrypt(message, -rotation_factor)  # Decrypting using Caesar Cipher is just encrypting with negative rotation factor

# Function to encrypt a message using Vigenere Cipher
def vigenere_cipher_encrypt(message, keyword):
    encrypted_message = ''
    key_index = 0
    for char in message:
        if char.isalpha():  # Check if the character is alphabetic
            shift = ord(keyword[key_index % len(keyword)].upper()) - 65  # Determine the shift for this character based on the keyword
            encrypted_char = caesar_cipher_encrypt(char, shift)  # Encrypt the character using Caesar Cipher with the determined shift
            encrypted_message += encrypted_char  # Add the encrypted character to the encrypted message
            key_index += 1  # Move to the next character in the keyword
        else:
            encrypted_message += char  # If the character is not alphabetic, keep it unchanged
    return encrypted_message

def vigenere_cipher_decrypt(message, keyword):
    decrypted_message = ''
    key_index = 0
    for char in message:
        if char.isalpha():  # Check if the character is alphabetic
            shift = ord(keyword[key_index % len(keyword)].upper()) - 65  # Determine the shift for this character based on the keyword
            decrypted_char = caesar_cipher_decrypt(char, shift)  # Decrypt the character using Caesar Cipher with the determined shift
            decrypted_message += decrypted_char  # Add the decrypted character to the decrypted message
            key_index += 1  # Move to the next character in the keyword
        else:
            decrypted_message += char  # If the character is not alphabetic, keep it unchanged
    return decrypted_message


# Function to generate RSA key pair
def generate_keypair(p, q):
    n = p * q  # Compute the modulus
    phi = (p - 1) * (q - 1)  # Compute Euler's totient function

    # Choose a random integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Compute the modular multiplicative inverse of e (mod phi)
    d = pow(e, -1, phi)

    return ((e, n), (d, n))  # Return the public and private keys

# Function to encrypt a message using RSA
def rsa_encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]  # Encrypt each character using the public key
    return encrypted_message

# Function to decrypt a message using RSA
def rsa_decrypt(message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in message])  # Decrypt each encrypted character using the private key
    return decrypted_message

# Function to save a key to a file
def save_key(filename, key):
    with open(filename, 'w') as f:
        f.write(','.join(map(str, key)))  # Write the key to the file as comma-separated values

# Function to load a key from a file
def load_key(filename):
    with open(filename, 'r') as f:
        return tuple(map(int, f.readline().strip().split(',')))  # Read the key from the file and convert it to a tuple of integers

# Function to get the rotation factor for Caesar Cipher encryption/decryption
def get_rotation_factor():
    while True:
        try:
            rotation_factor = int(input("Enter the rotation factor (0-25): "))  # Prompt the user to enter the rotation factor
            if 0 <= rotation_factor <= 25:  # Check if the rotation factor is within the valid range
                return rotation_factor
            else:
                print("Rotation factor must be within 0 and 25.")  # Display an error message if the rotation factor is invalid
        except ValueError:
            print("Invalid input. Please enter an integer.")  # Display an error message if the input is not an integer

# Function to get the keyword for Vigenere Cipher encryption/decryption
def get_keyword():
    while True:
        keyword = input("Enter the keyword: ")  # Prompt the user to enter the keyword
        if all(char.isalpha() for char in keyword):  # Check if the keyword contains only alphabetic characters
            return keyword
        else:
            print("The keyword must only contain alphabetic letters.")  # Display an error message if the keyword contains non-alphabetic characters

# Main function
def main():
    while True:
        print("\n\nChoose an option:")
        print("1. Encrypt a message using Caesar Cipher")
        print("2. Decrypt a message using Caesar Cipher")
        print("3. Encrypt a message using Vigenere Cipher")
        print("4. Decrypt a message using Vigenere Cipher")
        print("5. Encrypt a message using RSA")
        print("6. Decrypt a message using RSA")
        print("7. Save RSA key to file")
        print("8. Load RSA key from file")
        print("9. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")  # Prompt the user to enter their choice
        print("-------------------------------------------------------")
        
        # Process the user's choice
        if choice == '1':
            message = input("Enter the message to encrypt: ")  # Prompt the user to enter the message
            rotation_factor = get_rotation_factor()  # Get the rotation factor from the user
            encrypted_message = caesar_cipher_encrypt(message, rotation_factor)  # Encrypt the message using Caesar Cipher
            print("Encrypted Message:", encrypted_message)  # Print the encrypted message

        elif choice == '2':
            try:
                message = input("Enter the message to decrypt: ")  # Prompt the user to enter the message
                rotation_factor = get_rotation_factor()  # Get the rotation factor from the user
                decrypted_message = caesar_cipher_decrypt(message, rotation_factor)  # Decrypt the message using Caesar Cipher
                print("Decrypted Message:", decrypted_message)  # Print the decrypted message
            except TypeError:
                print("Unable to decrypt message...\n\nPlease try again\n")

        elif choice == '3':
            message = input("Enter the message to encrypt: ")  # Prompt the user to enter the message
            keyword = get_keyword()  # Get the keyword from the user
            encrypted_message = vigenere_cipher_encrypt(message, keyword)  # Encrypt the message using Vigenere Cipher
            print("Encrypted Message:", encrypted_message)  # Print the encrypted message

        elif choice == '4':
            try:
                message = input("Enter the message to decrypt: ")  # Prompt the user to enter the message
                keyword = get_keyword()  # Get the keyword from the user
                decrypted_message = vigenere_cipher_decrypt(message, keyword)  # Decrypt the message using Vigenere Cipher
                print("Decrypted Message:", decrypted_message)
            except TypeError:
                print("Unable to decrypt message...\n\nPlease try again\n")  # Print the decrypted message

        elif choice == '5':
            message = input("Enter the message to encrypt: ")  # Prompt the user to enter the message
            p = int(input("Enter a prime number (p): "))  # Prompt the user to enter a prime number
            q = int(input("Enter another prime number (q): "))  # Prompt the user to enter another prime number
            public_key, private_key = generate_keypair(p, q)  # Generate the RSA key pair
            encrypted_message = rsa_encrypt(message, public_key)  # Encrypt the message using RSA
            print("Encrypted Message:", encrypted_message)  # Print the encrypted message
            print("RSA public key:", public_key)  # Print the RSA public key
            print("RSA private key:", private_key)  # Print the RSA private key

        elif choice == '6':
            message = input("Enter the message to decrypt (comma-separated): ").split(',')  # Prompt the user to enter the encrypted message
            private_key = tuple(int(x) for x in input("Enter the private key (d,n): ").split(','))  # Prompt the user to enter the private key
            decrypted_message = rsa_decrypt(message, private_key)  # Decrypt the message using RSA
            print("Decrypted Message:", decrypted_message)  # Print the decrypted message
        

        elif choice == '7':
            filename = input("Enter the filename to save the RSA key: ")  # Prompt the user to enter the filename
            key = tuple(int(x) for x in input("Enter the RSA key (e,n): ").split(','))  # Prompt the user to enter the RSA key
            save_key(filename, key)  # Save the RSA key to a file
            print("RSA key saved to", filename)  # Print a confirmation message

        elif choice == '8':
                filename = input("Enter the filename to load the RSA key from: ")  # Prompt the user to enter the filename
                key = load_key(filename)  # Load the RSA key from the file
                print("RSA key loaded from", filename, ":", key)  # Print the loaded RSA key

        elif choice == '9':
            print("Goodbye!")  # Print a farewell message
            break  # Exit the program

        else:
            print("Invalid choice. Please choose again.")  # Display an error message if the choice is invalid

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function