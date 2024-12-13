import math

def l_balok(p, l, t):
    hitung = 2 * (p*l) + (p*t) + (l*t) 
    print(f'Luas Balok Adalah {hitung}')
    
def l_kubus(sisi):
    hitung = 6 * sisi**2
    print(f'Luas Kubus Adalah {hitung}')
    
def l_tabung(r,t):
    hitung = 2 * 3.14 * r * (r + t)
    print(f'Luas Tabung Adalah {hitung}')
    
def l_prisma(a, b, c, t_segitiga, tinggi_prisma):
     # Menghitung luas alas segitiga (A = 1/2 * alas * tinggi)
    A_alas = 0.5 * a * t_segitiga
    
    # Menghitung keliling alas segitiga (P = a + b + c)
    P_alas = a + b + c
    
    hitung = 2 * A_alas + P_alas * tinggi_prisma
    print(f'Luas Prisma Adalah {hitung}')

def l_limas_segitiga(a, b, c, t_alas, s, t_limas):
    # Menghitung luas alas segitiga (A = 1/2 * alas * tinggi)
    A_alas = 0.5 * a * t_alas
    
    # Menghitung keliling alas segitiga (P = a + b + c)
    P_alas = a + b + c
    
    # Menghitung luas sisi tegak (sisi segitiga)
    L_sisi_tegak = 0.5 * P_alas * s
    
    hitung =  A_alas + L_sisi_tegak
    print(f'Luas Limas Segitiga Adalah {hitung}')