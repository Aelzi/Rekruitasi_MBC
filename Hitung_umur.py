from datetime import datetime

def hitung_umur(tanggal_lahir):
    sekarang = datetime.now()
    selisih = sekarang - tanggal_lahir
    umur_hari = selisih.days
    umur_tahun = umur_hari // 365
    umur_hari_sisa = umur_hari % 365
    umur_jam = selisih.seconds // 3600
    umur_menit = (selisih.seconds // 60) % 60
    umur_detik = selisih.seconds % 60

    return umur_tahun, umur_hari_sisa, umur_jam, umur_menit, umur_detik

print("Memasukkan tanggal lahir (contoh: 3 Januari 2000 => YYY=2000, MM=01, DD=03)")
tahun = int(input("Masukkan tahun kelahiran (format: YYYY): "))
bulan = int(input("Masukkan bulan kelahiran (format: MM): "))
hari = int(input("Masukkan hari kelahiran (format: DD): "))

tanggal_lahir = datetime(tahun, bulan, hari)
umur = hitung_umur(tanggal_lahir)

print("Umur Anda adalah:")
print(f"{umur[0]} tahun, {umur[1]} hari, {umur[2]} jam, {umur[3]} menit, {umur[4]} detik")
