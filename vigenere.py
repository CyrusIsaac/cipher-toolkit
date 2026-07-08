def vigenere(text, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - 65
            if char.isupper():
                new_char = chr((ord(char) - 65 + shift) % 26 + 65)
                encrypted_text += new_char
                key_index += 1
            elif char.islower():
                new_char = chr((ord(char) - 97 + shift) % 26 + 97)
                encrypted_text += new_char
                key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

