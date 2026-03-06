# NAMA  : Darren Marcello Susanto
# KELAS : 9A
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
print("Data nilai asli: ", nilai_ujian)

n = len(nilai_ujian)

for i in range(n):
    for j in range(0, n - i - 1):
        if nilai_ujian[j] < nilai_ujian[j + 1]:   
            nilai_ujian[j], nilai_ujian[j + 1] = nilai_ujian[j + 1], nilai_ujian[j]

print("Hasil urut descending:", nilai_ujian)

penerima_beasiswa = []

for i in range (3):
    penerima_beasiswa.append(nilai_ujian[i])

print("Tiga nilai tertinggi (Penerima Beasiswa):", penerima_beasiswa)

nilai_lulus = []
for nilai in nilai_ujian :
    if nilai >= 60:
        nilai_lulus.append(nilai)
print("Daftar nilai yang lulus: ", nilai_lulus)
