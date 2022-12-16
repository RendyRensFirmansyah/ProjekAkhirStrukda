import json
import pandas as pd
import os

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.awal = None
    def isEmpty(self):
        return self.awal == None
    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.awal
        self.awal = newNode
    def get(self, index):
        if self.isEmpty() or index<1 or index>self.size():
            return None
        else:
            bantu = self.awal
            posisi = 1
            while posisi < index :
                bantu = bantu.next
                posisi = posisi + 1
            return bantu
    def getFirst(self):
        return self.awal
    def size(self):
        if self.isEmpty():
            banyakNode = 0
        else:
            bantu = self.awal
            banyakNode = 1
            while bantu.next is not None:
                banyakNode = banyakNode + 1
                bantu = bantu.next
        return banyakNode
    def getLast(self):
        if self.isEmpty():
            return None
        else:
            bantu = self.awal
            while bantu.next is not None:
                bantu = bantu.next
            return bantu
    def addData(self, data):
        if self.isEmpty():
            self.addFirst(data)
        else:
            newNode = Node(data)
            last = self.getLast()
            last.next = newNode
    def removeFirst(self):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        else:
            first = self.getFirst()
            self.awal = self.awal.next 
            del first
    def remove(self, index):
        import os,time
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        elif index+1 ==1:
            self.removeFirst()
            # print("\nData Berhasil Dihapus")
            os.system("cls")
            print()
            print()
            print("=================================================")
            print("|         Data Deleted Succesfully .... ✔       |")
            print("=================================================")
            time.sleep(1)
        else:
            prevNode = self.get(index)
            if prevNode is None:
                print("Data yang akan dihapus tidak ditemukan")
            else:
                removedNode = prevNode.next
                prevNode.next = removedNode.next
                del removedNode
                # print("\nData Berhasil Dihapus")
                os.system("cls")
                print()
                print()
                print("=================================================")
                print("|         Data Deleted Succesfully .... ✔       |")
                print("=================================================")
                time.sleep(1)
    def sendJson(self):
        if self.isEmpty():
            return []
        else:
            bantu = self.awal
            datajs = []
            while bantu is not None:
                datajs.append(bantu.info)
                bantu = bantu.next
                
            return datajs
    def updateKTP(self, index):
        import os,time
        nodeUpdate = self.get(index+1)
        if nodeUpdate is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            nodeUpdate.info = {
                    'Pemerintah Provinsi': input("Masukan Nama Provinsi : "),
                    'Pemerintah Kabupaten/Kota': input("Masukan Nama Kabupaten/Kota: "),
                    'Kecamatan': input("Masukan Nama Kecamatan : "),
                    'Kelurahan/Desa': (input("Masukan Nama Kelurahan/Desa : ")),
                    'Permohonan EKTP': (input("1. Baru | 2. Perpanjangan | 3. Penggantian : ")),
                    'Nama Lengkap': (input("Masukan Nama Lengkap : ")),
                    'Nomor Kartu Keluarga': (input("Masukan Nomor KK : ")),
                    'NIK': (input("Masukan Nomor NIK : ")),
                    'Alamat': (input("Masukan Alamat : "))
            }
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Recorded .... ⟳       |")
            print("===============================================")
            time.sleep(1.5)
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Updated .... ✔        |")
            print("===============================================")
            time.sleep(1)
    def updateKK(self, index):
        import os,time
        nodeUpdate = self.get(index+1)
        if nodeUpdate is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            nodeUpdate.info = {
                'Pemerintah Provinsi': input("Masukan Nama Provinsi : "),
                'Pemerintah Kabupaten/Kota': input("Masukan Nama Kabupaten/Kota: "),
                'Kecamatan': input("Masukan Nama Kecamatan : "),
                'Kelurahan/Desa': (input("Masukan Nama Kelurahan/Desa : ")),
                'Nama Lengkap Pemohon': (input("Masukan Nama Lengkap Pemohon : ")),
                'NIK Pemohon': (input("Masukan NIK Pemohon : ")),
                'No. KK Semula': (input("Masukan No. KK Semula : ")),
                'Alamat Pemohon': (input("Masukan Alamat Pemohon : ")),
                'Alasan Permohonan': (input("Masukan Alasan Permohonan : ")),
                'Jumlah Anggota Keluarga': (input("Masukan Jumlah Anggota Keluarga : ")),
                'Nama Anggota Keluarga 1': (input("Masukan Nama Lengkap Anggota Keluarga 1 : ")),
                'Nama Anggota Keluarga 2': (input("Masukan Nama Lengkap Anggota Keluarga 2 : ")),
                'Nama Anggota Keluarga 3': (input("Masukan Nama Lengkap Anggota Keluarga 3 : ")),
                'Nama Anggota Keluarga 4': (input("Masukan Nama Lengkap Anggota Keluarga 4 : ")),
                'Nama Anggota Keluarga 5': (input("Masukan Nama Lengkap Anggota Keluarga 5 : ")),
                'Nama Anggota Keluarga 6': (input("Masukan Nama Lengkap Anggota Keluarga 6 : ")),
                'Nama Anggota Keluarga 7': (input("Masukan Nama Lengkap Anggota Keluarga 7 : ")),
            }
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Recorded .... ⟳       |")
            print("===============================================")
            time.sleep(1.5)
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Updated .... ✔        |")
            print("===============================================")
            time.sleep(1)
    def updateAK(self, index):
        import os,time
        nodeUpdate = self.get(index+1)
        if nodeUpdate is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            nodeUpdate.info = {
                'Nomor KK': input("Masukan Nomor KK : "),
                'Nama Lengkap Ibu': input("Masukan Nama Lengkap Ibu : "),
                'NIK Ibu': input("Masukan NIK Ibu : "),
                'Nama Anak': input("Masukan Nama Anak : "),
                'Tempat, Tanggal Lahir': input("Masukan Tempat, Tanggal Lahir : "),
                'Jenis Kelamin': input("Masukan Jenis Kelamin : "),
                'Anak Ke': input("Anak Ke : "),
                'Nama Saksi': input("Masukan Nama Saksi : "),
                'NIK Saksi': input("Masukan NIK Saksi : "),
                'Nomor Akta Kelahiran': input("Masukan Nomor Akta Kelahiran : ")
            }
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Recorded .... ⟳       |")
            print("===============================================")
            time.sleep(1.5)
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Updated .... ✔        |")
            print("===============================================")
            time.sleep(1)
    def updateAP(self, index):
        import os,time
        nodeUpdate = self.get(index+1)
        if nodeUpdate is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            nodeUpdate.info = {
                'Surat Bukti Perkawinan': input("Masukan Nomor Surat Bukti Perkawinan : "),
                'Nama Pria': input("Masukan Nama Lengkap Pria : "),
                'Nomor Akta Pria': input("Masukan Nomor Akta Pria : "),
                'Nama Wanita ': input("Masukan Nama Lengkap Wanita : "),
                'Nomor Akta Wanita ': input("Masukan Nomor Akta Wanita : "),
                'Surat Keterangan Lurah': input("Masukan Nomor Surat Keterangan Lurah: "),
                'NIK Pria': input("Masukan Nomor NIK Pria : "),
                'NIK Wanita': input("Masukan Nomor NIK Wanita : "),
                'Nama Saksi 1': input("Masukan Nama Saksi 1 : "),
                'Nama Saksi 2': input("Masukan Nama Saksi 2 : "),
                'NIK Saksi 1': input("Masukan Nomor NIK Saksi 1 : "),
                'NIK Saksi 2': input("Masukan Nomor NIK Saksi 2 : "),
            }
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Recorded .... ⟳       |")
            print("===============================================")
            time.sleep(1.5)
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Updated .... ✔        |")
            print("===============================================")
            time.sleep(1)
    def updateKIA(self, index):
        import os, time
        nodeUpdate = self.get(index+1)
        if nodeUpdate is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            nodeUpdate.info = {
                'NIK Ayah': input("Masukan Nomor NIK Ayah : "),
                'Nama Ayah': input("Masukan Nama Lengkap Ayah : "),
                'NIK Ibu': input("Masukan Nomor NIK Ibu : "),
                'Nama Ibu': input("Masukan Nama Lengkap Ibu: "),
                'Nama Anak': input("Masukan Nama Lengkap Anak: "),
                'Nomor Akta Kelahiran': input("Masukan Nomor Akta Kelahiran : "),
                'Nomor KK': input("Masukan Nomor KK : ")
            }
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Recorded .... ⟳       |")
            print("===============================================")
            time.sleep(1.5)
            os.system("cls")
            print()
            print()
            print("===============================================")
            print("|         Data Has Been Updated .... ✔        |")
            print("===============================================")
            time.sleep(1)
