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
 
  a)Mengambil persentase laba sesuai indeks bulan dari list persentase_laba.
  b)Menghitung keuntungan_bulanan = (persentase_laba[bulan] / 100) * modal_awal.
  c)Menambahkan hasilnya ke total_keuntungan.
  d)Menampilkan keuntungan setiap bulan dengan perintah print().
5. Output: Setelah perulangan selesai, program menampilkan total keuntungan selama 8 bulan berdasarkan hasil penjumlahan seluruh laba bulanan.



