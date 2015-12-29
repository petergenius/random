#!/usr/bin/env python3
#a list of all possible letters
alphabet = "aJs`1*/C$RIm!HwMdt~&9b#)]D;i:['KhP?VLvT6GqB8Njpu(ey%3}oQA.FW>l>xX-@U0<_^=|z5r2Z{OkYf+4{n7gS=E,"
#get the message from the user
message = input("Please enter a message to encrypt: ")

#stores the encrypted message
encryptedMessage = ""

#get the secret key
key1 = int(input("first key: "))
key2 = int(input("2nd key: "))
key3 = int(input("3rd key: "))
#This action is needed as if not the program wont take key as a number
key = int (key1)
if key3 = 0:
    alphabet = "_Zn0=F(:2,vV]Tb.e;h|}l+uagJMRCE<Hj{5BO>`r#I*i9'?QApfotWU@)N31yzm>qXs-^GwDLPY=%&kK$!xS87d/~[{64"
elif key3 = 1:
    alphabet = "aJs`1*/C$RIm!HwMdt~&9b#)]D;i:['KhP?VLvT6GqB8Njpu(ey%3}oQA.FW>l>xX-@U0<_^=|z5r2Z{OkYf+4{n7gS=E,"
elif key3 = 2:
    alphabet = "}-zFN8;hV{=)yq{5XlDjd*(JvU=/Hk3r$'Kp:BQxoL|R~+S6Y>2bw?O7Gt]04T.n1!se,uW^EC&#_PM9ZfI%A>g<[m@ai`"
else:
    invalid key
#loop through each character in the message
for char in message:

    if char in alphabet:

        #find the position of the character in the alphabet
        #e.g. 'a' is position 0, 'e' is position 4, etc.
        position = alphabet.find(char)

        #add the secret key to find the encrypted character position
        # % 26 means 'go back to 0 once you get to 26'
        newPosition = (position + key) % key2 # 94

        #add the encrypted letter to the message
        #the encrypted letter is in the alphabet at newPosition
        encryptedMessage = encryptedMessage + alphabet[newPosition]

    else:

        #some characters (e.g. '£', '?') aren't in the alphabet, 
        # so just add the unencrypted letter to the message
        encryptedMessage = encryptedMessage + char
reversemessage = encryptedMessage[::-1]
print("Your message is:", reversemessage)
