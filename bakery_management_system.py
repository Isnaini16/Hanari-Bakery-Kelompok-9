from interfaces_and_base import Product, BakingProcess
from bread_products import RotiManis, Croissant
from pastry_products import ButterCookies, Muffin

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
