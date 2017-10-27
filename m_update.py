import pymongo
import time
import sys
print (sys.argv)

from pymongo import MongoClient

host = input("IP Address Host: ")
print("Host yg dimasukkan : ", host)
text_file = open("Hasil.txt", "a")

c = pymongo.MongoClient(host, 27017)
kuliah = c.kuliah
mahasiswa = kuliah.data_mahasiswa

mulai = time.time()

data_mahasiswa = {
        'nama': 'Ajeng Shaffira Atthariq',
        'nim' : '157006005',
        'alamat' : 'Bekasi',
        'agama' : 'Islam',
        'jenis_kelamin' : 'P',
        'tempat_lahir' : 'Pekanbaru',
        'tanggal_lahir' : '1997-10-09',
        'foto' : '0xCE'
    }

hasil = mahasiswa.update_many({'nim': '157006021'}, {'$set' : data_mahasiswa})

text_file.write("\nHasil UPDATE dengan MongoDB: %s detik" % (time.time() - mulai))
print("Hasil UPDATE dengan MongoDB: %s detik" % (time.time() - mulai))
text_file.close()
