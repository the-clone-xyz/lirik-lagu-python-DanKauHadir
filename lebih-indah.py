import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("Tetapi satu sinar terangi jiwaku", 0.1),
        ("Saat ku melihat senyummu", 0.14),
        ("Dan kau hadir", 0.15),
        ("Merubah segalanya", 0.15),
        ("Menjadi lebih indah", 0.09),
    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [0.3, 0.2, 0.3, 0.4, 0.6]
    # Ubah judul lagu
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')


jalanin_lirik()