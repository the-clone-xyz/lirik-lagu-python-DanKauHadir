import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("Dan kau hadir", 0.10),
        ("Merubah segalanya", 0.21),
        ("Menjadi lebih indah", 0.21),
        ("Kau bawa cinta ku", 0.10),
        ("Setinggi angkasa", 0.10),
        ("Membuatku merasa sempurna", 0.12),
    ] 

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [1, 0.9, 0.9, 0.9, 0.9, 0.9]
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')

jalanin_lirik()