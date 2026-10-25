class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} mulai berlari di rel kereta!")

    def ambil_koin(self, jumlah):
        if jumlah <= 0:
            print("Jumlah koin harus lebih dari 0.")
            return
        self.koin += jumlah
        self.skor += jumlah * 10
        print(f"{self.nama} mengambil {jumlah} koin. Total koin: {self.koin}")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"{self.nama} menabrak rintangan. Game over!")

    def info_player(self):
        status = "Berlari" if self.is_running else "Berhenti"
        print(
            f"Nama: {self.nama} | Skor: {self.skor} | "
            f"Koin: {self.koin} | Status: {status}"
        )


if __name__ == "__main__":
    player1 = KarakterSurfer("Jake")
    player1.info_player()
    player1.berlari()
    player1.ambil_koin(5)
    player1.ambil_koin(3)
    player1.info_player()
    player1.tabrak_rintangan()
    player1.info_player()
