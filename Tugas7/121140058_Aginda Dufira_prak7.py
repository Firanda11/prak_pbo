import tkinter as tk
from tkinter import filedialog, messagebox

class VigenereCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vigenere Cipher")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_text = tk.Label(self.root, text="Enter the text:")
        self.label_text.pack()
        
        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack()
        
        self.label_key = tk.Label(self.root, text="Enter the key:")
        self.label_key.pack()
        
        self.key_entry = tk.Entry(self.root, width=50)
        self.key_entry.pack()
        
        self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack()
        
        self.decrypt_button = tk.Button(self.root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack()
        
        self.save_button = tk.Button(self.root, text="Save to File", command=self.save_to_file)
        self.save_button.pack()
        
    def encrypt_text(self):
        plaintext = self.text_entry.get()
        key = self.key_entry.get()
        ciphertext = self.vigenere_encrypt(plaintext, key)
        messagebox.showinfo("Encryption Result", "Ciphertext: " + ciphertext)
        
    def decrypt_text(self):
        ciphertext = self.text_entry.get()
        key = self.key_entry.get()
        plaintext = self.vigenere_decrypt(ciphertext, key)
        messagebox.showinfo("Decryption Result", "Plaintext: " + plaintext)
        
    def save_to_file(self):
        ciphertext = self.text_entry.get()
        save_path = filedialog.asksaveasfilename(defaultextension=".txt")
        
        try:
            with open(save_path, "w") as file:
                file.write(ciphertext)
            messagebox.showinfo("Save to File", "File saved successfully.")
        except OSError:
            messagebox.showerror("Save to File", "Failed to save file. Folder not found.")
        
    def vigenere_encrypt(self, text, key):
        encrypted_text = ""
        key_len = len(key)
        for i in range(len(text)):
            char = text[i]
            if char.isalpha():
                key_char = key[i % key_len].upper()
                if char.islower():
                    encrypted_char = chr((ord(char) - 97 + ord(key_char) - 65) % 26 + 97)
                else:
                    encrypted_char = chr((ord(char) - 65 + ord(key_char) - 65) % 26 + 65)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text
    
    def vigenere_decrypt(self, text, key):
        decrypted_text = ""
        key_len = len(key)
        for i in range(len(text)):
            char = text[i]
            if char.isalpha():
                key_char = key[i % key_len].upper()
                if char.islower():
                    decrypted_char = chr((ord(char) - 97 - ord(key_char) + 65) % 26 + 97)
                else:
                    decrypted_char = chr((ord(char) - 65 - ord(key_char) + 65) % 26 + 65)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text


if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereCipherGUI(root)
    root.mainloop()
