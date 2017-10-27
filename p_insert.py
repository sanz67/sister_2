import psycopg2
import time
import baca


host = input("IP Address Host: ")
print("Host yg dimasukkan : ", host)

text_file = open("Hasil.txt", "a")

try:
    conn=psycopg2.connect(dbname='kuliah', user='postgres', password='12345', host=host)
except:
    print("I am unable to connect to the database.")

mulai = time.time()

n = 0
cur = conn.cursor()
for i in range(320):
    cur.execute("INSERT INTO data_mahasiswa (nama,nim,alamat,agama,jenis_kelamin,tempat_lahir,tanggal_lahir,foto) VALUES ('Ihsan Hasanudin', 157006021, 'Cianjur', 'Islam', 'L', 'Cianjur', '1996-10-09','0xCE')");
    n = n+1

print ("Data di-insert : " + str(n))
conn.commit()

print("dalam waktu %s detik" % (time.time() - mulai))
conn.close()
