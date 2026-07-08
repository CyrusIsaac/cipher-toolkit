# 🔐 The Cipher Toolkit: A Modular Encryption Playground

Hey there! Welcome to my Encryption Toolkit. 🚀

This is a clean, lightweight, and interactive Command-Line Interface (CLI) application written in Python. I built this project to explore how historical and modern encryption algorithms work under the hood. 

Instead of jamming all the logic into one massive script, I designed it **modularly**. Every cipher lives in its own dedicated Python file, and they are all seamlessly orchestrated by a central controller (`main.py`). It’s an awesome resource for anyone learning Python architecture, string manipulation, or basic cryptography!

---

## 🛠️ Inside the Toolkit

Here are the ciphers I implemented from scratch:

1. **Caesar Cipher:** The classic alphabet shifter. Moves your letters forward based on a numeric key.
2. **Atbash Cipher:** An ancient substitution cipher that mirrors the alphabet completely backwards (A becomes Z, B becomes Y).
3. **XOR Cipher:** A fast bitwise algorithm that scrambles text binary data using a numeric key. (Pro tip: running the encryption algorithm twice decrypts it automatically!).
4. **Vigenère Cipher:** An evolution of Caesar that uses a keyword instead of a number, making your shifts dynamic and harder to crack.
5. **ROT13 Cipher:** A special 13-place Caesar rotation where your key is fixed. Running it a second time flips it right back to normal text.

---

## 📂 Project Architecture

The folder structure looks like this:
```text
├── main.py            # The main CLI control room and menu interface
├── caesarcipher.py    # Caesar cipher math logic
├── atbash.py          # Alphabet mirroring logic
├── xor.py             # Bitwise XOR data manipulation
├── vigenere.py        # Keyword polyalphabetic shifting 
└── rot13.py           # Fixed 13-step rotation script
```

---

## 🚀 How to Run It Anywhere (Linux, macOS, Windows)

Since this project has zero external dependencies and uses pure standard Python libraries, you can run it instantly on any system!

### 1. Download the Code
Fire up your Linux terminal or local command prompt and clone this repository:
```bash
git clone https://github.com/CyrusIsaac/cipher-toolkit
```

### 2. Step Into the Folder
Move into the project directory:
```bash
cd YOUR_REPOSITORY_NAME
```

### 3. Launch the Toolkit
Run the main controller file using Python:
```bash
python main.py
```
*(Note: If you are running on a standard Linux setup, you might need to type `python3 main.py` instead).*

---

## 💡 Notes for Curious Minds
* **Educational Purpose Only:** These tools are built from scratch to show you the programming logic behind standard ciphers. Please don't use them to secure actual user passwords or banking details in production! 
* **Input Restrictions:** When using the XOR cipher, make sure your secret key is a *number* (between 1 and 255). Passing a text string as a key will make the program safely reject it.

Feel free to fork this, play around with the formulas, or add your own ciphers to the hub! Happy coding! 💻
