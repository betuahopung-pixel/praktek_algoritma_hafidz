
print("    PROGRAM KELULUSAN MAHASISWA")
print("====================================")

# Data target nilai mahasiswa
target_nilai = {
    "andi": 70,
    "budi": 75,
    "citra": 80
}

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa (Andi/Budi/Citra): ").lower()

# Mengecek nama mahasiswa
if nama in target_nilai:

    target = target_nilai[nama]

    print("\nNama mahasiswa :", nama.capitalize())
    print("Target nilai   :", target)

    percobaan = 1
    lulus = False

    # Perulangan maksimal 3 kali
    while percobaan <= 3:

        print("\nPercobaan ke-", percobaan)

        nilai = int(input("Masukkan nilai ujian: "))

        # Mengecek nilai dengan target
        if nilai >= target:
            print("Selamat! Nilai Anda mencapai target.")
            lulus = True
            break
        else:
            print("Nilai belum mencapai target.")
            print("Silakan mengikuti remedial.")

        percobaan += 1

    # Menampilkan hasil akhir
    print("\n====================================")

    if lulus:
        print(nama.capitalize(), "berhasil lulus!")
        print("Jumlah percobaan:", percobaan)
    else:
        print(nama.capitalize(), "dinyatakan TIDAK LULUS.")
        print("Sudah mengikuti 3 kali percobaan.")

    print("====================================")

else:
    print("Nama mahasiswa tidak ditemukan!")
    print("Silakan masukkan Andi, Budi, atau Citra.")

