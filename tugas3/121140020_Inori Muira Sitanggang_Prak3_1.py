class AkunBank:
  list_pelanggan={}
  def __init__(self, nomor, nama, saldo):
    self.__no_pelanggan=nomor
    self.__nama_pelanggan=nama
    self.__jumlah_saldo=saldo
    AkunBank.list_pelanggan.update({self.__no_pelanggan:self.__nama_pelanggan})
    self.menu=0

  def lihat_saldo(self):
    print("Akun Bank ",self.__nama_pelanggan,"memiliki saldo Rp", self.__jumlah_saldo)

  def tarik_tunai(self):
    self.jumlahtarik=int(input("Masukkan jumlah nominal yang ingin ditarik: "))
    if self.jumlahtarik > self.__jumlah_saldo:
      print("Nominal saldo Anda tidak mencukupi!")
    else:
      print("Saldo berhasil ditarik.")
      self.__jumlah_saldo-=self.jumlahtarik

  def transfer(self):
    self.jumlahtrasfer=int(input("Masukkan jumlah nominal yang ingin ditransfer: "))
    if self.jumlahtrasfer <= self.__jumlah_saldo:
      self.atmtujuan=int(input("Masukkan nomor rekening yang dituju: "))
      if self.atmtujuan in AkunBank.list_pelanggan:
        print("Transfer Rp",self.jumlahtrasfer,"ke", AkunBank.list_pelanggan[self.atmtujuan],"sukses!")
        self.__jumlah_saldo-=self.jumlahtrasfer

      else:
        print("Nomor rekening tujuan tidak dikenal. Sistem akan kembali ke menu utama")
    else:
      print("Nominal saldo yang Anda punya tidak mencukupi")

  def lihat_menu(self):
    print("Selamat datang di Bank Jago")
    print("Halo", self.__nama_pelanggan,"Apa yang ingin anda lakukan?")
    print("1. Cek saldo\n2. Tarik tunai\n3. Transfer\n4. Keluar")
    self.menu=int(input("Masukkan opsi: "))
    if self.menu == 1:
      AkunBank.lihat_saldo(self)
    elif self.menu == 2:
      AkunBank.tarik_tunai(self)
    elif self.menu == 3:
      AkunBank.transfer(self)

Akun1=AkunBank(1234, "Inori", 5000000000)
Akun2=AkunBank(2345, "Ukraina", 6666666666)
Akun3=AkunBank(3456, "Elon Musk", 9999999999)

while Akun1.menu < 4:
  Akun1.lihat_menu()
  print()
print("\nTerima kasih.")
