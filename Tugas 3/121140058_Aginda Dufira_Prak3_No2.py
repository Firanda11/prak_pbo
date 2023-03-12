#Aginda Dufira
#Tugas 3
#No 2

class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.no_pelanggan = no_pelanggan
        self.nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append(self)

    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print(f"Halo {self.nama_pelanggan}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    def lihat_saldo(self):
        print(f"{self.nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")

    def tarik_tunai(self):
        nominal = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if nominal > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= nominal
            print("Saldo berhasil ditarik!")

    def transfer(self):
        nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_rek_tujuan = int(input("Masukkan no rekening tujuan: "))
        pelanggan_tujuan = None
        for pelanggan in AkunBank.list_pelanggan:
            if pelanggan.no_pelanggan == no_rek_tujuan:
                pelanggan_tujuan = pelanggan
                break
        if pelanggan_tujuan is None:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama .")
        else:
            if nominal > self.__jumlah_saldo:
                print("Nominal saldo yang Anda punya tidak cukup!")
            else:
                self.__jumlah_saldo -= nominal
                pelanggan_tujuan.__jumlah_saldo += nominal
                print(f"Transfer Rp {nominal} ke {pelanggan_tujuan.nama_pelanggan} sukses!")

# contoh penggunaan
Akun1 = AkunBank(1234, "Aginda Dufira", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.lihat_menu()
while True:
    pilihan = int(input("Masukkan nomor input: "))
    if pilihan == 1:
        Akun1.lihat_saldo()
    elif pilihan == 2:
        Akun1.tarik_tunai()
    elif pilihan == 3:
        Akun1.transfer()
    elif pilihan == 4:
        break
    else:
        print("Input tidak valid!")
    Akun1.lihat_menu()
