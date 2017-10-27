
def bacaDB(conn):
    cur = conn.cursor()
    try:
        cur.execute("""SELECT * from data_mahasiswa""")
    except:
        print("SELECT ERROR")
    rows = cur.fetchall()
    print ("\nBaris: \n")
    for row in rows:
        print (" ", row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
