from interfaces_and_base import Product, BakingProcess, DevelopmentProcess
from typing import List

# Subclass untuk Roti Manis
class RotiManis(Product, BakingProcess, DevelopmentProcess):
    def __init__(self):
        bahan_baku = {
            "Tepung terigu": 500,  # gram
            "Gula": 100,
            "Telur": 2,  # butir
            "Mentega": 100,
            "Ragi": 7,
            "Susu": 200,  # ml
            "Garam": 5
        }
        super().__init__(
            nama="Roti Manis",
            kode="RM001",
            bahan_baku=bahan_baku,
            biaya_produksi=25000,  # per batch 12 pcs
            harga_jual=3000,  # per pcs
            jumlah_pcs=12
        )
    
    def pengadonan(self) -> str:
        return "Mencampur tepung, gula, telur, dan bahan kering. Menambahkan mentega dan susu secara bertahap."
    
    def pengembangan(self) -> str:
        return "Memfermentasi adonan selama 1-2 jam hingga mengembang 2x lipat."
    
    def pemanggangan(self) -> str:
        return "Memanggang dalam oven 180°C selama 15-20 menit hingga golden brown."
    
    def simulasi_produksi(self) -> List[str]:
        return [
            f"1. Pengadonan: {self.pengadonan()}",
            f"2. Pengembangan: {self.pengembangan()}",
            f"3. Pemanggangan: {self.pemanggangan()}"
        ]

# Subclass untuk Croissant
class Croissant(Product, BakingProcess, DevelopmentProcess):
    def __init__(self):
        bahan_baku = {
            "Tepung terigu": 400,
            "Mentega": 250,
            "Susu": 150,
            "Gula": 50,
            "Ragi": 7,
            "Garam": 8,
            "Telur": 1
        }
        super().__init__(
            nama="Croissant",
            kode="CR001",
            bahan_baku=bahan_baku,
            biaya_produksi=35000,  # per batch 8 pcs
            harga_jual=5000,  # per pcs
            jumlah_pcs=8
        )
    
    def pengadonan(self) -> str:
        return "Membuat adonan dasar dan melakukan teknik laminating dengan mentega."
    
    def pengembangan(self) -> str:
        return "Proofing adonan selama 2-3 jam dengan suhu ruang, dilanjutkan chilling."
    
    def pemanggangan(self) -> str:
        return "Memanggang dalam oven 200°C selama 18-22 menit dengan steam awal."
    
    def simulasi_produksi(self) -> List[str]:
        return [
            f"1. Pengadonan: {self.pengadonan()}",
            f"2. Pengembangan: {self.pengembangan()}",
            f"3. Pemanggangan: {self.pemanggangan()}"
        ]
