with open("Hasil.txt", "r") as f:
    conf = f.readlines()

kata = "" 

for line in conf:
    words = line.split()
    print(words)
    kata = kata + str(words)

'''def getKata():
    return kata

getKata()'''