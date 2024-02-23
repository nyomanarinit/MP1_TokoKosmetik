#-------------------------------------------------#
# NAMA          : NYOMAN ARINI TRIRAHAYU          #
# NIM           : 2309116002                      #
# KELAS         : SISTEM INFORMASI -A             #
# MATA KULIAH   : PRAKTIKUM ASD                   #
#-------------------------------------------------#

# import untuk membersihkan terminal
import os

os.system("cls")
# import untuk menampilkan data dalam bentuk tabel
from prettytable import PrettyTable

# Definisi kelas Produk untuk merepresentasikan produk kosmetik
class Produk:
    def __init__(self, kode, nama, harga, stok, kategori):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kategori = kategori

# Definisi kelas TokoKosmetik untuk manajemen produk
class TokoKosmetik:
    def __init__(self):
        # Inisialisasi dengan beberapa produk kosmetik default
        self.produk_list = [
            Produk("1", "Lipstik Merah", 50000, 20, "Bibir"),
            Produk("2", "Bedak Tabur", 75000, 15, "Wajah"),
            Produk("3", "Eyeliner Hitam", 60000, 18, "Mata"),
            Produk("4", "Blush On", 90000, 10, "Wajah"),
            Produk("5", "Maskara Waterproof", 80000, 25, "Mata"),
        ]

    # Fungsi untuk menambahkan produk baru ke dalam daftar
    def tambah_produk(self, produk):
        # Memeriksa apakah ada nilai yang kosong pada produk yang akan ditambahkan
        if any(
            value is None or str(value).strip() == ""
            for value in [
                produk.kode,
                produk.nama,
                produk.harga,
                produk.stok,
                produk.kategori,
            ]
        ):
            print("Data produk tidak lengkap. Mohon isi semua informasi.")
        elif str(produk.kode).strip() == "" or str(produk.nama).strip() == "":
            print("Kode dan Nama produk tidak boleh kosong. Mohon isi semua informasi.")
        else:
            self.produk_list.append(produk)
            print("Produk berhasil ditambahkan.")

    # Fungsi untuk menampilkan daftar produk dalam bentuk tabel menggunakan PrettyTable
    def lihat_produk(self):
        if self.produk_list:
            table = PrettyTable()
            table.field_names = ["Kode", "Nama", "Harga", "Stok", "Kategori"]
            for produk in self.produk_list:
                table.add_row(
                    [
                        produk.kode,
                        produk.nama,
                        produk.harga,
                        produk.stok,
                        produk.kategori,
                    ]
                )
            print(table)
        else:
            print("Belum ada produk dalam toko.")

    # Fungsi untuk mengupdate informasi produk berdasarkan kode produk
    def update_produk(
        self, kode, nama_baru=None, harga_baru=None, stok_baru=None, kategori_baru=None
    ):
        for produk in self.produk_list:
            if produk.kode == kode:
                # Memeriksa apakah nilai baru diberikan, jika ya, perbarui nilainya
                if nama_baru is not None:
                    produk.nama = nama_baru
                if harga_baru is not None:
                    produk.harga = harga_baru
                if stok_baru is not None:
                    produk.stok = stok_baru
                if kategori_baru is not None:
                    produk.kategori = kategori_baru

                print("Produk berhasil diperbarui.")
                return

        print("Produk dengan kode", kode, "tidak ditemukan.")

    # Fungsi untuk menghapus produk dari daftar berdasarkan kode produk
    def hapus_produk(self, kode):
        try:
            index_produk = next(
                i for i, produk in enumerate(self.produk_list) if produk.kode == kode
            )
            del self.produk_list[index_produk]
            print("Produk berhasil dihapus.")
        except StopIteration:
            print("Produk tidak ditemukan.")


# Fungsi utama program
def main():
    # Membuat objek dari kelas TokoKosmetik
    toko_kosmetik = TokoKosmetik()

    while True:
        # Menampilkan menu utama
        print("Hallo, Selamat Datang.....   ")
        print("\n===TOKO KOSMETIK ARINI'S===")
        print("+----+----------------------+")
        print("| No | Pilihan Menu         |")
        print("+----+----------------------+")
        print("| 1  | Tambah Produk        |")
        print("| 2  | Lihat Daftar Produk  |")
        print("| 3  | Update Produk        |")
        print("| 4  | Hapus Produk         |")
        print("| 0  | Keluar               |")
        print("+----+----------------------+")

        try:
            pilihan = int(
                input("Masukkan pilihan Anda: ")
            )  # Meminta pengguna memilih opsi
        except ValueError:
            print("Masukkan pilihan yang valid (angka).")
            continue

        if pilihan == 1:
            try:
                kode = input("Masukkan kode produk: ")
                nama = input("Masukkan nama produk: ")
                harga = float(input("Masukkan harga produk: "))
                stok = int(input("Masukkan stok produk: "))
                kategori = input("Masukkan kategori produk: ")
                produk = Produk(kode, nama, harga, stok, kategori)
                toko_kosmetik.tambah_produk(produk)
            except ValueError:
                print("Masukkan nilai yang valid untuk harga dan stok.")
                continue

        elif pilihan == 2:
            toko_kosmetik.lihat_produk()

        elif pilihan == 3:
            kode = input("Masukkan kode produk yang ingin diupdate: ")
            try:
                nama_baru_input = input(
                    "Masukkan nama baru produk (kosongkan jika tidak ingin diubah): "
                )
                nama_baru = (
                    float(nama_baru_input) if nama_baru_input.strip() != "" else None
                )

                harga_baru_input = input(
                    "Masukkan harga baru produk (kosongkan jika tidak ingin diubah): "
                )
                harga_baru = (
                    float(harga_baru_input) if harga_baru_input.strip() != "" else None
                )

                stok_baru_input = input(
                    "Masukkan stok baru produk (kosongkan jika tidak ingin diubah): "
                )
                stok_baru = (
                    int(stok_baru_input) if stok_baru_input.strip() != "" else None
                )

                kategori_baru_input = input(
                    "Masukkan kategori baru produk (kosongkan jika tidak ingin diubah): "
                )
                kategori_baru = (
                    int(kategori_baru_input)
                    if kategori_baru_input.strip() != ""
                    else None
                )

                toko_kosmetik.update_produk(
                    kode, nama_baru, harga_baru, stok_baru, kategori_baru
                )
            except ValueError:
                print("Masukkan nilai yang valid untuk harga dan stok.")
                continue

        elif pilihan == 4:
            kode = input("Masukkan kode produk yang ingin dihapus: ")
            toko_kosmetik.hapus_produk(kode)

        elif pilihan == 0:
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Menjalankan program
main()
