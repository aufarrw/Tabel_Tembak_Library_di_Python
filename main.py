from ctypes import *

lib = CDLL("D:\\magang\\22-26 Agustus 2022\\26 Agustus 2022\\Python\\ParabolMortar.dll")

dargs = c_double, c_double
dres = c_double

lib.parabol_asin.argtypes = dargs
lib.parabol_asin.restype = dres

c="y"
while c == "y":
    print('Masukkan jarak: ')
    a = int(input())
    if a < 100:
        print('Jarak terlalu dekat dengan mortar')
    
    elif a <= 450:
        b = 67.08204
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 0')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 800:
        b = 89.44272
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 1')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 1350:
        b = 116.18951
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 2')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 2600:
        b = 161.24516
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 3')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 3700:
        b = 192.35385
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 4')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 4700:
        b = 216.79484
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 5')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 5600:
        b = 236.643193
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 6')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 6300:
        b = 250.99801
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 7')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    elif a <= 6500:
        b = 254.95098
        print('jarak: ', a)
        print('kecepatan: ', b)
        print('isian: 8')
        print('sudut elevasi: ', lib.parabol_asin(a, b))

    else:
        print('Jarak tidak dapat tercapai')

    print('membidik lagi?(y/n) ')
    c = input()[0]
    if c == "n":
        break;
    elif c == "y":
        continue
    else:
        print(c, 'tidak terdaftar, harap input y atau n')
        while c != "y" and c != "n":
            print('membidik lagi?(y/n) ')
            input()[0]
            if c == "n":
                break;
            elif c == "y":
                continue
            else:
                print(c, 'tidak terdaftar, harap input y atau n')
                continue