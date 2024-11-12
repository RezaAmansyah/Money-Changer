# Money-Changer

Berikut adalah contoh deskripsi proyek untuk file README berdasarkan kode di atas:

---

# Money Currency Exchange

Johnny Money Currency Exchange adalah sebuah aplikasi sederhana untuk menukar mata uang dengan nilai tukar yang diambil secara real-time menggunakan API dari FreeCurrencyAPI. Aplikasi ini memungkinkan pengguna untuk menukar mata uang dari IDR ke berbagai mata uang lainnya (USD, EUR, CAD, TRY, THB, dan JPY) atau sebaliknya.

## Fitur Utama
- **Tukar Mata Uang**: Pengguna dapat memilih untuk menukar dari IDR ke mata uang lain atau dari mata uang lain ke IDR.
- **Sistem Voucher**: Untuk menggunakan layanan tukar mata uang, pengguna harus membeli voucher terlebih dahulu. Aplikasi akan menghasilkan kode acak yang perlu dimasukkan pengguna untuk melanjutkan transaksi.
- **Validasi Pembayaran**: Aplikasi memeriksa jumlah uang yang dimasukkan pengguna, memberikan kembali jika uang berlebih, atau meminta tambahan jika kurang.
- **Penggunaan API**: Mengambil data nilai tukar mata uang terbaru dari API FreeCurrencyAPI untuk memastikan nilai tukar yang up-to-date.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama.
- **Requests**: Mengambil data dari FreeCurrencyAPI.
- **Random**: Menghasilkan kode voucher acak.
- **String**: Membuat kode voucher.

## Cara Menggunakan
1. **Jalankan Aplikasi**: Eksekusi kode di terminal.
2. **Masukkan Nama**: Setelah nama dimasukkan, aplikasi akan menanyakan apakah Anda ingin membeli voucher.
3. **Beli Voucher**: Jika memilih untuk membeli, masukkan uang yang diminta dan Anda akan menerima kode unik.
4. **Masukkan Kode Voucher**: Setelah pembayaran selesai, masukkan kode untuk verifikasi.
5. **Pilih Layanan Tukar**: Setelah verifikasi, pilih opsi tukar mata uang yang diinginkan.
6. **Tukar Mata Uang**: Masukkan jumlah uang yang ingin ditukar, dan aplikasi akan menghitung serta menampilkan jumlah dalam mata uang yang dipilih.
7. **Kembali**: Aplikasi akan mengembalikan sisa uang jika ada.

## Daftar Mata Uang yang Didukung
- **USD** - Dolar Amerika Serikat
- **EUR** - Euro
- **CAD** - Dolar Kanada
- **IDR** - Rupiah
- **TRY** - Lira Turki
- **THB** - Baht Thailand
- **JPY** - Yen Jepang

## Contoh Kode Penggunaan API
```python
def convert_currency(base):
    currencies = ','.join(CURRENCY)
    url = f'{USER_URL}&base_currency={base}&currencies={currencies}'
    response = requests.get(url)
    data = response.json()
    return data['data']
```

## Catatan
- Nilai tukar mata uang yang diambil dari API mungkin memiliki batasan tergantung pada penggunaan dan batasan akses API.
- Pastikan Anda memiliki koneksi internet untuk mengambil data nilai tukar.

---

