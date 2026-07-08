def xor(text , key):
    encrypted_text=""
    for char in text:
        new_char=chr(ord(char)^key)
        encrypted_text+=new_char
    return encrypted_text
