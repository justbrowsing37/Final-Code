# ''' [Make sure to fill out the program header as follows.]

# Student Name: Bhanu Sugguna
# Program Title: Charecters
# Program Description: This is the third assignment for unit 6
# Date Modified/Created: 23-02-24
# Course:  G10 Dig. Tech and Inov. w/ Mr.Mah

# '''
# import os

# while True:
#     char = input("Enter a single character \n(or type 'next' to move to the next step): ").strip().lower()
#     #ask the user to enter a single charecter
#     if char.lower().strip() == 'next':
#         os.system('clear')
#         #Check if the user wants to move on
#         break
#     elif len(char) != 1:
#         #check if char has a value of more than one len.
#         print("Please enter only one character.")
#         continue
#     print("Unicode decimal representation of '{}' is: {}".format(char, ord(char)))
#     #format it so that it print the unicode decimal representation

    
# while True:
#     try:
#         num = int(input("\nEnter a number larger than 32 \n(type next to move to the 'next' step): "))
#         #get the num input from the user
#         if num < 32:
#             print("Please enter a number 32 or greater")
#             #make sure that the number meets the requirements
#             continue
#         elif num >= 32:
#             print("Unicode charecter represented by '{}' is {}".format(num, chr(num)))
#             if input("Do you want to move to the next step? (yes/no): ").lower() == "yes":
#                 os.system('clear')
#                 break
#     except ValueError:
#         print("Please enter a valid interger")
        
# while True:
#     letter = input("\nPlease input a letter of the alphabet: ").upper()
#     offset_input = 1
#     try:
#         next_letter = chr(((ord(letter) - 65 + offset_input) % 26) +65)
#         print("{} letters after {} is {}".format(offset_input, letter, next_letter))
#         if input("Do you want to move to the next step (y/n): ").lower == "y" or "yes":
#             break
#     except ValueError:
#         print("Please enter a value for the offset")

# while True:
#     word = input("Plesase type in an word: ").strip().lower()
#     wordint = str(word)
#     if word == "next":
#         break
#     else:
#         for i in word:
#             acsii = ord(i)
#             print(f"{i.upper()} is equal to {acsii}")
#         if word == "next":
#             break
        
while True:
    letter = input("Please type a letter of the alphabet: ")
    offset = int(input("Please type a number: "))
    try:
        next_letter = chr(((ord(letter) - 65 + offset) % 26) +65)
        print(f"{offset} letters after {letter.upper()} is {next_letter}")
        if input("Do you want to move on? (y/n): ").lower() == "y" or "yes":
            print("\n\n\nThere is nothing else here to do... \n\nGoodbye")
            break
    except ValueError:
        print("Please enter a valid latter of the alphabet")