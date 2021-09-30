import os
from caesarCipher_art import logo
from caesarCipher_encode import encode
from caesarCipher_decode import decode

game_continue = True
while(game_continue):
    os.system('clear')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26
        encode(text = text, shift = shift, list_of_letters = alphabet)
        
    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % 26
        decode(text = text, shift = shift, list_of_letters = alphabet)
        
    else:
        print("Wrong Input...")
    
    
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == 'no':
        game_continue = False

print("Goodbye!!")