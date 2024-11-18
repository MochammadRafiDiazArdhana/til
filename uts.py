from math import floor


jumlahSemuaPesertaKuliah = int(input('masukkan jumlah semua peserta kuliah: '))
prosentaseMinimalPesertaMasuk = float(input('masukkan prosentase minimal peserta kuliah: '))
batasTerlambat = int(input('batas waktu terlambat: '))
mahasiswa = []
for x in range(jumlahSemuaPesertaKuliah):
    mewMahasiswa = int(input('masukkan waktu mhs ' +str(x+1)+' masuk: '))
    mahasiswa.append(mewMahasiswa)
mahasiswaTerlambat = 0
number = 0
for x in mahasiswa:
    if x > batasTerlambat:
        mahasiswaTerlambat = mahasiswaTerlambat+1
jumlahMinimumMhs = prosentaseMinimalPesertaMasuk
if mahasiswaTerlambat > floor(jumlahMinimumMhs):
    print('kelas batal')
else:
    print('Kelas Tidak batal')