class antrianQueue:
    def __init__(self,n=50):
        self.size = n
        self.sizeIn = 0
        self.data = []
    def antrianFull(self):
        if self.sizeIn == self.size:
            return True
        else:
            return False
    def antrianKosong(self):
        if self.sizeIn == 0:
            return True
        else:
            return False
    def enqueue(self,name):
        import time
        if self.antrianFull():
            print("Mohon Maaf Sementara Ini Antrian Sudah Terlalu Penuh")
            print("Silahkan Menunggu Terlebih Dahulu ! Terima Kasih.")
        else:
            self.data.append(name)
            self.sizeIn = len(self.data)
            print(name,"Telah berhasil ditambahkan ke antrian.")
            menuCostumer()
    def dequeue(self):
        if self.antrianKosong():
            print("Antrian masih dalam keadaan kosong")
            return None
        else:
            clearData = self.data.pop(0)
            self.sizeIn == len(self.data)
            print("Antrian dengan nama :", clearData)
            print("Dimohon untuk melakukan konfirmasi")
            print("Antrian setelah ini adalah :", self.data)
        print("Tekan enter untuk lanjut")
        input()
        menuAdmin()
    def lihatAntrian(self):
        if self.antrianKosong():
            print("Saat ini antrian masih kosong")
        else:
            print("========== DAFTAR ANTRIAN MALL PELAYANAN PUBLIK ==========")
            number = 1
            for i in self.data:
                print(" "+str(number)+". ",i)
                number += 1
            print("Total antrian saat ini :", len(self.data))
        print("Tekan enter untuk lanjut")
        input()
        menuAdmin()
        

