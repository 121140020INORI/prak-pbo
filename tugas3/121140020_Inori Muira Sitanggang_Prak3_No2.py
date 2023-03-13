class Ket(object):
  #Kelas berbentuk privat karena hanya dapat diakses dalam kelas itu sendiri, dan atribut status menjadi salah satu contoh atribut yang privat
  def __init__(self,nama,status,harga_asli):
      self.__nama=nama
      self.__status=status
      self.__harga_asli=harga_asli

  #Kelas publik Sapa dapat diakses diluar kelas itu sendiri
  def Sapa(self):
      print("Ada diskon besar-besaran perabot rumah tangga hanya hari ini sampai 95%!")
  #Kelas Info berbentuk protected karena masih bisa diakses diluar kelas itu sendiri atau turunan kelasnya 
  def Info(self):
      print("INFO")
      print("Toko   :" + self._Ket__nama)
      print("status :" + self._Ket__status)

class Toko(Ket):
  def __init__(self,nama,status,harga_asli,kode_barang):
      super().__init__(nama,status,harga_asli)      
      self.__kode_barang=kode_barang #atribut kode_barang yang bersifat private
  def Salam(self):
      print("Halo FamilyMart! kami {} {} Lho!".format(
          self._Ket__nama,self._Ket__status)) # yang ditampilkan hanya nama toko dan status diskon, harga asli barang dan kode barang tidak ditampilkan
      self.Sapa()

a=Toko("FamMart","sedang potong harga",10000000,40020)
a.Salam()
a.Info()
