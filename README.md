# Praktikum 3

# Naifah Alya Kamilah (312510193)

## LATIHAN 1
### Tujuan

untuk menampilkan _n_ bilangan-bilangan acak yang nilainya **lebih kecil dari 0.5**. Dengan nilai _n_ diinput saat _runtime_ (program dijalankan). Program ini menggunakan kombinasi perulangan `for` dan `while`, dan fungsi `random()`.
### Alur Algoritma

1. Import Library: Program ini memuat fingsi `random()` dari pustaka random untuk memuat angka acak antara 0.0 dan 1.0.
2. Input nilai N: Pengguna diminta untuk memberikan input berupa jumlah angka acak yang akan dihasilkan (n).
3. Perulangann `for`: Untuk mengulang proses pencarian angka acak sebanyak _n_ kali.
4. Perulangan `while`: Pada setiap putaran `for`, program akan terus membuat angka acak hingga menemukan angka yang di bawah 0.5, kemudiaan saat kondisi terpenuhi (a < 0.5), angka itu akan dicetak dan pengulangan `while` akan diakhiri dengan perintah break.
5. Output: Program mencetka n angka acak yang masing-masing bernilai di bawah 0.5.

## LATIHAN 2
### Tujuan

Untuk menghitung dan menampilkan total keuntungan selama 8 bulan berdasarkan persentase laba yang berubah-ubah setiap periode, dengan menggunakan perulangan `for`, operasi aritmetika, serta pengambilan data dari list.
### Alur Algoritma
1. Inisialisasi Modal Awal: Program dimulai untuk menghitung total keuntungan selama 8 bulan dengan modal awal pengusaha adalah 100 juta rupiah yangg disimpan dalam variabel `modal awal =  100000000000`
2. Menentukan persentase laba per bulan: Daftar persentase laba tiap bulan ditentukan menggunakan list: [0, 0, 1, 1, 5, 5, 5, 3]. Angka-angka tersebut menunjukkan perubahan laba per bulan dari bulan pertama hingga bulan kedelapan.
3. Inisialisasi Total Keuntungan: Sebuah variabel `total_keuntungan` digunakan dengan nilai awal 0, yang berfungsi untuk menyimpan hasil penjumlahan seluruh keuntungan bulanan.
4. Perulangan `for`:Program menggunakan perulangan for sebanyak 8 kali (karena ada 8 bulan).
Di setiap iterasi, program:
 
   a)Mengambil persentase laba sesuai indeks bulan dari list `persentase_laba`.
  
   b)Menghitung `keuntungan_bulanan = (persentase_laba[bulan] / 100) * modal_awal`.
  
   c)Menambahkan hasilnya ke `total_keuntungan`.
  
   d)Menampilkan keuntungan setiap bulan dengan perintah `print()`.
5. Output: Setelah perulangan selesai, program menampilkan total keuntungan selama 8 bulan berdasarkan hasil penjumlahan seluruh laba bulanan.

## LATIHAN 3
### Tujuan

Untuk menciptakan simulasi operasi mesin ATM yang sederhana, yang memungkinkan pengguna untuk memeriksa saldo, menarik uang tunai, dan keluar dari sistem, dengan menggunakan loop `while`, struktur kondisi `if-elif-else`, serta penanganan kesalahan melalui `try-except` untuk memastikan bahwa input yang diberikan valid.
## Alur Algoritma
1. Inisialisasi Saldo Awal: Program menetapkan saldo awal pengguna sebesar Rp 1.000.000, yang disimpan dalam variabel `saldo`.
2. Perulangan `while True`: Diterapkan untuk menampilkan menu ATM secara berulang hingga pengguna memutuskan untuk keluar. Pada setiap iterasi, program menunjukkan menu utama yakni Cek Saldo, Tarik Tunai dan Keleuar.
3. Input Pilihan Pengguna: Program meminta pengguna untuk memilih opsi melalui fungsi `input()` dan menyimpannya dalam variabel `pilihan`.
4. Percabangan `if-elif-else`:

   * Jika `pilihan == "1"`: Program menampilkan saldo saat ini dengan format rupiah (f"Rp {saldo:,}").
   * Jika `pilihan == "2"`: Program meminta pengguna memasukkan jumlah uang yang ingin ditarik.
Menggunakan try-except untuk menangani input tidak valid.

       a) Jika jumlah ≤ 0 → tampilkan pesan error.
     
       b) ka jumlah > saldo → tampilkan “Saldo tidak mencukupi.”
     
       c) Jika valid → saldo dikurangi (saldo -= jumlah_tarik) dan hasil penarikan ditampilkan.
   
       d) Jika saldo habis → tampilkan pesan “Saldo Anda telah habis.”

   * Jika `pilihan == "3"`: Program menampilkan pesan keluar dan menghentikan perulangan dengan `break`
   * Jika input bukan 1, 2, atau 3: tampilkan pesan "Pilihan tidak valid."
5. Output: Program akan terus beroperasi dan menampilkan saldo terkini atau pesan hasil transaksi, hingga pengguna memutuskan untuk keluar.