dataKTP = LinkedList()
dataKK = LinkedList()
dataAK = LinkedList()
dataAP = LinkedList()
dataKIA = LinkedList()
data2 = antrianQueue()

# Mengkonversi Data Json ke LinkedList

if os.path.exists('dataKTP.json'):
    with open('dataKTP.json', 'r') as f:
        dataKtp = json.load(f)

    for i in dataKtp:
        dataKTP.addData(i)

if os.path.exists('dataKK.json'):
    with open('dataKK.json', 'r') as f:
        dataKk = json.load(f)

    for i in dataKk:
        dataKK.addData(i)

if os.path.exists('dataAK.json'):
    with open('dataAK.json', 'r') as f:
        dataAk = json.load(f)

    for i in dataAk:
        dataAK.addData(i)

if os.path.exists('dataAP.json'):
    with open('dataAP.json', 'r') as f:
        dataAp = json.load(f)

    for i in dataAp:
        dataAP.addData(i)

if os.path.exists('dataKIA.json'):
    with open('dataKIA.json', 'r') as f:
        dataKia = json.load(f)

    for i in dataKia:
        dataKIA.addData(i)

# Main Menu
def menuCostumer():
    import os, time
    os.system("cls")
    print("======================================")
    print("     MALL PELAYANAN PUBLIK JEMBER     ")
    print("               COSTUMER               ")
    print("======================================")
    print("| 1. Ambil  Antrian                  |")
    print("| 2. Keluar                          |")
    print("======================================") 
        
    inputProgram = int(input("Pilih Daftar Menu : "))
    if inputProgram == 1:
        dataAntrian = input("Masukkan nama antrian : ")
        data2.enqueue(dataAntrian)
    else:
        os.system("cls")
        print()
        print()
        print()
        print("===================================")
        print("|      Kembali ke menu...... ⟳    |")
        print("===================================")
        time.sleep(2)
        menuHome()

