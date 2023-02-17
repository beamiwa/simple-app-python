import os
import sys


os.system('cls')

sys.exit


mahasiswa = [
    {'NIM': '2201', 'Nama': 'Doraemon', 'Semester' : '3', 'Total SKS': '72', 'IPK': '3.10'},
    {'NIM': '2202', 'Nama': 'Nobita', 'Semester' : '3', 'Total SKS': '69', 'IPK': '3.00'},
    {'NIM': '2203', 'Nama': 'Shizuka', 'Semester' : '3', 'Total SKS': '69', 'IPK': '2.99'}
]

def welcome():
    print('''\n\t\t   SELAMAT DATANG\n
         DATA SISTEM INFORMASI AKADEMIK MAHASISWA
           PROGRAM STUDI BERENANG RENANG DI LAUT
    ---------------------------------------------------''')
welcome()

def menu_utama ():
    print('''
    \t\t     MENU UTAMA\n
    1. Report Data Mahasiswa
    2. Menambahkan Data Mahasiswa
    3. Mengubah Data Mahasiwa
    4. Menghapus Data Mahasiswa
    5. Exit\n''')
    Pilihan_menu = str(input('Silakan Pilih Menu Utama (1-5): '))

    if Pilihan_menu == '1':
        menu_read()
    elif Pilihan_menu == '2': 
        menu_create()
    elif Pilihan_menu == '3':
        menu_update()
    elif Pilihan_menu == '4':
        menu_delete()
    elif Pilihan_menu == '5':
        print('Goodbye Kakak')
        sys.exit()
    else:
        print('Angka yang Anda Masukkan Salah')
        menu_utama()

def menu_read():
    welcome()
    print('\n\t*****MENU INFORMASI AKADEMIK MAHASISWA*****\n')
    print('1. Report Seluruh Data')
    print('2. Report Data Tertentu')
    print('3. Kembali ke Menu Utama\n')
    pilihan_read = str(input('Masukkan Angka pilihan (1-3): '))

    if pilihan_read == '1':
        if len(mahasiswa) != 0:
            welcome()
            print('\n\t Data Informasi Akademik Seluruh Mahasiswa\n')
            print('NIM\t|Nama               \t|Semester\t|Total SKS\t|IPK')
            for i in range(len(mahasiswa)):
                print('{}\t|{}         \t|{}           \t|{}\t        |{}'.format(mahasiswa[i]['NIM'], mahasiswa[i]['Nama'],mahasiswa[i]['Semester'],mahasiswa[i]['Total SKS'], mahasiswa[i]['IPK']))
            menu_read()

        else:
            welcome()
            print('Tidak Ada Data Mahasiswa')
        menu_read()
        
    elif len(mahasiswa) == 0:
        print('Data Mahasiswa Kosong')
        menu_read()

    elif pilihan_read == '2':
        welcome()
        print('\n     Data Informasi Akademik Mahasiswa Berdasarkan NIM\n')
        if len(mahasiswa) != 0:
            nim_mahasiswa = input('Masukkan NIM: ')
            print(f'Data Mahasiswa dengan NIM {nim_mahasiswa}: ')

            data_mahasiswa = []
            for i in range(len(mahasiswa)):
                data_mahasiswa.append(mahasiswa[i]['NIM'])
            if nim_mahasiswa in data_mahasiswa:
                print(f"{data_mahasiswa.index(nim_mahasiswa) + 1}. NIM: {nim_mahasiswa}, Nama: {mahasiswa[data_mahasiswa.index(nim_mahasiswa)]['Nama']}, Semester: {mahasiswa[data_mahasiswa.index(nim_mahasiswa)]['Semester']} , Total SKS: {mahasiswa[data_mahasiswa.index(nim_mahasiswa)]['Total SKS']} , IPK: {mahasiswa[data_mahasiswa.index(nim_mahasiswa)]['IPK']}")
                menu_read()
            else:           
                print('Tidak Ada Data Mahasiswa')
            menu_read()
        elif len(mahasiswa) == 0:
            print('Data Mahasiswa Kosong')
            menu_read() 


    elif pilihan_read == '3':
        welcome()
        menu_utama()

    else:
        print('Angka yang Anda Masukkan Salah')
        menu_read()

