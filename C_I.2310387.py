panjang_balok = float(input("\nMasukkan panjang balok: "))
lebar_balok = float(input("Masukkan lebar balok: "))
tinggi_balok = float(input("Masukkan tinggi balok: "))

keliling_balok = 4 * (panjang_balok + lebar_balok + tinggi_balok)
luas_balok = 2 * (panjang_balok * lebar_balok + panjang_balok * tinggi_balok + lebar_balok * tinggi_balok)
volume_balok = panjang_balok * lebar_balok * tinggi_balok

print(f"Keliling Balok = \033[92m{keliling_balok}\033[0m")
print(f"Luas Balok = \033[92m{luas_balok}\033[0m")
print(f"Volume Balok = \033[92m{volume_balok}\033[0m")