from caesarcipher import caesar
from atbash import atbash
from xor import xor
from vigenere import vigenere
from rot13 import rot13

def main():
    print("--- Welcome to Encryption Toolkit ---")
    print("1. Caesar Cipher")
    print("2. Atbash Cipher")
    print("3. XOR Cipher")
    print("4. Vigenère Cipher")
    print("5. ROT13 Cipher")
    print("6. Exit")
    
    choice = input("Choose Encryption Type: ")
    
    # Agar user 6 select kare toh furan exit ho jaye
    if choice == "6":
        print("Goodbye!")
        return
        
    # Agar choice 1 se 5 ke darmiyan nahi hai toh invalid choice de
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice!")
        return

    # Sahi choice par hi text input mange ga
    text = input("\nEnter the text to encrypt: ")
    secret_message = ""
    
    if choice == "1":
        shift = int(input("Enter Caesar shift: "))
        secret_message = caesar(text, shift) 
        
    elif choice == "2":
        secret_message = atbash(text)      
        
    elif choice == "3":
        key = int(input("Enter XOR numeric key: "))
        secret_message = xor(text, key) 
        
    elif choice == "4":
        key = input("Enter Vigenère keyword: ")
        secret_message = vigenere(text, key)  
        
    elif choice == "5":
        secret_message = rot13(text)        

    print("\n==============================")
    print(f"Original Text: {text}")
    print(f"Secret Cipher: {secret_message}")
    print("==============================")

if __name__ == "__main__":
    main()
