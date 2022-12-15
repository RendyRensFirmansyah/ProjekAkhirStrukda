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
        print("\n Data Berhasil Ditambahkan \n")
    def removeFirst(self):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        else:
            first = self.getFirst()
            self.awal = self.awal.next 
            del first
    def remove(self, index):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        elif index+1 ==1:
            self.removeFirst()
            print("\nData Berhasil Dihapus")
        else:
            prevNode = self.get(index)
            if prevNode is None:
                print("Data yang akan dihapus tidak ditemukan")
            else:
                removedNode = prevNode.next
                prevNode.next = removedNode.next
                del removedNode
                print("\nData Berhasil Dihapus")
    def sendJson(self):
        if self.isEmpty():
            return "Belum ada data"
        else:
            bantu = self.awal
            datajs = []
            while bantu is not None:
                datajs.append(bantu.info)
                bantu = bantu.next
                
            return datajs
    def update(self, index):
        nodeUpdate = self.get(index+1)
        if nodeUpdate is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            nodeUpdate.info = {
                'Nama': input("Masukan Nama                : "),
                'NIK': input("Masukan No NIK          : "),
                'No. KTP': input("Masukan Pilihan No. KTP    : "),
                'Tempat, Tanggal Lahir': (input("Masukan Tempat, Tanggal Lahir      : "))
            }
            print("\nData Berhasil Diedit")
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
        

data, data2 = LinkedList(), antrianQueue()

# Mengkonversi Data Json ke LinkedList

if os.path.exists('dataMPP.json'):
    with open('dataMPP.json', 'r') as f:
        dataKost = json.load(f)

    for i in dataKost:
        data.addData(i)

# Main Menu
def menuCostumer():
    import os
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
        menuHome()

