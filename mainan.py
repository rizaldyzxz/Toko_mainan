from tabulate import tabulate

def main():
    # Kamus mainan dan harga
    mainan = {
        "1": "hotwheels",
        "2": "lego batman",
        "3": "boneka barbie",
        "4": "nerf pistol",
        "5": "nerf shotgun",
        "6": "nerf rifle",
        "7": "nerf sniper",
        "8": "set playdoh",
        "9": "tamiya rakitan",
        "10": "lego city",
        "11": "bayblade",
        "12": "pokeball",
        "13": "action fgur anya",
        "14": "bola bekel 1 set",
        "15": "kelereng 1 plastik",
        "16": "congklak",
        "17": "monopoli",
        "18": "yoyo",
        "19": "rubik",
    }
    harga = {
        "1": 55000,
        "2": 750000,
        "3": 700000,
        "4": 310000,
        "5": 500000,
        "6": 600000,
        "7": 850000,
        "8": 200000,
        "9": 450000,
        "10": 900000,
        "11": 400000,
        "12": 50000,
        "13": 100000,
        "14": 20000,
        "15": 5000,
        "16": 10000,
        "17": 25000,
        "18": 15000,
        "19": 45000,
    }

    # Menyambut pengguna
    name = input("Masukkan nama Anda: ")
    print(f"Halo {name}, selamat datang di Toko Mainan!")
    
    # Looping untuk pembelian berulang
    while True:
        # Menampilkan daftar mainan
        print("\nDaftar Mainan:")
        table = [[kode, mainan[kode], f"Rp{harga[kode]}"] for kode in mainan]
        print(tabulate(table, headers=["Kode", "Nama Mainan", "Harga"], tablefmt="grid"))

        # Meminta pilihan mainan
        pilihan_mainan = input("Masukkan kode mainan yang ingin dibeli (atau 'keluar' untuk selesai): ")

        if pilihan_mainan == "keluar":
            break

        # Validasi input kode mainan
        try:
            main_dipilih = mainan[pilihan_mainan]
        except KeyError:
            print("Maaf, kode mainan yang dimasukkan tidak valid.")
            continue

        # Menanyakan jumlah mainan
        while True:
            try:
                jumlah_mainan = int(input(f"Berapa banyak {main_dipilih} yang ingin Anda beli? "))
                break
            except ValueError:
                print("Jumlah mainan harus berupa angka. Coba lagi.")

        # Menghitung total harga
        total_harga = jumlah_mainan * harga[pilihan_mainan]

        # Menampilkan detail pembelian
        print(f"\nPembelian {name}:")
        print(f"{jumlah_mainan}x {main_dipilih} - Rp{total_harga}")

        # Menanyakan kelanjutan pembelian
        lagi = input("Apakah Anda ingin membeli lagi (ya/tidak)? ")
        if lagi != "ya":
            break

    # Pesan perpisahan
    print("\nTerima kasih telah berbelanja di Toko Mainan!")

if __name__ == "__main__":
    main()