import texttable as tt
import getpass



def menu():
    print("=======================================")
    print("\n\t-----pilihan-----")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")

    pilih = input ("\n\tsilahkan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran()
    else:
        exit
    tanya()

def tanya():
    tanya = input ("\n kembali ke menu (y/t)? ")
    if tanya == "y":
        menu()
    elif tanya == "t":
        exit
    else:
        print ("\n\tsalah input.........!!!")

def nilai_mahasiswa():
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    nilai_akhir = []


    x = [[]]

    jawab = "y"

    tab = tt.Texttable()

    while (jawab == 'y'):
        nama.append(input("masukan nama: "))
        nim.append(input("masukan nim: "))
        tugas = int(input("nilai tugas: "))
        tugas = float(tugas)
        nilai_tugas.append(tugas)
        uts = int(input("nilai uts: "))
        uts = float(uts)
        nilai_uts.append(uts)
        uas = int(input("nilai uas: "))
        uas = float(uas)
        nilai_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        nilai_akhir.append(hasil)
        jawab = input("tambah data [y/t]? ")

    for i in nama:
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],nilai_tugas[idx],nilai_uts[idx],nilai_uas[idx],nilai_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['1','1','1','r','r','r','r'])
    tab.header(['no','nama','nim','nilai tugas','nilai uts','nilai uas','nilai akhir'])
    print (tab.draw())

def pembayaran () :
    print ("\n=========================================================")
    nama = input ("\nmasukan nama : ")
    nim = input ("\nmasukan NIM : ")
    semester = input ("\nmasukan semester :")
    print ("\n\t-----pilihan pembayaran-----")
    print ("\t1. pembayaran spp")
    print ("\t2. pembayaran uts")
    print ("\t3.pembayaran uas")
    print ("\t4.pembayaran spp & uts")
    print ("\t5.pembayaran spp & uas")
    pilih = input ("\n\tsilahkan pilih : ")
    if pilih == "1" :
        spp()
    elif pilih == "2" :
        uts()
    elif pilih == "3" :
        uas()
    elif pilih == "4" :
        spp_uts()
    elif pilih == "5" :
        spp_uas()
    else:
        exit
        tanya ()
def spp () :
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 5000000 * bulan
    print ("========================================")
    print ("\tottal yang harus dibayar Rp.5000000 * ",bulan," = Rp. ",total)


def uas () :
    matkul_uas = int(input("\n\tjumlah mata kuliah = "))
    matkul_uas = float(matkul_uas)
    total = 500000 * matkul_uas
    print ("========================================")
    print ("\ttotal yang harus di bayar Rp.5000000 * ",matkul_uas," = Rp. ",total)

def uts () :
    matkul_uts = int(input("\n\tjumlah mata kuliah ="))
    matkul_uts = float(matkul_uts)
    total = 5000000 * matkul_uts
    print ("========================================")
    print ("\ttotal yang harus di bayar Rp.5000000 * ",matkul_uts," = Rp. ",total)

def  spp_uas():
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    matkul  = int(input("\n\jumlah mata kuliah = "))
    matkul = float(matkul)
    bulan = float(bulan)
    total_spp = 5000000 * bulan
    bayar_uas = 500000 * matkul
    total = total_spp + bayar_uas + 5000
    print ("\ttotal bayar spp Rp. 5000000 * ",bulan," = Rp. ",total_spp)
    print ("\ttotal bayar uas Rp. 500000 * ",matkul," = Rp. ",bayar_uas)
    print ("\tbiaya tambahan server sebesar Rp. 5000")
    print ("=======================================")
    print ("\ttotal yang harus di bayar", total)

def spp_uts() :
    bulan = int(input("\n\tjumlah bulan yang di bayar = "))
    matkul  = int(input("\n\jumlah mata kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 5000000 * bulan
    bayar_uts = 500000 * matkul
    total = total_spp + bayar_uts + 5000
    print ("\ttotal bayar spp Rp. 5000000 * ",bulan," = Rp. ",total_spp)
    print ("\ttotal bayar uas Rp. 500000 * ",matkul," = Rp. ",bayar_uts)
    print ("\tbiaya tambahan server sebesar Rp. 5000")
    print ("=======================================")
    print ("\ttotal yang harus di bayar", total)

username = input("\nUsername : ")
password = getpass.getpass()
print ("===========================================")

if username == "biyant" and password == "12345678910" :
    menu()

else :
    print ("MAAF PASSWORD ATAU USERNAME SALAH...!!!")
  
