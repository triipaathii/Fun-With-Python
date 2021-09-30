def decode(text, shift, list_of_letters):
    message = []
    for i in range(len(text)):
        if text[i] in list_of_letters:
            position = list_of_letters.index(text[i])
            if position-shift < 0:
                position += 26 - shift 
            else:
                position-=shift
            message += list_of_letters[position]
        else:
            message += text[i]
    print(f"Your decrypted message will be: " +"".join(message))