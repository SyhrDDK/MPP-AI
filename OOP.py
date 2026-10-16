class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True	
        
    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru
        
    def tembak(self):
        if self.is_active:
            self.skor += 50
            
    def info_status(self):
        status = "Aktif" if self.is_active else "Tidak Aktif"
        print(f"warna peluru: {self.warna_peluru}")
        print(f"skor: {self.skor}")
        print(f"status: {status}")

# --- UJI COBA PROGRAM ---
katak = KatakZuma("Merah")
katak.info_status()

katak.ganti_warna("Hijau")
katak.tembak()
katak.tembak()
katak.info_status()