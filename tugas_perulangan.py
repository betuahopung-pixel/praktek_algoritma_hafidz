berapa = int(input("Masukkan Jumlah Mahasiswa :"))

if berapa >= 5 and berapa <= 10:
    
    nilai = 0
    
    for n in range(berapa):
        nilai_inpt = int(input("Masukkan Nilai Mahasiswa :"))
        nilai = nilai + nilai_inpt
        
    hasil = nilai / berapa
    print("nilai rata-ratanya : ", hasil)

    if hasil >= 90:
        ket = "A"
    elif hasil >= 80:
        ket = "B"
    elif hasil >= 70:
        ket = "C"
    else:
        ket = "D"
        
    print(ket)