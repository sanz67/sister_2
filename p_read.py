import psycopg2
import time

host = input("IP Address Host: ")
print("Host yg dimasukkan : ", host)
text_file = open("Hasil.txt", "a")

try:
    conn=psycopg2.connect(dbname='kuliah', user='postgres', password='12345', host=host)
except:
    print("I am unable to connect to the database.")

mulai = time.time()

cur = conn.cursor()
try:
     cur.execute("""SELECT * from data_mahasiswa""")
except:
    print("SELECT ERROR")
    rows = cur.fetchall()
    print ("\nBaris: \n")
    for row in rows:
         '''print (" ", row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])'''

conn.commit()
print("data yang dibaca : " + str(cur.rowcount))

print(" %s detik" % (time.time() - mulai))
conn.close()
