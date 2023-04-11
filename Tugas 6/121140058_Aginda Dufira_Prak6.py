# Nama : Aginda Dufira
# NIM  : 121140058
# Kelas : RB

from abc import ABC, abstractmethod
from datetime import date

class AkunBank(ABC):
    def __init__(self, nama: str, tahun_daftar: int, saldo: float):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
    
    @abstractmethod
    def transfer_saldo(self, jumlah: float):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
    def lihat_saldo(self):
        print(f"Saldo {self.nama}: {self.saldo}")
    
    def hitung_usia(self):
        today = date.today()
        return today.year - self.tahun_daftar
    
class AkunGold(AkunBank):
    def transfer_saldo(self, jumlah: float):
        usia = self.hitung_usia()
        if usia >= 3:
            if jumlah > 100000:
                self.saldo -= jumlah
            else:
                self.saldo -= jumlah + 2000
        else:
            if jumlah > 100000:
                self.saldo -= jumlah + 2000
            else:
                self.saldo -= jumlah
    
    def lihat_suku_bunga(self):
        if self.hitung_usia() >= 3 and self.saldo >= 1000000000:
            print("Suku bunga: 1%")
        elif self.saldo >= 1000000000:
            print("Suku bunga: 2%")
        else:
            print("Suku bunga: 3%")
        
class AkunSilver(AkunBank):
    def transfer_saldo(self, jumlah: float):
        usia = self.hitung_usia()
        if usia >= 3:
            if jumlah > 100000:
                self.saldo -= jumlah
            else:
                self.saldo -= jumlah + 2000
        else:
            if jumlah > 100000:
                self.saldo -= jumlah + 5000
            else:
                self.saldo -= jumlah
    
    def lihat_suku_bunga(self):
        if self.hitung_usia() >= 3 and self.saldo >= 10000000:
            print("Suku bunga: 1%")
        elif self.saldo >= 10000000:
            print("Suku bunga: 2%")
        else:
            print("Suku bunga: 3%")

# contoh penggunaan
akun_gold = AkunGold("Andi", 2018, 1500000000)
akun_silver = AkunSilver("Budi", 2020, 8000000)

akun_gold.lihat_saldo()
akun_gold.transfer_saldo(200000)
akun_gold.lihat_saldo()
akun_gold.lihat_suku_bunga()

akun_silver.lihat_saldo()
akun_silver.transfer_saldo(50000)
akun_silver.lihat_saldo()
akun_silver.lihat_suku_bunga()
