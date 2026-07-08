def atbash(text):
    encrypted_text=""
    for char in text:
        if char.isupper():
            new_char=chr(155-ord(char))
            encrypted_text+=new_char
        elif char.islower():
            new_char=chr(219-ord(char))
            encrypted_text+=new_char
        else:
            encrypted_text+=char
    return encrypted_text
