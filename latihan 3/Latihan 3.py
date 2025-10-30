# Simulasi Mesin ATM
# Saldo awal: Rp 1.000.000
# Pengguna dapat menarik uang hingga saldo habis atau memilih keluar.

saldo = 1000000

while True:
    print("\n=== Mesin ATM ===")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Keluar")

    pilihan = input("Pilih opsi (1/2/3): ")

    if pilihan == "1":
        print(f"Saldo Anda saat ini: Rp {saldo:,}")

    elif pilihan == "2":
        try:
            jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik (Rp): "))
            if jumlah_tarik <= 0:
                print("Jumlah tarik tunai harus lebih dari 0.")
            elif jumlah_tarik > saldo:
                print("Saldo tidak mencukupi.")
            else:
                saldo -= jumlah_tarik
                print("Penarikan berhasil!")
                if saldo == 0:
                    print("Saldo Anda telah habis.")
        except ValueError:
            print("Masukkan jumlah yang valid (angka).")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan ATM!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
