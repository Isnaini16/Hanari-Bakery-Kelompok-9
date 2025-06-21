from interfaces_and_base import Product, BakingProcess, DevelopmentProcess, ToppingProcess
from typing import List

# Subclass untuk Butter Cookies
class ButterCookies(Product, BakingProcess, ToppingProcess):
    def __init__(self):
        bahan_baku = {
            "Tepung terigu": 300,
            "Mentega": 200,
            "Gula halus": 100,
            "Telur": 1,
            "Vanilla": 5,  # ml
            "Garam": 2
        }
        super().__init__(
            nama="Butter Cookies",
            kode="BC001",
            bahan_baku=bahan_baku,
            biaya_produksi=20000,  # per batch 24 pcs
            harga_jual=1500,  # per pcs
            jumlah_pcs=24
        )
    
    def pengadonan(self) -> str:
        return "Mengocok mentega dan gula hingga pucat, menambahkan telur dan tepung."
    
    def pemanggangan(self) -> str:
        return "Memanggang dalam oven 160°C selama 12-15 menit hingga tepi kecoklatan."
    
    def topping(self) -> str:
        return "Menambahkan taburan gula halus atau coklat chip sebelum dipanggang."
    
    def simulasi_produksi(self) -> List[str]:
        return [
            f"1. Pengadonan: {self.pengadonan()}",
            f"2. Topping: {self.topping()}",
            f"3. Pemanggangan: {self.pemanggangan()}"
        ]

# Subclass untuk Muffin
class Muffin(Product, BakingProcess, DevelopmentProcess, ToppingProcess):
    def __init__(self):
        bahan_baku = {
            "Tepung terigu": 250,
            "Gula": 150,
            "Telur": 2,
            "Minyak": 80,  # ml
            "Susu": 180,  # ml
            "Baking powder": 10,
            "Blueberry": 100
        }
        super().__init__(
            nama="Muffin",
            kode="MF001",
            bahan_baku=bahan_baku,
            biaya_produksi=18000,  # per batch 12 pcs
            harga_jual=2500,  # per pcs
            jumlah_pcs=12
        )
    
    def pengadonan(self) -> str:
        return "Mencampur bahan kering dan basah secara terpisah, lalu digabung dengan teknik folding."
    
    def pengembangan(self) -> str:
        return "Membiarkan adonan rest selama 10-15 menit untuk hidrasi tepung."
    
    def pemanggangan(self) -> str:
        return "Memanggang dalam oven 180°C selama 18-22 menit hingga golden brown."
    
    def topping(self) -> str:
        return "Menambahkan blueberry dan streusel topping sebelum dipanggang."
    
    def simulasi_produksi(self) -> List[str]:
        return [
            f"1. Pengadonan: {self.pengadonan()}",
            f"2. Pengembangan: {self.pengembangan()}",
            f"3. Topping: {self.topping()}",
            f"4. Pemanggangan: {self.pemanggangan()}"
        ]
