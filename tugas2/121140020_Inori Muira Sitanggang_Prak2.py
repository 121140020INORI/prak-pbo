#Inori Muira Sitanggang_121140020_RB

class Diri:
    jumlah_mata = 2
    jumlah_kepala = 1

    #constructor
    def __init__(self, nama, nim, kelas_PBO_siakad, jumlah_sks, absensi):
        self.nama = nama
        self.nim = nim
        self.kelas_PBO_siakad = kelas_PBO_siakad
        self.jumlah_sks = jumlah_sks
        self.absensi = absensi

    def Panggil_semua(self):
        print("Saya bernama:",self.nama)
        print("NIM saya:",self.nim)
        print("Kelas PBO saya:",self.kelas_PBO_siakad)
        print("Dan jumlah sks PBO sebesar ",self.jumlah_sks, " sks")
        print("Kehadiran:",self.absensi)

ini_objek = Diri("Inori", "121140020", "RB", 4, "Hadir")
ini_objek.Panggil_semua()
print(ini_objek.jumlah_mata)
print(ini_objek.jumlah_kepala)

    

