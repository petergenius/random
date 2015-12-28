#!/usr/bin/env python3
#a list of the letters to encrypt
alphabet = "lbuk26cq3igrh9fsmnjevtw57d8x40zypoa1"

#get the message from the user
message = input("Please enter a message to encrypt: ").lower()

#this variable will store the encrypted message
encryptedMessage = ""

#get the secret key
key = input("Please enter the key: ")
#This action is needed as if not the program wont take key as a number
key = int (key)

#loop through each character in the message
for char in message:

    if char in alphabet:

        #find the position of the character in the alphabet
        #e.g. 'a' is position 0, 'e' is position 4, etc.
        position = alphabet.find(char)

        #add the secret key to find the encrypted character position
        # % 26 means 'go back to 0 once you get to 26'
        newPosition = (position + key) % 36

        #add the encrypted letter to the message
        #the encrypted letter is in the alphabet at newPosition
        encryptedMessage = encryptedMessage + alphabet[newPosition]

    else:

        #some characters (e.g. '£', '?') aren't in the alphabet, 
        # so just add the unencrypted letter to the message
        encryptedMessage = encryptedMessage + char

print("Your encrypted message is:" , encryptedMessage)
