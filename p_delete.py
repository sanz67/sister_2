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
cur.execute("\nDELETE FROM data_mahasiswa WHERE nim='157006021'");

conn.commit()
print ("\nData yang dihapus : " + str(cur.rowcount))

print(" %s detik" % (time.time() - mulai))

baca.bacaDB(conn)

conn.close()
