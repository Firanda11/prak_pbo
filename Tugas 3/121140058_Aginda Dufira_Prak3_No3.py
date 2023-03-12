#Aginda Dufira
#Tugas 3
#No 3

class Mahasiswa:
    
    jumlah_mahasiswa = 0  # atribut kelas

    def __init__(self, nama, umur, jurusan):
        self.nama = nama  # atribut public
        self._umur = umur  # atribut protected
        self.__jurusan = jurusan  # atribut private
        Mahasiswa.jumlah_mahasiswa += 1  # setiap instance akan menambahkan jumlah_mahasiswa

    # fungsi public
    def get_umur(self):
        return self._umur

    # fungsi protected
    def _get_jurusan(self):
        return self.__jurusan

    # fungsi private
    def __get_nama(self):
        return self.nama

    def display_info(self):
        print(f"Nama: {self.__get_nama()}, Umur: {self.get_umur()}, Jurusan: {self._get_jurusan()}")

# membuat instance Mahasiswa
mhs1 = Mahasiswa("Akbar", 20, "Informatika")
mhs2 = Mahasiswa("Aginda", 19, "Matematika")

# mengakses atribut public
print("Atribut Public")
print(f"Nama Mahasiswa 1: {mhs1.nama}")
print(f"Nama Mahasiswa 2: {mhs2.nama}")

# mengakses atribut protected
print("\nAtribut Protected")
print(f"Umur Mahasiswa 1: {mhs1.get_umur()}")
print(f"Umur Mahasiswa 2: {mhs2.get_umur()}")

# mengakses atribut private
print("\nAtribut Private")
# print(mhs1.__jurusan)  # tidak bisa diakses karena private
# print(mhs2.__get_nama())  # tidak bisa diakses karena private
mhs1.display_info()
mhs2.display_info()

# mengakses atribut kelas
print("\nAtribut Kelas")
print(f"Jumlah Mahasiswa: {Mahasiswa.jumlah_mahasiswa}")
