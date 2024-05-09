def main():
    # Kamus mainan dan harga
    mainan = {
        "1": "hotwheels",
        "2": "lego batman",
        "3": "boneka barbie",
        # ... (sisanya sama)
    }
    harga = {
        "1": 55000,
        "2": 750000,
        # ... (sisanya sama)
    }

    # Menyambut pengguna
    name = input("Masukkan nama Anda: ")
    print(f"Halo {name}, selamat datang di Toko Mainan!")

    # Looping untuk pembelian berulang
    while True:
        # Menampilkan daftar mainan
        print("\nDaftar Mainan:")
        for kode, nama_mainan in mainan.items():
            print(f"{kode}. {nama_mainan} - Rp{harga[kode]}")

        # Meminta pilihan mainan
        pilihan_mainan = input("Masukkan kode mainan yang ingin dibeli (atau 'keluar' untuk selesai): ")

    #     if pilihan_mainan == "keluar":
    #         break

        # # Validasi input kode mainan
        # try:
        #     main_dipilih = mainan[pilihan_mainan]
        # except KeyError:
        #     print("Maaf, kode mainan yang dimasukkan tidak valid.")
        #     continue

        # # Menanyakan jumlah mainan
        # while True:
        #     try:
        #         jumlah_mainan = int(input(f"Berapa banyak {main_dipilih} yang ingin Anda beli? "))
        #         break
        #     except ValueError:
        #         print("Jumlah mainan harus berupa angka. Coba lagi.")

        # # Menghitung total harga
        # total_harga = jumlah_mainan * harga[pilihan_mainan]

        # # Menampilkan detail pembelian
        # print(f"\nPembelian {name}:")
        # print(f"{jumlah_mainan}x {main_dipilih} - Rp{total_harga}")

        # # Menanyakan kelanjutan pembelian
        # lagi = input("Apakah Anda ingin membeli lagi (ya/tidak)? ")
        # if lagi != "ya":
        #     break

    # Pesan perpisahan
    print("\nTerima kasih telah berbelanja di Toko Mainan!")

if __name__ == "_main_":
    main()