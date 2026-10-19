nilaitugas =int(input("masukkan nilai Tugas : "))
uts = int(input("masukkan nilai UTS : "))
uas = int(input("masukkan nilai UAS : "))
kehadiranmahasiswa = int(input("masukkan nilai kehadiran : "))

nilai_akhir = (20 / 100 * nilaitugas) + (30 / 100 * uts) + (50 / 100 * uas)


print("======HASIL======")
print("Nilai akhir =", nilai_akhir)
print (kehadiranmahasiswa,"%")

if nilai_akhir >= 75 and kehadiranmahasiswa >= 85:

    if nilai_akhir >= 85 and kehadiranmahasiswa >= 90 and nilai_akhir % 2 == 0:
        print("Status      : Lulus Dengan Predikat")
    elif nilai_akhir >= 75 and kehadiranmahasiswa >= 80:
        print("Status      : Lulus")
else:
    print("Status      : Belum Lulus")