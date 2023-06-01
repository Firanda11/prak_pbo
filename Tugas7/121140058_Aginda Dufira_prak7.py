import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Fungsi untuk enkripsi teks menggunakan Vigenere cipher
def encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(plain_text):
        key_index = i % key_length
        key_char = key[key_index]
        if char.isalpha():
            char = chr((ord(char.upper()) + ord(key_char.upper()) - 2 * ord('A')) % 26 + ord('A'))
        encrypted_text += char
    return encrypted_text

# Fungsi untuk membuka file teks
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                text = file.read()
            text_entry.delete('1.0', tk.END)
            text_entry.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror('Error', f'Failed to open file: {str(e)}')

# Fungsi untuk menyimpan file hasil enkripsi
def save_file(encrypted_text):
    file_path = filedialog.asksaveasfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(encrypted_text)
            messagebox.showinfo('Success', 'File saved successfully.')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save file: {str(e)}')

# Fungsi untuk mengenkripsi teks saat tombol "Encrypt" ditekan
def encrypt_text():
    text = text_entry.get('1.0', tk.END).strip()
    key = key_entry.get().strip()
    if not text or not key:
        messagebox.showwarning('Warning', 'Please enter text and key.')
        return
    encrypted_text = encrypt(text, key)
    save_file(encrypted_text)

# Inisialisasi GUI
root = tk.Tk()
root.title('Vigenere Cipher')
root.geometry('400x300')

# Frame utama
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Label untuk judul
title_label = tk.Label(main_frame, text='Vigenere Cipher', font=('Helvetica', 16, 'bold'))
title_label.pack(pady=10)

# Frame untuk input teks
text_frame = tk.Frame(main_frame)
text_frame.pack(pady=10)

# Label dan Textbox untuk teks
text_label = tk.Label(text_frame, text='Text:')
text_label.pack(side=tk.LEFT)
text_entry = tk.Text(text_frame, height=5, width=30)
text_entry.pack(side=tk.LEFT)

# Frame untuk input key
key_frame = tk.Frame(main_frame)
key_frame.pack(pady=10)

# Label dan Textbox untuk key
key_label = tk.Label(key_frame, text='Key:')
key_label.pack(side=tk.LEFT)
key_entry = tk.Entry(key_frame, width=30)
key_entry.pack(side=tk.LEFT)

# Tombol untuk membuka file
open_button = tk.Button(main_frame, text='Open File', command=open_file)
open_button.pack(pady=5)

# Tombol untuk mengenkripsi teks
encrypt_button = tk.Button(main_frame, text='Encrypt', command=encrypt_text)
encrypt_button.pack(pady=5)

# Jalankan GUI
root.mainloop()
