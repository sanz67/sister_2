import pymongo
import time
import sys
print (sys.argv)

from pymongo import MongoClient

host = input("IP Address Host: ")

text_file = open("Hasil.txt", "a")

c = pymongo.MongoClient(host, 27017)
kuliah = c.kuliah
mahasiswa = kuliah.data_mahasiswa

mulai = time.time()
hasil = mahasiswa.find({})

text_file.write("\nHasil READ dengan MongoDB: %s detik" % (time.time() - mulai))
print("%s detik" % (time.time() - mulai))
text_file.close()
