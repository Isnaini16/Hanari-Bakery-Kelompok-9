from abc import ABC, abstractmethod
from typing import Dict, List

# Interface untuk proses produksi standar
class BakingProcess(ABC):
    @abstractmethod
    def pengadonan(self) -> str:
        pass
    
    @abstractmethod
    def pemanggangan(self) -> str:
        pass

class DevelopmentProcess(ABC):
    @abstractmethod
    def pengembangan(self) -> str:
        pass

class ToppingProcess(ABC):
    @abstractmethod
    def topping(self) -> str:
        pass

# Abstract Superclass untuk semua produk bakery
class Product(ABC):
    def __init__(self, nama: str, kode: str, bahan_baku: Dict[str, float], 
                 biaya_produksi: float, harga_jual: float, jumlah_pcs: int):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku  # {nama_bahan: jumlah}
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual
        self.jumlah_pcs = jumlah_pcs
    
    def hitung_profit(self, jumlah_produksi: int) -> float:
        """Menghitung estimasi profit berdasarkan jumlah produksi"""
        batch_needed = jumlah_produksi / self.jumlah_pcs
        total_biaya = self.biaya_produksi * batch_needed
        total_pendapatan = self.harga_jual * jumlah_produksi
        return total_pendapatan - total_biaya
    
    def get_info(self) -> Dict:
        return {
            "nama": self.nama,
            "kode": self.kode,
            "bahan_baku": self.bahan_baku,
            "biaya_produksi": self.biaya_produksi,
            "harga_jual": self.harga_jual,
            "jumlah_pcs_per_batch": self.jumlah_pcs
        }
    
    @abstractmethod
    def simulasi_produksi(self) -> List[str]:
        pass
