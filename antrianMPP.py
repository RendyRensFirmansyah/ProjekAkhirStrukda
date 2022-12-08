try:
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
        def enqueue(self,n):
            if self.antrianFull():
                print("Mohon Maaf Sementara Ini Antrian Sudah Terlalu Penuh")
                print("Silahkan Menunggu Terlebih Dahulu ! Terima Kasih.")
            else:
                self.data.append(n)
                self.sizeIn = len(self.data)
                print(n,"Telah berhasil ditambahkan ke antrian.")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()
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
            self.menu()
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
            self.menu()
        def exit(self):
            print("Anda telah keluar dari program")
            import sys
            sys.exit()
        def menu(self):
            import os
            os.system("cls")
            print("======================================")
            print("     MALL PELAYANAN PUBLIK JEMBER     ")
            print("======================================")
            print("| 1. Tambah Antrian                  |")
            print("| 2. Lihat Daftar Antrian            |")
            print("| 3. Panggil Antrian                 |")
            print("| 4. Pengajuan Permohonan            |")
            print("| 5. Keluar Program                  |")
            print("======================================")
                
            inputProgram = int(input("Pilih Daftar Menu : "))
            if inputProgram == 1:
                dataAntrian = input("Masukkan nama antrian : ")
                self.enqueue(dataAntrian)
            elif inputProgram == 2:
                self.lihatAntrian()
            elif inputProgram == 3:
                self.dequeue()
            elif inputProgram == 4:
                pass
            elif inputProgram == 5:
                self.exit()
            else:
                print("Mohon maaf pilihan menu tidak sesuai !")
                print("Tekan enter untuk kembali ke menu")
                input()
                self.menu
    tes = antrianQueue()
    tes.menu()
except ValueError:
    print("Program Not Responding")
