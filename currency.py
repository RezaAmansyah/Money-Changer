import requests
import random
import string

#memasukan API KEY dan URL
API_KEY = 'fca_live_MW9Uo4ch5HVSDC5SMMlKeoPzW82TBc3KuXN4XgZI'
USER_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCY = ['USD','EUR','CAD','IDR','TRY','THB','JPY']

#==========================================================================================================
def convert_currency(base):
    currencies = ','.join(CURRENCY)
    url = f'{USER_URL}&base_currency={base}&currencies={currencies}'

    try:
        response = requests.get(url)
        data = response.json()
        return data['data']

    except Exception as e:
        print('InValid Pilihan ')
        return None
#============================================================================================================
def random_string(panjang:int) -> str:
    hasil_random_string = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_random_string
#============================================================================================================
def tukar_mata_uang(): 
    '''
    Fungsi Mendapatkan nilai tukar mata uang dari user input
    Fungsi bisa dari IDR ke kurs lain atau sebaliknya
    '''
    print('='*90)
    print(f'{"Selamat Datang Di Menu Transaksi Johnny Money":^90}')
    print('='*90)
    print(f'{"Berikut Mata Uang Yang Tersedia Di Toko Kami":^90}')
    print('='*90)
    print('1. US Dollar = USD\n2. Euro = EUR\n3. Dollar Canada = CAD')
    print('4. Yen Jepang = JPY\n5. Lira Rurki = TRY\n6. Bhat Thailand = THB')
    print('='*90)
    print('Silahkan Pilih :\n1. Tukar Dari IDR\n2. Tukar Ke IDR ')
    while True:
        user_choose = input('Silahkan masukan Pilihan Anda : ')
        if user_choose == '1':
            base_currencies = 'IDR'   #dari IDR ke Kurs Lain
            tujuan_currencies = input('Silahkan Masukan Mata Uang Yang Akan di Tukar contoh(USD): ').upper()
            jumlah = input('Masukan Jumlah Uang Yang Akan Di Tukar: ')
            if jumlah.isdigit():
                jumlah = int(jumlah)
            else:
                print('Input Jumlah Tidak Valid')

            if base_currencies not in CURRENCY:
                print('Upss, Mohon Maaf Tapi Pilihan Anda Tidak Valid')

            data = convert_currency(base_currencies)

            del data[base_currencies]
            found = False
            for curr, value in data.items():
                if curr == tujuan_currencies:
                    found =True
                    print('Silahkan Ambil Uang Anda')
                    print(f'{curr} : {round((value*jumlah),3)}')
            if not found:
                print(f'Mata Uang {tujuan_currencies} Tidak Tersedia di Toko Kami')

            print('Terima Kasih Telah Menggunakan Layanan Kami')
            break

        elif user_choose == '2':   #dari kurs lain ke rupiah
            print('USD EUR CAD TRY THB JPY')
            base_currencies = input('masukan kurs yang akan anda tukar: ').upper()
            jumlah = (input('Masukan Jumlahnya Uang Yang Akan Anda Tukar: '))
            if jumlah.isdigit():
                jumlah = int(jumlah)
            else:
                print('Input Jumlah Tidak Valid')

            if base_currencies not in CURRENCY:
                print('Upss, Mohon Maaf Tapi Pilihan Anda Tidak Valid')

            data = convert_currency(base_currencies)

            del data[base_currencies]
            for curr, value in data.items():
                if curr == 'IDR':
                    print('Silahkan Ambil Uang Anda')
                    print(f"{curr} : {round((value*jumlah),4)}")
            print('Terima Kasih Telah Menggunakan Layanan Kami')
            break
        else:
            print('Pilihan Anda Tidak Valid')
            break
    

#=============================================================================================================
def main_app():
    '''
    fungsi beli voucher untuk menggunakan layanan transaksi mata uang
    '''
    try:
        while True:
            print('='*90)
            print(f'{"Selamat Datang Di Johnny Money":^90}')
            print(f'{"Jasa Tukar Mata Uang Terpercaya Sejak 1999":^90}')
            print('='*90)
            user_name = input('Silahkan Masukan Nama Anda: ').title()
            if user_name.isdigit():
                print('Nama Tidak Boleh Angka')
            else:
                print('\n')
                print(f'Hallo {user_name} Untuk Melanjutkan Transaksi Anda Harus Membeli Voucher')
            print('='*90)
            beli_voucher = input('Apakah Anda mau membeli voucher (y/n): ')
            
            if beli_voucher == 'n':
                print('ga jadi beli voucher ya')
                break
            else:
                print('Harga Vochher cuman 5000 aja :) ')
                total =  5000
                print(f'Total Harga Yang harus Anda Bayar adalah {total}')
                uang_customer = input('Silahkan Masukan Uang anda: ')
                if uang_customer.isdigit():
                    uang_customer = int(uang_customer)
                else:
                    print('Harus Angka gan ')
                    continue

                while True:
                    if uang_customer == total:
                        kode = random_string(4)
                        print(f'ini kodenya {kode}')

                        masukan_kode = input('Masukan Kode nya gan Pastikan Tidak Boleh salah: ')
                        if masukan_kode == kode:
                            print('OKe Gann')
                            break
                        else:
                            print('Kode SALAH')
                            continue

                    elif uang_customer > total:
                        kode = random_string(4)
                        print(f'ini kodenya {kode}')

                        masukan_kode = input('Masukan Kode nya gan Pastikan Tidak Boleh salah: ')
                        if masukan_kode == kode:
                            print('OKe Gann')
                            print(f'Kembaliannya nih gan {uang_customer-total}')
                            break
                        else:
                            print('Kode SALAH')
                            continue

                    elif uang_customer < total:
                        selisih = total - uang_customer
                        print(f'Wadu uang nya kurang {selisih} Gan')
                        print('Tambah Lagi Gan')
                        uang_tambah = int(input('masukan uang tambahan: '))

                        if uang_tambah == selisih:
                            kode = random_string(4)
                            print(f'ini kodenya {kode}')

                            masukan_kode = input('Masukan Kode nya gan Pastikan Tidak Boleh salah: ')
                            if masukan_kode == kode:
                                print('OKe Gann')
                                break
                            else:
                                print('Kode SALAH')
                                continue
                        elif uang_tambah > selisih:
                            kode = random_string(4)
                            print(f'ini kodenya {kode}')

                            masukan_kode = input('Masukan Kode nya gan Pastikan Tidak Boleh salah: ')
                            if masukan_kode == kode:
                                print('OKe Gann')
                                print(f'Kembaliannya : {uang_tambah - selisih}')
                                break
                            else:
                                print('Kode SALAH')
                                continue
                    else:
                        print('Tidak Valid')

                
                is_done = input('tekan 1 untuk tukar mata uang dan tombol apapun untuk membatalkan transaksi:' )
                if is_done == '1':
                    tukar_mata_uang()
                    break
                else:
                    print('Jika Anda Membatalkan Transaksi Maka Voucher akan hangus')
                    user_confirm = input('Apakah Anda Yakin Mmbatalkan Transaksi(y/n): ').lower()
                    if user_confirm == 'y':
                        print('Mohon Maaf Transaksi Di batalkan. Terimakasih Telah Menggunakan Jasa Kami')
                        break
                    else:
                        continue
    except:
        print('Input Tidak Valid')

main_app()