def MenuKTP():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKtp():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("         KARTU TANDA PENDUDUK         ")
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
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("       Tambah Pengajuan data KTP      ")
        print("======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            data.addData(
            {
                    'Nama': input("Masukan Nama                : "),
                    'NIK': input("Masukan No NIK          : "),
                    'No. KTP': input("Masukan Pilihan No. KTP    : "),
                    'Tempat, Tanggal Lahir': (input("Masukan Tempat, Tanggal Lahir      : "))
            })
            berapaData -= 1
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def tampilkanData():
        if data.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataMPP.json', 'r') as f:
                dataKost = json.load(f)
                dataKost = pd.DataFrame(dataKost)
            return print(dataKost)

    def editData():
        clear()
        print("=====================================")
        print("=                Edit               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        data.update(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def hapusData():
        clear()
        print("=====================================")
        print("=               Hapus               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        data.remove(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataMPP.json', 'w') as json_file:
            json.dump(data.sendJson(), json_file, indent=4)

        pilih = mainKtp()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("=====================================")
            print("=          Tampilan Tabel           =")
            print("=      Data Anak Kost Pak Budi      =")
            print("=====================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            break
        else:
            print("Salah memilih angka !")
def MenuKK():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKtp():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("            KARTU KELUARGA            ")
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
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("       Tambah Pengajuan data KTP      ")
        print("======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            data.addData(
            {
                    'Nama': input("Masukan Nama                : "),
                    'NIK': input("Masukan No NIK          : "),
                    'No. KTP': input("Masukan Pilihan No. KTP    : "),
                    'Tempat, Tanggal Lahir': (input("Masukan Tempat, Tanggal Lahir      : "))
            })
            berapaData -= 1
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def tampilkanData():
        if data.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataMPP.json', 'r') as f:
                dataKost = json.load(f)
                dataKost = pd.DataFrame(dataKost)
            return print(dataKost)

    def editData():
        clear()
        print("=====================================")
        print("=                Edit               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        data.update(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def hapusData():
        clear()
        print("=====================================")
        print("=               Hapus               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        data.remove(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataMPP.json', 'w') as json_file:
            json.dump(data.sendJson(), json_file, indent=4)

        pilih = mainKtp()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("=====================================")
            print("=          Tampilan Tabel           =")
            print("=      Data Anak Kost Pak Budi      =")
            print("=====================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            break
        else:
            print("Salah memilih angka !")
def MenuAkteKelahiran():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKtp():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("            KARTU KELUARGA            ")
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
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("       Tambah Pengajuan data KTP      ")
        print("======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            data.addData(
            {
                    'Nama': input("Masukan Nama                : "),
                    'NIK': input("Masukan No NIK          : "),
                    'No. KTP': input("Masukan Pilihan No. KTP    : "),
                    'Tempat, Tanggal Lahir': (input("Masukan Tempat, Tanggal Lahir      : "))
            })
            berapaData -= 1
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def tampilkanData():
        if data.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataMPP.json', 'r') as f:
                dataKost = json.load(f)
                dataKost = pd.DataFrame(dataKost)
            return print(dataKost)

    def editData():
        clear()
        print("=====================================")
        print("=                Edit               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        data.update(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def hapusData():
        clear()
        print("=====================================")
        print("=               Hapus               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        data.remove(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataMPP.json', 'w') as json_file:
            json.dump(data.sendJson(), json_file, indent=4)

        pilih = mainKtp()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("=====================================")
            print("=          Tampilan Tabel           =")
            print("=      Data Anak Kost Pak Budi      =")
            print("=====================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            break
        else:
            print("Salah memilih angka !")
def MenuAktePerkawinan():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKtp():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("            KARTU KELUARGA            ")
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
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("       Tambah Pengajuan data KTP      ")
        print("======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            data.addData(
            {
                    'Nama': input("Masukan Nama                : "),
                    'NIK': input("Masukan No NIK          : "),
                    'No. KTP': input("Masukan Pilihan No. KTP    : "),
                    'Tempat, Tanggal Lahir': (input("Masukan Tempat, Tanggal Lahir      : "))
            })
            berapaData -= 1
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def tampilkanData():
        if data.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataMPP.json', 'r') as f:
                dataKost = json.load(f)
                dataKost = pd.DataFrame(dataKost)
            return print(dataKost)

    def editData():
        clear()
        print("=====================================")
        print("=                Edit               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        data.update(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def hapusData():
        clear()
        print("=====================================")
        print("=               Hapus               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        data.remove(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataMPP.json', 'w') as json_file:
            json.dump(data.sendJson(), json_file, indent=4)

        pilih = mainKtp()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("=====================================")
            print("=          Tampilan Tabel           =")
            print("=      Data Anak Kost Pak Budi      =")
            print("=====================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            break
        else:
            print("Salah memilih angka !")
def MenuKIA():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def mainKtp():
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("            KARTU KELUARGA            ")
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
        clear()
        print("======================================")
        print("     MALL PELAYANAN PUBLIK JEMBER     ")
        print("       Tambah Pengajuan data KTP      ")
        print("======================================")
        print("\n")
        berapaData = int(input("Berapa Data yang akan Ditambah ? "))
        print("")
        while berapaData:
            data.addData(
            {
                    'Nama': input("Masukan Nama                : "),
                    'NIK': input("Masukan No NIK          : "),
                    'No. KTP': input("Masukan Pilihan No. KTP    : "),
                    'Tempat, Tanggal Lahir': (input("Masukan Tempat, Tanggal Lahir      : "))
            })
            berapaData -= 1
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def tampilkanData():
        if data.isEmpty():
            return print("Data Kosong")
        else:
            with open('dataMPP.json', 'r') as f:
                dataKost = json.load(f)
                dataKost = pd.DataFrame(dataKost)
            return print(dataKost)

    def editData():
        clear()
        print("=====================================")
        print("=                Edit               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        print("\n")
        data.update(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    def hapusData():
        clear()
        print("=====================================")
        print("=               Hapus               =")
        print("=      Data Anak Kost Pak Budi      =")
        print("=====================================")
        print("\n")
        tampilkanData()
        print("\n")
        index = int(input("Data Index Keberapa yang akan diedit ? "))
        data.remove(index)
        print("\n")
        input("Tekan Enter Untuk Kembali ke Menu Utama")
        clear()

    while True:

        # Convert Linkedlist To Json
        with open('dataMPP.json', 'w') as json_file:
            json.dump(data.sendJson(), json_file, indent=4)

        pilih = mainKtp()

        if pilih == 1:
            tambahData()
        elif pilih == 2:
            editData()
        elif pilih == 3:
            hapusData()
        elif pilih == 4:
            clear()
            print("=====================================")
            print("=          Tampilan Tabel           =")
            print("=      Data Anak Kost Pak Budi      =")
            print("=====================================")
            print("\n")
            tampilkanData()
            print("\n")
            input("Tekan Enter Untuk Kembali ke Menu Utama")
            clear()
        elif pilih == 0:
            break
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
    print("| 6. Keluar Program                  |")
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
    elif inputMenu == 6:
        pass
    else:
        print("Mohon maaf pilihan menu tidak ada")

def menuHome():
    from getpass import getpass
    import os
    os.system("cls")
    print("======================================")
    print("     MALL PELAYANAN PUBLIK JEMBER     ")
    print("======================================")
    print("| 1. Customer                        |")
    print("| 2. Admin                           |")
    print("| 3. Keluar                          |")
    print("======================================")
    inputMenu = int(input("Pilih Daftar Menu : "))
    if inputMenu == 1:
        # self.menuCostumer()
        menuCostumer()
    elif inputMenu == 2:
        inputUser = input("Masukan Username : ")
        inputPass = getpass("Masukan Password : ")
        if inputUser == "Admin" and inputPass == "Admin":
            menuAdmin()
        else:
            print("user dan password yang anda masukan salah")
            menuHome()
    else:
        pass

menuHome()