def menu_create():
    welcome()
    print('\n**MENU MENAMBAHKAN DATA MAHASISWA**\n')
    print('1. Tambah Data Siswa')
    print('2. Kembali ke Menu Utama\n')
    pilihan_create = input('Masukkan Angka Pilihan (1-2): ')

    if pilihan_create == '1':
        while True :
            welcome()
            print('\n+++++++ Menambahkan Data Informasi Mahasiswa +++++++\n')
            Mahasiswa_baru = {}
            NIM_baru = str(input('Masukkan NIM Baru: '))
            check_NIM   = []

            if len (NIM_baru) != 4 :
                print('NIM Harus 4 Digit Angka!')

            else :
                for i in range(len(mahasiswa)):
                    if NIM_baru == mahasiswa[i]['NIM']:
                        check_NIM.append(NIM_baru)

                if len(check_NIM) == 0:
                    Mahasiswa_baru['NIM'] = NIM_baru

                    List_sisa = ['Nama', 'Semester', 'Total SKS', 'IPK']
                    for i in List_sisa :
                        Mahasiswa_baru[f'{i}'] = (input(f'Masukkan {i}: '))

                    while True :
                        save_data = str(input('Apakah Data Akan Disimpan? (y/n): ')).lower()

                        if save_data != 'y' and save_data != 'n':
                            print ('Maaf, Input yang Anda Masukkan Salah')

                        elif save_data == 'y':
                            mahasiswa.append(Mahasiswa_baru)
                            print('Data Tersimpan')
                        
                        else :
                            print ('Data Tidak Tersimpan')
                            break

                else :
                    print ('Data dengan NIM Tersebut Sudah Ada')
            break
        menu_create()

    elif pilihan_create == '2':
        menu_utama()

    else:
        print('Masukkan Angka 1 atau 2!!!!')
        menu_create()

