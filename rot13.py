def rot13(text):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - 65 + 13) % 26 + 65)
            encrypted_text += new_char
        elif char.islower():
            new_char = chr((ord(char) - 97 + 13) % 26 + 97)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text
