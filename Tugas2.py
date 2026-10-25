class Buku:
    def __init__(self, judul, penulis, stok):
        self.judul = judul
        self.penulis = penulis
        self.stok = stok

    def pinjam(self):
        if self.stok <= 0:
            print(f"Buku '{self.judul}' sedang tidak tersedia.")
            return False
        self.stok -= 1
        print(f"Buku '{self.judul}' berhasil dipinjam. Sisa stok: {self.stok}")
        return True

    def kembalikan(self):
        self.stok += 1
        print(f"Buku '{self.judul}' dikembalikan. Stok sekarang: {self.stok}")

    def info_buku(self):
        print(f"Judul: {self.judul} | Penulis: {self.penulis} | Stok: {self.stok}")


class AnggotaPerpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_pinjam = []

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.daftar_pinjam.append(buku.judul)
            print(f"{self.nama} meminjam '{buku.judul}'.")

    def kembalikan_buku(self, buku):
        if buku.judul not in self.daftar_pinjam:
            print(f"{self.nama} tidak meminjam buku '{buku.judul}'.")
            return
        buku.kembalikan()
        self.daftar_pinjam.remove(buku.judul)
        print(f"{self.nama} mengembalikan '{buku.judul}'.")

    def info_anggota(self):
        daftar = ", ".join(self.daftar_pinjam) if self.daftar_pinjam else "Tidak ada"
        print(f"Anggota: {self.nama} | Buku dipinjam: {daftar}")


if __name__ == "__main__":
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2)
    buku2 = Buku("Bumi", "Tere Liye", 1)
    anggota1 = AnggotaPerpustakaan("Rina")

    buku1.info_buku()
    buku2.info_buku()
    anggota1.info_anggota()

    anggota1.pinjam_buku(buku1)
    anggota1.pinjam_buku(buku2)
    anggota1.pinjam_buku(buku2)

    anggota1.info_anggota()
    buku1.info_buku()
    buku2.info_buku()

    anggota1.kembalikan_buku(buku1)
    anggota1.info_anggota()
    buku1.info_buku()