def menu_update():
    welcome()
    print('\n+++++++ Mengubah Data Informasi Mahasiswa +++++++\n')
    print('1. Ubah Data Siswa')
    print('2. Kembali ke Menu Utama')
    pilihan_update = input('Masukkan Angka Pilihan (1-2): ')
    
    
    if pilihan_update == '1':
        if len(mahasiswa) != 0:                   
            while True:
                check_NIM3 = str(input('Masukan NIM yang Ingin Diubah: '))
                mahasiswa_baru = []
                for i in range(len(mahasiswa)):
                    mahasiswa_baru.append(mahasiswa[i]['NIM'])
                if check_NIM3 in mahasiswa_baru:
                    rubah = input('Tekan y Jika Ingin Mengubah dan n untuk Membatalkan: ').lower()
                    
                    if rubah == 'y':
                        data_update = mahasiswa_baru.index(check_NIM3)
                        # print(data_update)
                        while True:
                            ganti_kolom = str(input('Masukkan Data yang Ingin Diganti (NIM/Nama/Semester/SKS/IPK): '))
                            
                            # mengganti NIM
                            if ganti_kolom == 'NIM':
                                NIMbaru = input('Masukkan NIM baru: ')
                                if NIMbaru not in mahasiswa_baru:
                                    while True:
                                        nanya = input('Jadi Meng-update (y/n)? ').lower()
                                        if nanya == 'y':
                                            mahasiswa[data_update]['NIM'] = NIMbaru
                                            print('Data Telah Tersimpan')
                                            menu_update()

                                        elif nanya == 'n':
                                            print('Data Tidak Jadi Tersimpan')
                                            menu_update()
                                        else:
                                            print('Hanya Menerima y/n!')
                                else:
                                    print(f'NIM Dengan Nomor Tersebut Sudah Terpakai')
                                    menu_update()
                            
                            elif ganti_kolom == 'NAMA':
                                NAMAbaru = input('Masukkan Nama Mahasiswa: ')
                                while True:
                                    nanya = input('Jadi Meng-update (y/n)? ').lower()
                                    if nanya == 'y':
                                        mahasiswa[data_update]['Nama'] = NAMAbaru
                                        print('Data Telah Tersimpan')
                                        menu_update()

                                    elif nanya == 'n':
                                        print('Data Tidak Jadi Tersimpan')
                                        menu_update()

                                    else:
                                        print('Klik y/n')
                            
                            elif ganti_kolom == 'SEMESTER':
                                SEMESTERbaru = input('Masukkan Semester: ')
                                while True:
                                    nanya = input('Jadi Meng-update (y/n)? ').lower()
                                    if nanya == 'y':
                                        mahasiswa[data_update]['Semester'] = SEMESTERbaru
                                        print('Data Telah Tersimpan')
                                        menu_update()

                                    elif nanya == 'n':
                                        print('Data Tidak Jadi Tersimpan')
                                        menu_update()
                                    else:
                                        print('Hanya Menerima y/n')
                            
                            elif ganti_kolom == 'SKS':
                                SKSbaru = input('Masukkan SKS baru: ')
                                while True:
                                    nanya = input('Jadi Meng-update (y/n)? ').lower()
                                    if nanya == 'y':
                                        mahasiswa[data_update]['Total SKS'] = SKSbaru
                                        print('Data Telah Tersimpan')
                                        menu_update()

                                    elif nanya == 'n':
                                        print('Data Tidak Jadi Tersimpan')
                                        menu_update()
                                    else:
                                        print('Hanya Menerima y/n')

                            elif ganti_kolom == 'IPK':
                                IPKbaru = input('Masukkan IPK baru: ')
                                while True:
                                    nanya = input('Jadi Meng-update (y/n)? ').lower()
                                    if nanya == 'y':
                                        mahasiswa[data_update]['IPK'] = IPKbaru
                                        print('Data Telah Tersimpan')
                                        menu_update()

                                    elif nanya == 'n':
                                        print('Data Tidak Jadi tersimpan')
                                        menu_update()
                                    else:
                                        print('Hanya Menerima y/n')
                            
                            
                            else:
                                print('Hanya menerima (NIM/Nama/Semester/SKS/IPK)')

                    elif rubah == 'n':
                        print('Sistem Tidak Jadi Merubah Data')
                        menu_update()
                        
                    else:
                        print('Masukkan y/n Saja')

                elif check_NIM3 not in mahasiswa_baru:
                    print(f'NIM Dengan Nomor {check_NIM3} Tidak Tersedia')
                    menu_update()
        
        elif len(mahasiswa) == 0:
            print('Data Mahasiswa Kosong')
            menu_update()    

    elif pilihan_update == '2':
        menu_utama()
    
    else:
        print('Angka yang Anda Masukkan Salah Kak!')
        menu_update()
                
            

def menu_delete():
    print('1. Hapus Data Siswa')
    print('2. kembali ke Menu Utama')

    pilihan_delete = input('Masukkan Angka Pilihan(1-2): ')
    if pilihan_delete == '1':
        if len(mahasiswa) != 0:
            while True:
                delete = input('\nSilahkan Masukkan NIM yang Ingin Dihapus: ')
                mahasiswa_del = []
                
                for i in range(len(mahasiswa)):
                    mahasiswa_del.append(mahasiswa[i]['NIM']) 

                    if delete in mahasiswa_del:
                        hapus = input('Tekan y Untuk Menghapus dan n Untuk Membatalkan: ').lower()
                        if hapus == 'y':  
                            del mahasiswa[mahasiswa_del.index(delete)]                        
                            print(f'Data dengan NIM {delete} berhasil dihapus')
                            menu_delete()
                            break

                        elif hapus == 'n':
                            print('Data Tidak Jadi Dihapus\n')
                            menu_delete()

                        else:
                            print('Hanya Menerima y/n!')
                else:
                    print(f'\nNIM {delete} Tidak Tersedia!\n')
                    menu_delete()
        
        elif len(mahasiswa) == 0:
            print('Data Mahasiswa Kosong')
            menu_delete()

    elif pilihan_delete == '2':
        menu_utama ()

    else:
        welcome()
        print('Angkanya Salah Kak!')
        print('')
        menu_delete()
   


menu_utama()