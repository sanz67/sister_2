import pymongo
import time
import sys
print (sys.argv)

from pymongo import MongoClient

host = input("IP Address Host: ")
print("Host yg dimasukkan : ", host)

text_file = open("Hasil.txt", "w")
text_file.write("Host_server: %s\n" % host)

c = pymongo.MongoClient(host, 27017)
kuliah = c.kuliah
mahasiswa = kuliah.data_mahasiswa

mahasiswa.delete_many({})
mulai = time.time()

for i in range(320):
    data_mahasiswa = {
            '_id' : 'ObjectId(' + str(i) + ')',
            'nama': 'Ihsan Hasanudin',
            'nim' : '157006021',
            'alamat' : 'Cianjur',
            'agama' : 'Islam',
            'jenis_kelamin' : 'L',
            'tempat_lahir' : 'Cianjur',
            'tanggal_lahir' : '1996-10-09',
            'foto' : '0xCE'
        }
    hasil = mahasiswa.insert_one(data_mahasiswa)

text_file.write("Hasil INSERT dengan MongoDB: %s detik" % (time.time() - mulai))
print("%s detik" % (time.time() - mulai))
text_file.close()
