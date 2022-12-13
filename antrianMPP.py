try:
    class node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
    class saveDataLL:
        def __init__(self):
            self.head = None
        def addBegin(self, inData):
            nodeNew = node(inData)
            nodeNew.next = self.head
            self.head = nodeNew
        def addEnd(self, inData):
            nodeNew = node(inData)
            if self.head is None:
                self.head = nodeNew
                return
            nNode = self.head
            while(nNode.next):
                nNode = nNode.next
            nNode.next= nodeNew
        def removeData(self, keyRemove):
            head = self.head
            if (head is not None):
                if (head.data == keyRemove):
                    self.head = head.next
                    head = None
                    return
            while (head is not None):
                if head.data == keyRemove:
                    break
                prev = head
                head = head.next
            if (head == None):
                return
            prev.next = head.next
            head = None
        def printLL(self):
            printvalue = self.head
            while(printvalue):
                print(printvalue.data)
                printvalue = printvalue.next
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
                self.menuCostumer()
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
            print("Terima Kasih telah menggunakan Mall Pelayanan Publik Jember")
            import sys
            sys.exit()
        def pengajuanPermohonanKK(self):
            import time
            global savePeople_data
            savePeople_data = saveDataLL()
            dataOne = input("Masukkan NIK : ")
            savePeople_data.addBegin(dataOne)
            dataTwo = input("Masukka No.KTP : ")
            savePeople_data.addEnd(dataTwo)
            dataThree = input("Masukkan Tempat, Tanggal Lahir : ")
            savePeople_data.addEnd(dataThree)
            print("======= Data telah masuk ke dalam layanan ========")
            print("====== Mohon tunggu proses permohonan anda =======")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()
        def pengajuanPermohonanKTP(self):
            global savePeople_data
            savePeople_data = saveDataLL()
            dataOne = input("Masukkan Nama Lengkap : ")
            savePeople_data.addBegin(dataOne)
            dataTwo = input("Masukka No.KK : ")
            savePeople_data.addEnd(dataTwo)
            dataThree = input("Masukka Gol. Darah : ")
            savePeople_data.addEnd(dataThree)
            dataFour = input("Masukkan Tempat, Tanggal Lahir : ")
            savePeople_data.addEnd(dataFour)
            dataFive = input("Masukkan Nomor Telepon : ")
            savePeople_data.addEnd(dataFive)
            print("======= Data telah masuk ke dalam layanan ========")
            print("====== Mohon tunggu proses permohonan anda =======")
            print("Tekan enter untuk lanjut")
            input()
            self.menu()
        def menuHome(self):
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
                self.menuCostumer()
            elif inputMenu == 2:
                inputUser = input("Masukan Username : ")
                inputPass = getpass("Masukan Password : ")
                if inputUser == "Admin" and inputPass == "Admin":
                    self.menu()
                else:
                    print("user dan password yang anda masukan salah")
                    self.menuHome()
            else:
                self.exit()

        def menuPengajuan(self):
            import os
            os.system("cls")
            print("======================================")
            print("     MALL PELAYANAN PUBLIK JEMBER     ")
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
                self.pengajuanPermohonanKTP()
            elif inputMenu == 2:
                self.pengajuanPermohonanKK()
            elif inputMenu == 3:
                pass
            elif inputMenu == 4:
                pass
            elif inputMenu == 5:
                pass
            elif inputMenu == 6:
                self.menu()
            else:
                print("Mohon maaf pilihan menu tidak ada")
        def menuCostumer(self):
            global savePeople_data
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
                self.enqueue(dataAntrian)
            else:
                self.menuHome()
        
        def menu(self):
            global savePeople_data
            import os
            os.system("cls")
            print("======================================")
            print("     MALL PELAYANAN PUBLIK JEMBER     ")
            print("                 ADMIN                ")
            print("======================================")
            print("| 1. Lihat Daftar Antrian            |")
            print("| 2. Panggil Antrian                 |")
            print("| 3. Pengajuan Permohonan            |")
            print("| 4. Data Permohonan                 |")
            print("| 5. Keluar Program                  |")
            print("======================================")
                
            inputProgram = int(input("Pilih Daftar Menu : "))
            if inputProgram == 1:
                self.lihatAntrian()
            elif inputProgram == 2:
                self.dequeue()
            elif inputProgram == 3:
                self.menuPengajuan()
            elif inputProgram == 4:
                savePeople_data.printLL()
                input()
                self.menu()
            elif inputProgram == 5:
                self.menuHome()
            else:
                print("Mohon maaf pilihan menu tidak sesuai !")
                print("Tekan enter untuk kembali ke menu")
                input()
                self.menu()
    tes = antrianQueue()
    tes.menuHome()
except ValueError:
    print("Program Not Responding")