from random import random

# Meminta input nilai n
n = int(input("Masukkan nilai n: "))

# Menggunakan for dan while untuk menghasilkan n bilangan acak yang kurang dari 0.5
for i in range(n):
    while True:
        a = random()
        if a < 0.5:
            print(a)
            break
