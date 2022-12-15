class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class saveDataLL:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
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
    def get(self, index):
        if self.isEmpty() or index<1 or index>self.size():
            return None
        else:
            helping = self.awal
            position = 1
            while position < index :
                helping = helping.next
                position = position + 1
            return helping
    def getFirst(self):
        return self.head
    def size(self):
        if self.isEmpty():
            manyNode = 0
        else:
            helping = self.head
            manyNode = 1
            while helping.next is not None:
                manyNode = manyNode + 1
                helping = helping.next
        return manyNode
    def getLast(self):
        if self.isEmpty():
            return None
        else:
            helping = self.head
            while helping.next is not None:
                helping = helping.next
            return helping
    def addData(self, dataIn):
        if self.isEmpty():
            self.addFirst(dataIn)
        else:
            nodeNew = node(dataIn)
            last = self.getLast()
            last.next = nodeNew
        print("\n Data Berhasil Ditambahkan \n")
    def removeFirst(self):
        if self.isEmpty():
            print("Penghapusan gagal karena data kosong")
        else:
            first = self.getFirst()
            self.head = self.head.next 
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
    def update(self, index):
        updateNode = self.get(index+1)
        if updateNode is None:
            print("Data yang akan diedit tidak ditemukan")
        else:
            updateNode.data = {
                'Nama': input("Masukan Nama                   : "),
                'No HP': input("Masukan Pilihan No HP          : "),
                'No HP Ortu': input("Masukan Pilihan No HP Orangtua : "),
                'Lama Kost (Bulan)': int(input("Berapa Bulan                   : ")),
                'Daerah Asal': (input("Daerah Asal                    : "))
            }
            print("\nData Berhasil Diedit")