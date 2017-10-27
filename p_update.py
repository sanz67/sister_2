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

cur = conn.cursor()
cur.execute("UPDATE data_mahasiswa SET nama='Ajeng Shaffira Atthariq', nim='157006021', alamat='Bekais', agama='Islam', jenis_kelamin='P', tempat_lahir='Pekanbaru', tanggal_lahir='1997-10-09',foto='0xCE' WHERE nim='157006021'");

conn.commit()
print ("Data yang di-update : " + str(cur.rowcount))

print("dalam waktu %s detik" % (time.time() - mulai))

baca.bacaDB(conn)

conn.close()
