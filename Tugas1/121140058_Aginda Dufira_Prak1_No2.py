#Latihan No 2

username = "informatika"
password = "12345678"
counter = 0

while counter < 3:
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    if input_username == username and input_password == password:
        print("Berhasil login!")
        break
    else:
        print("Username atau password salah. Coba lagi.")
        counter += 1

if counter == 3:
    print("Akun Anda telah diblokir.")
