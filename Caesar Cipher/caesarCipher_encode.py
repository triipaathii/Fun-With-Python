def encode(text, shift, list_of_letters):
    message = []
    for i in range(len(text)):
        if text[i] in list_of_letters:
            position = list_of_letters.index(text[i])
            if position+shift > 25:
                position += shift - 26
            else:
                position+=shift
            message += list_of_letters[position]
        else:
            message += text[i]
    print(f"Your encrypted message will be: " +"".join(message))