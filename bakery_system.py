from abc import ABC, abstractmethod
from typing import Dict, List
import json

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

# Sistem Manajemen Bakery
class BakeryManagementSystem:
    def __init__(self):
        self.products = {
            "1": RotiManis(),
            "2": Croissant(),
            "3": ButterCookies(),
            "4": Muffin()
        }
        self.custom_products = {}
    
    def tambah_produk_baru(self):
        print("\n=== TAMBAH PRODUK BARU ===")
        nama = input("Nama produk: ")
        kode = input("Kode produk: ")
        
        print("Masukkan bahan baku (ketik 'selesai' untuk mengakhiri):")
        bahan_baku = {}
        while True:
            nama_bahan = input("Nama bahan: ")
            if nama_bahan.lower() == 'selesai':
                break
            jumlah = float(input(f"Jumlah {nama_bahan}: "))
            bahan_baku[nama_bahan] = jumlah
        
        biaya = float(input("Biaya produksi per batch: "))
        harga = float(input("Harga jual per pcs: "))
        jumlah_pcs = int(input("Jumlah pcs per batch: "))
        
        # Membuat custom product class
        class CustomProduct(Product, BakingProcess):
            def __init__(self):
                super().__init__(nama, kode, bahan_baku, biaya, harga, jumlah_pcs)
            
            def pengadonan(self):
                return "Proses pengadonan standar untuk produk custom."
            
            def pemanggangan(self):
                return "Proses pemanggangan standar untuk produk custom."
            
            def simulasi_produksi(self):
                return [
                    f"1. Pengadonan: {self.pengadonan()}",
                    f"2. Pemanggangan: {self.pemanggangan()}"
                ]
        
        new_id = str(len(self.products) + len(self.custom_products) + 1)
        self.custom_products[new_id] = CustomProduct()
        print(f"Produk {nama} berhasil ditambahkan dengan ID: {new_id}")
    
    def tampilkan_semua_produk(self):
        print("\n=== DAFTAR SEMUA PRODUK ===")
        all_products = {**self.products, **self.custom_products}
        
        for id_produk, produk in all_products.items():
            info = produk.get_info()
            print(f"\nID: {id_produk}")
            print(f"Nama: {info['nama']}")
            print(f"Kode: {info['kode']}")
            print(f"Bahan Baku: {info['bahan_baku']}")
            print(f"Biaya Produksi: Rp {info['biaya_produksi']:,}")
            print(f"Harga Jual: Rp {info['harga_jual']:,}")
            print(f"Jumlah per Batch: {info['jumlah_pcs_per_batch']} pcs")
            print("-" * 50)
    
    def kalkulator_profit(self):
        print("\n=== KALKULATOR ESTIMASI PROFIT ===")
        self.tampilkan_daftar_produk()
        
        pilihan = input("Pilih ID produk: ")
        all_products = {**self.products, **self.custom_products}
        
        if pilihan in all_products:
            produk = all_products[pilihan]
            jumlah = int(input("Masukkan jumlah pcs yang akan diproduksi: "))
            
            profit = produk.hitung_profit(jumlah)
            batch_needed = jumlah / produk.jumlah_pcs
            total_biaya = produk.biaya_produksi * batch_needed
            total_pendapatan = produk.harga_jual * jumlah
            
            print(f"\n=== HASIL KALKULASI ===")
            print(f"Produk: {produk.nama}")
            print(f"Jumlah produksi: {jumlah} pcs")
            print(f"Batch yang dibutuhkan: {batch_needed:.2f}")
            print(f"Total biaya produksi: Rp {total_biaya:,.2f}")
            print(f"Total pendapatan: Rp {total_pendapatan:,.2f}")
            print(f"Estimasi profit: Rp {profit:,.2f}")
        else:
            print("ID produk tidak valid!")
    
    def simulasi_proses_produksi(self):
        print("\n=== SIMULASI PROSES PRODUKSI ===")
        self.tampilkan_daftar_produk()
        
        pilihan = input("Pilih ID produk: ")
        all_products = {**self.products, **self.custom_products}
        
        if pilihan in all_products:
            produk = all_products[pilihan]
            print(f"\nSimulasi produksi untuk: {produk.nama}")
            print("=" * 40)
            
            proses = produk.simulasi_produksi()
            for step in proses:
                print(step)
        else:
            print("ID produk tidak valid!")
    
    def tampilkan_daftar_produk(self):
        print("\nDaftar Produk:")
        all_products = {**self.products, **self.custom_products}
        for id_produk, produk in all_products.items():
            print(f"{id_produk}. {produk.nama}")
    
    def run(self):
        while True:
            print("\n" + "="*50)
            print("SISTEM INFORMASI HANARI BAKERY")
            print("="*50)
            print("1. Tambah produk baru")
            print("2. Tampilkan semua produk")
            print("3. Kalkulator estimasi profit")
            print("4. Simulasi proses produksi")
            print("5. Keluar")
            
            pilihan = input("\nPilih menu (1-5): ")
            
            if pilihan == "1":
                self.tambah_produk_baru()
            elif pilihan == "2":
                self.tampilkan_semua_produk()
            elif pilihan == "3":
                self.kalkulator_profit()
            elif pilihan == "4":
                self.simulasi_proses_produksi()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan sistem Hanari Bakery!")
                break
            else:
                print("Pilihan tidak valid!")

# Menjalankan sistem
if __name__ == "__main__":
    sistem = BakeryManagementSystem()
    sistem.run()