def MenuKTP():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKtp():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("         Kartu Tanda Penduduk         ")
        print("======================================")
        print("\n")
        print("| 1. Tambah data pengajuan KTP       |")
        print("| 2. Edit data KTP                   |")
        print("| 3. Hapus data KTP                  |")
        print("| 4. Tampilkan data KTP              |")
        print("| 0. Keluar Program                  |")
        print("\n")
        print("======================================")
        pilih = int(input("Pilih Menu : "))
        return pilih

    def tambahData():
        import time,os
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print("      Tambah Pengajuan data KTP        ")
        print("=======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            dataKTP.addData(
            {
                    'Pemerintah Provinsi': input("Masukan Nama Provinsi : "),
                    'Pemerintah Kabupaten/Kota': input("Masukan Nama Kabupaten/Kota: "),
                    'Kecamatan': input("Masukan Nama Kecamatan : "),
                    'Kelurahan/Desa': (input("Masukan Nama Kelurahan/Desa : ")),
                    'Permohonan EKTP': (input("1. Baru | 2. Perpanjangan | 3. Penggantian : ")),
                    'Nama Lengkap': (input("Masukan Nama Lengkap : ")),
                    'Nomor Kartu Keluarga': (input("Masukan Nomor KK : ")),
                    'NIK': (input("Masukan Nomor NIK : ")),
                    'Alamat': (input("Masukan Alamat : "))
            })
            berapaData -= 1
        print("\n")
        os.system("cls")
        print()
        print()
        print("==========================================")
        print("|         Data In Progress .... ⟳        |")
        print("==========================================")
        time.sleep(1.5)
        os.system("cls")
        print()
        print()
        print("===============================================")
        print("|         Data Has Been Recorded .... ✔       |")
        print("===============================================")
        time.sleep(1)
        clear()

    def tampilkanData():
        if dataKTP.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataKTP.json', 'r') as f:
                dataKtp = json.load(f)
                dataKtp = pd.DataFrame(dataKtp)
            return print(dataKtp)

    def editData():
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print("        Edit Data Pengajuan KTP        ")
        print("=======================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        dataKTP.updateKTP(index)
        print("\n")
        clear()

    def hapusData():
        clear()
        print("========================================")
        print("      MALL PELAYANAN PUBLIK JEMBER      ")
        print("        Hapus Data Pengajuan KTP        ")
        print("========================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        dataKTP.remove(index)
        print("\n")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataKTP.json', 'w') as json_file:
            json.dump(dataKTP.sendJson(), json_file, indent=4)

        pilih = mainKtp()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("==========================================")
            print("        MALL PELAYANAN PUBLIK JEMBER      ")
            print("        Tampilan Data Pengajuan KTP       ")
            print("==========================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            menuPengajuan()
        else:
            print("Salah memilih angka !")
def MenuKK():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKK():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("            Kartu Keluarga            ")
        print("======================================")
        print("\n")
        print("| 1. Tambah data pengajuan KK        |")
        print("| 2. Edit data KK                    |")
        print("| 3. Hapus data KK                   |")
        print("| 4. Tampilkan data KK               |")
        print("| 0. Keluar Program                  |")
        print("\n")
        print("======================================")
        pilih = int(input("Pilih Menu : "))
        return pilih

    def tambahData():
        import os,time
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print(" Tambah Pengajuan data Kartu Keluarga  ")
        print("=======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            dataKK.addData(
            {
                'Pemerintah Provinsi': input("Masukan Nama Provinsi : "),
                'Pemerintah Kabupaten/Kota': input("Masukan Nama Kabupaten/Kota: "),
                'Kecamatan': input("Masukan Nama Kecamatan : "),
                'Kelurahan/Desa': (input("Masukan Nama Kelurahan/Desa : ")),
                'Nama Lengkap Pemohon': (input("Masukan Nama Lengkap Pemohon : ")),
                'NIK Pemohon': (input("Masukan NIK Pemohon : ")),
                'No. KK Semula': (input("Masukan No. KK Semula : ")),
                'Alamat Pemohon': (input("Masukan Alamat Pemohon : ")),
                'Alasan Permohonan': (input("Masukan Alasan Permohonan : ")),
                'Jumlah Anggota Keluarga': (input("Masukan Jumlah Anggota Keluarga : ")),
                'Nama Anggota Keluarga 1': (input("Masukan Nama Lengkap Anggota Keluarga 1 : ")),
                'Nama Anggota Keluarga 2': (input("Masukan Nama Lengkap Anggota Keluarga 2 : ")),
                'Nama Anggota Keluarga 3': (input("Masukan Nama Lengkap Anggota Keluarga 3 : ")),
                'Nama Anggota Keluarga 4': (input("Masukan Nama Lengkap Anggota Keluarga 4 : ")),
                'Nama Anggota Keluarga 5': (input("Masukan Nama Lengkap Anggota Keluarga 5 : ")),
                'Nama Anggota Keluarga 6': (input("Masukan Nama Lengkap Anggota Keluarga 6 : ")),
                'Nama Anggota Keluarga 7': (input("Masukan Nama Lengkap Anggota Keluarga 7 : ")),
            })
            berapaData -= 1
        print("\n")
        os.system("cls")
        print()
        print()
        print("==========================================")
        print("|         Data In Progress .... ⟳        |")
        print("==========================================")
        time.sleep(1.5)
        os.system("cls")
        print()
        print()
        print("===============================================")
        print("|         Data Has Been Recorded .... ✔       |")
        print("===============================================")
        time.sleep(1)
        clear()

    def tampilkanData():
        if dataKK.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataKK.json', 'r') as f:
                dataKk = json.load(f)
                dataKk = pd.DataFrame(dataKk)
            return print(dataKk)

    def editData():
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print("  Edit Data Pengajuan Kartu Keluarga   ")
        print("=======================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        dataKK.updateKK(index)
        print("\n")
        clear()

    def hapusData():
        clear()
        print("========================================")
        print("      MALL PELAYANAN PUBLIK JEMBER      ")
        print("  Hapus Data Pengajuan Kartu Keluarga   ")
        print("========================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        dataKK.remove(index)
        print("\n")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataKK.json', 'w') as json_file:
            json.dump(dataKK.sendJson(), json_file, indent=4)

        pilih = mainKK()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("==========================================")
            print("        MALL PELAYANAN PUBLIK JEMBER      ")
            print("  Tampilan Data Pengajuan Kartu Keluarga  ")
            print("==========================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            menuPengajuan()
        else:
            print("Salah memilih angka !")
def MenuAkteKelahiran():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainAkta():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("            Akta Kelahiran            ")
        print("======================================")
        print("\n")
        print("| 1. Tambah data pengajuan Akte Kelahiran |")
        print("| 2. Edit data Akte Kelahiran             |")
        print("| 3. Hapus data Akte Kelahiran            |")
        print("| 4. Tampilkan data Akte Kelahiran        |")
        print("| 0. Keluar Program                       |")
        print("\n")
        print("======================================")
        pilih = int(input("Pilih Menu : "))
        return pilih

    def tambahData():
        import os,time
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print(" Tambah Pengajuan data Akta Kelahiran ")
        print("======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            dataAK.addData(
            {
                'Nomor KK': input("Masukan Nomor KK : "),
                'Nama Lengkap Ibu': input("Masukan Nama Lengkap Ibu : "),
                'NIK Ibu': input("Masukan NIK Ibu : "),
                'Nama Anak': input("Masukan Nama Anak : "),
                'Tempat, Tanggal Lahir': input("Masukan Tempat, Tanggal Lahir : "),
                'Jenis Kelamin': input("Masukan Jenis Kelamin : "),
                'Anak Ke': input("Anak Ke : "),
                'Nama Saksi': input("Masukan Nama Saksi : "),
                'NIK Saksi': input("Masukan NIK Saksi : "),
                'Nomor Akta Kelahiran': input("Masukan Nomor Akta Kelahiran : ")
            })
            berapaData -= 1
        print("\n")
        os.system("cls")
        print()
        print()
        print("==========================================")
        print("|         Data In Progress .... ⟳        |")
        print("==========================================")
        time.sleep(1.5)
        os.system("cls")
        print()
        print()
        print("===============================================")
        print("|         Data Has Been Recorded .... ✔       |")
        print("===============================================")
        time.sleep(1)
        clear()

    def tampilkanData():
        if dataAK.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataAK.json', 'r') as f:
                dataAk = json.load(f)
                dataAk = pd.DataFrame(dataAk)
            return print(dataAk)

    def editData():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("  Edit Data Pengajuan Akta Kelahiran  ")
        print("======================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        dataAK.updateAK(index)
        print("\n")
        clear()

    def hapusData():
        clear()
        print("=======================================")
        print("      MALL PELAYANAN PUBLIK JEMBER     ")
        print("  Hapus Data Pengajuan Akta Kelahiran  ")
        print("=======================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        dataAK.remove(index)
        print("\n")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataAK.json', 'w') as json_file:
            json.dump(dataAK.sendJson(), json_file, indent=4)

        pilih = mainAkta()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("==========================================")
            print("        MALL PELAYANAN PUBLIK JEMBER      ")
            print("  Tampilan Data Pengajuan Akta Kelahiran  ")
            print("==========================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            menuPengajuan()
        else:
            print("Salah memilih angka !")
def MenuAktePerkawinan():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainAktaP():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("            Akta Perkawinan           ")
        print("======================================")
        print("\n")
        print("| 1. Tambah data pengajuan Akta Perkawinan |")
        print("| 2. Edit data Akta Perkawinan             |")
        print("| 3. Hapus data Akta Perkawinan            |")
        print("| 4. Tampilkan data Akta Perkawinan        |")
        print("| 0. Keluar Program                        |")
        print("\n")
        print("======================================")
        pilih = int(input("Pilih Menu : "))
        return pilih

    def tambahData():
        import os,time
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print(" Tambah Pengajuan data Akta Perkawinan ")
        print("=======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            dataAP.addData(
            {
                'Surat Bukti Perkawinan': input("Masukan Nomor Surat Bukti Perkawinan : "),
                'Nama Pria': input("Masukan Nama Lengkap Pria : "),
                'Nomor Akta Pria': input("Masukan Nomor Akta Pria : "),
                'Nama Wanita ': input("Masukan Nama Lengkap Wanita : "),
                'Nomor Akta Wanita ': input("Masukan Nomor Akta Wanita : "),
                'Surat Keterangan Lurah': input("Masukan Nomor Surat Keterangan Lurah: "),
                'NIK Pria': input("Masukan Nomor NIK Pria : "),
                'NIK Wanita': input("Masukan Nomor NIK Wanita : "),
                'Nama Saksi 1': input("Masukan Nama Saksi 1 : "),
                'Nama Saksi 2': input("Masukan Nama Saksi 2 : "),
                'NIK Saksi 1': input("Masukan Nomor NIK Saksi 1 : "),
                'NIK Saksi 2': input("Masukan Nomor NIK Saksi 2 : "),
            })
            berapaData -= 1
        print("\n")
        os.system("cls")
        print()
        print()
        print("==========================================")
        print("|         Data In Progress .... ⟳        |")
        print("==========================================")
        time.sleep(1.5)
        os.system("cls")
        print()
        print()
        print("===============================================")
        print("|         Data Has Been Recorded .... ✔       |")
        print("===============================================")
        time.sleep(1)
        clear()

    def tampilkanData():
        if dataAP.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataAP.json', 'r') as f:
                dataAp = json.load(f)
                dataAp = pd.DataFrame(dataAp)
            return print(dataAp)

    def editData():
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print("  Edit Data Pengajuan Akta Perkawinan  ")
        print("=======================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        dataAP.updateAP(index)
        print("\n")
        clear()

    def hapusData():
        clear()
        print("========================================")
        print("      MALL PELAYANAN PUBLIK JEMBER      ")
        print("  Hapus Data Pengajuan Akta Perkawinan  ")
        print("========================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        dataAP.remove(index)
        print("\n")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataAP.json', 'w') as json_file:
            json.dump(dataAP.sendJson(), json_file, indent=4)

        pilih = mainAktaP()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("==========================================")
            print("        MALL PELAYANAN PUBLIK JEMBER      ")
            print("  Tampilan Data Pengajuan Akta Perkawinan  ")
            print("==========================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            menuPengajuan()
        else:
            print("Salah memilih angka !")
def MenuKIA():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKIA():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("         Kartu Identitas Anak         ")
        print("======================================")
        print("\n")
        print("| 1. Tambah data pengajuan KIA        |")
        print("| 2. Edit data KIA                    |")
        print("| 3. Hapus data KIA                   |")
        print("| 4. Tampilkan data KIA               |")
        print("| 0. Keluar Program                  |")
        print("\n")
        print("======================================")
        pilih = int(input("Pilih Menu : "))
        return pilih

    def tambahData():
        import os,time
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print("      Tambah Pengajuan data KIA        ")
        print("=======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            dataKIA.addData(
            {
                'NIK Ayah': input("Masukan Nomor NIK Ayah : "),
                'Nama Ayah': input("Masukan Nama Lengkap Ayah : "),
                'NIK Ibu': input("Masukan Nomor NIK Ibu : "),
                'Nama Ibu': input("Masukan Nama Lengkap Ibu: "),
                'Nama Anak': input("Masukan Nama Lengkap Anak: "),
                'Nomor Akta Kelahiran': input("Masukan Nomor Akta Kelahiran : "),
                'Nomor KK': input("Masukan Nomor KK : ")
            })
            berapaData -= 1
        print("\n")
        os.system("cls")
        print()
        print()
        print("==========================================")
        print("|         Data In Progress .... ⟳        |")
        print("==========================================")
        time.sleep(1.5)
        os.system("cls")
        print()
        print()
        print("===============================================")
        print("|         Data Has Been Recorded .... ✔       |")
        print("===============================================")
        time.sleep(1)
        clear()

    def tampilkanData():
        if dataKIA.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataKIA.json', 'r') as f:
                dataKia = json.load(f)
                dataKia = pd.DataFrame(dataKia)
            return print(dataKia)

    def editData():
        clear()
        print("=======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER      ")
        print("       Edit Data Pengajuan KIA         ")
        print("=======================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        dataKIA.updateKIA(index)
        print("\n")
        clear()

    def hapusData():
        clear()
        print("========================================")
        print("      MALL PELAYANAN PUBLIK JEMBER      ")
        print("        Hapus Data Pengajuan KIA        ")
        print("========================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        dataKIA.remove(index)
        print("\n")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataKIA.json', 'w') as json_file:
            json.dump(dataKIA.sendJson(), json_file, indent=4)

        pilih = mainKIA()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("==========================================")
            print("        MALL PELAYANAN PUBLIK JEMBER      ")
            print("        Tampilan Data Pengajuan KIA       ")
            print("==========================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            menuPengajuan()
        else:
            print("Salah memilih angka !")

def menuAdmin():
    import os
    os.system("cls")
    print("======================================")
    print("     MALL PELAYANAN PUBLIK JEMBER     ")
    print("                 ADMIN                ")
    print("======================================")
    print("| 1. Lihat Daftar Antrian            |")
    print("| 2. Panggil Antrian                 |")
    print("| 3. Pengajuan Permohonan            |")
    print("| 0. Keluar Menu                     |")
    print("======================================")
        
    inputProgram = int(input("Pilih Daftar Menu : "))
    if inputProgram == 1:
        data2.lihatAntrian()
    elif inputProgram == 2:
        data2.dequeue()
    elif inputProgram == 3:
        menuPengajuan()
    elif inputProgram == 0:
        menuHome()
    else:
        print("Mohon maaf pilihan menu tidak sesuai !")
        print("Tekan enter untuk kembali ke menu")
        input()
        data2.menu()

def menuPengajuan():
    import os
    os.system("cls")
    print("======================================")
    print("     MALL PELAYANAN PUBLIK JEMBER     ")
    print("        PENGAJUAN PERMOHONANAN        ")
    print("======================================")
    print("| 1. Pembuatan KTP                   |")
    print("| 2. Pembuatan Kartu Keluarga        |")
    print("| 3. Pembuatan Akta Kelahiran        |")
    print("| 4. Pengurusan Akta Perkawinan      |")
    print("| 5. Pengurusan KIA                  |")
    print("| 0. Keluar Program                  |")
    print("======================================")
    
    inputMenu = int(input("Pilih Daftar Menu : "))
    if inputMenu == 1:
        MenuKTP()
    elif inputMenu == 2:
        MenuKK()
    elif inputMenu == 3:
        MenuAkteKelahiran()
    elif inputMenu == 4:
        MenuAktePerkawinan()
    elif inputMenu == 5:
        MenuKIA()
    elif inputMenu == 0:
        menuAdmin()
    else:
        print("Mohon maaf pilihan menu tidak ada")

def menuHome():
    from getpass import getpass
    import os,time
    os.system("cls")
    print("======================================")
    print("     MALL PELAYANAN PUBLIK JEMBER     ")
    print("======================================")
    print("| 1. Customer                        |")
    print("| 2. Admin                           |")
    print("| 0. Keluar                          |")
    print("======================================")
    inputMenu = int(input("Pilih Daftar Menu : "))
    if inputMenu == 1:
        menuCostumer()
    elif inputMenu == 2:
        inputUser = input("Masukan Username : ")
        inputPass = getpass("Masukan Password : ")
        if inputUser == "Admin" and inputPass == "Admin":
            os.system("cls")
            print()
            print()
            print("===================================")
            print("|          Waiting .... ⟳        |")
            print("===================================")
            time.sleep(1)
            menuAdmin()
        else:
            print("user dan password yang anda masukan salah")
            menuHome()
    else:
        print("Terima Kasih telah menggunakan Mall Pelayanan Publik Jember")
        exit()

menuHome()