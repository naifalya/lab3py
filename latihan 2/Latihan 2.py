# Menghitung total keuntungan selama 8 bulan
# Modal awal: 100 juta (100.000.000)
modal_awal = 100000000

# Persentase laba per bulan 1-2: 0%, Bulan 3-4: 1%, Bulan 5-7: 5%, Bulan 8: 3%
persentase_laba = [0, 0, 1, 1, 5, 5, 5, 3]

# Inisialisasi total keuntungan
total_keuntungan = 0

# Menghitung keuntungan per bulan dan menjumlahkan
for bulan in range(8):
    keuntungan_bulanan = (persentase_laba[bulan] / 100) * modal_awal
    total_keuntungan += keuntungan_bulanan
    print(f"Bulan {bulan+1}: Keuntungan = {keuntungan_bulanan:,.0f}")

# Total keuntungan
print(f"\nTotal keuntungan selama 8 bulan: {total_keuntungan:,.0f}")