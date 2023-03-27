# Nama  : Aginda Dufira
# NIM   : 121140058
# no2

import random

class Robot:
    jumlah_turn=0
    
    def __init__(self,nama,health,damage):
        self.nama=nama
        self.health=health
        self.damage=damage
    
    def lakukan_aksi(self,other):
        if self.nama=="Antares":
            damage=self.damage
            if self.jumlah_turn!=1 and self.jumlah_turn%3==0:
                damage*=1.5
            other.terima_aksi(damage)
            if self==robotmu:
                print(f"Robotmu ({robotmu.nama}) menyerang sebanyak {damage} DMG")
            elif self==robotlawan:
                print(f"Robot lawan ({robotlawan.nama}) menyerang sebanyak {damage} DMG")
        
        elif self.nama=="Alphasetia":
            damage=self.damage
            if self.jumlah_turn%2==0:
                self.health+=4000
                if self==robotmu:
                    print(f"Robotmu ({robotmu.nama}) menambah darah sebanyak 4000 HP")
                elif self==robotlawan:
                    print(f"Robot lawan ({robotlawan.nama}) menambah darah sebanyak 4000 HP")
            other.terima_aksi(damage)
            if self==robotmu:
                print(f"Robotmu ({robotmu.nama}) menyerang sebanyak {damage} DMG")
            elif self==robotlawan:
                print(f"Robot lawan ({robotlawan.nama}) menyerang sebanyak {damage} DMG")
        
        else:
            damage=self.damage
            if self.jumlah_turn%4==0:
                self.health+=7000
                damage*=2
                if self==robotmu:
                    print(f"Robotmu ({robotmu.nama}) menambah darah sebanyak 7000 HP")
                elif self==robotlawan:
                    print(f"Robot lawan ({robotlawan.nama}) menambah darah sebanyak 7000 HP")
            other.terima_aksi(damage)
            if self==robotmu:
                print(f"Robotmu ({robotmu.nama}) menyerang sebanyak {damage} DMG")
            elif self==robotlawan:
                print(f"Robot lawan ({robotlawan.nama}) menyerang sebanyak {damage} DMG")
        
    def terima_aksi(self,damage):
        self.health-=damage
    
    def tambah_turn(self,other):
        self.jumlah_turn+=1
        other.jumlah_turn+=1
    
    def kurang_turn(self,other):
        self.jumlah_turn-=1
        other.jumlah_turn-=1

class Antares(Robot):
    def __init__(self, nama="Antares", health=50000, damage=5000):
        super().__init__(nama,health,damage)
        
class Alphasetia(Robot):
    def __init__(self, nama="Alphasetia", health=40000, damage=6000):
        super().__init__(nama,health,damage)
        
class Lecalicus(Robot):
    def __init__(self, nama="Lecalicus", health=45000, damage=5500):
        super().__init__(nama,health,damage)

print ("Selamat datang di pertandingan robot Yamako")
while(True):
    p1=input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : ")
    if p1=="1":
        robotmu=Antares()
        break
    elif p1=="2":
        robotmu=Alphasetia()
        break
    elif p1=="3":
        robotmu=Lecalicus()
        break
    else:
        print("Pilihan tidak ada, coba lagi!")

while(True):
    p2=input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : ")
    if p2=="1":
        robotlawan=Antares()
        break
    elif p2=="2":
        robotlawan=Alphasetia()
        break
    elif p2=="3":
        robotlawan=Lecalicus()
        break
    else:
        print("Pilihan tidak ada, coba lagi!")

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting!\n")

while(robotmu.health>0 and robotlawan.health>0):
    robotmu.tambah_turn(robotlawan)
    print(f"Turn saat ini : {robotmu.jumlah_turn}")
    print(f"Robotmu ({robotmu.nama} - {robotmu.health}), robot lawan ({robotlawan.nama} - {robotlawan.health})")
    p1=int(input(f"Pilih tangan robotmu ({robotmu.nama}): "))
    p2=random.randint(1,3)
    if p2==1:
        tanganlawan="batu"
    elif p2==2:
        tanganlawan="kertas"
    else:
        tanganlawan="gunting"
    print(f"Robot lawan memilih {tanganlawan}!")
    
    if p1 == 1:
        if p2 == 1:
            print("Seri!")
        elif p2==2:
            robotlawan.lakukan_aksi(robotmu)
        else:
            robotmu.lakukan_aksi(robotlawan)
    
    elif p1 == 2:
        if p2 == 1:
            robotmu.lakukan_aksi(robotlawan)
        elif p2==2:
            print("Seri!")
        else:
            robotlawan.lakukan_aksi(robotmu)
    
    elif p1 == 3:
        if p2 == 1:
            robotlawan.lakukan_aksi(robotmu)
        elif p2==2:
            robotmu.lakukan_aksi(robotlawan)
        else:
            print("Seri!")
    
    else:
        print("Pilihan salah, coba lagi!")
        robotmu.kurang_turn(robotlawan)
        
    if robotmu.health<=0:
        print("Maaf, "+robotmu.nama+" kalah dalam pertandingan ini.")
    if robotlawan.health<=0:
        print(f"\nRobotmu ({robotmu.nama}) mengalahkan robot lawan ({robotlawan.nama})!")
        print("Selamat, "+robotmu.nama+" menang dalam pertandingan ini!")
    print()
