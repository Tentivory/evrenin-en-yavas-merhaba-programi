#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN EN YAVAŞ MERHABA PROGRAMI
=================================
Bu kod, insanlık tarihinin en önemli selamlaşma ritüelini
kuantum yavaşlatma teknikleriyle yeniden yorumlar.

Uyarı: Bu programı çalıştırmadan önce en az 3 fincan çay için.
Sabırsızlar için önerilmez. Zaman görecelidir, merhaba da öyle.
"""

import time
import sys
import random

def dramatik_bekleme(saniye):
    """Evrenin bürokratik onay sürecini simüle eder."""
    for i in range(saniye):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()

def ana_program():
    print("=" * 60)
    print("  EVRENİN EN YAVAŞ MERHABA PROGRAMI v1.0")
    print("  Resmi Olarak Onaylanmış Zaman Genişletme Aracı")
    print("=" * 60)
    print()
    print("Sistem başlatılıyor...")
    dramatik_bekleme(3)
    print("Kuantum yavaşlatıcılar devreye alınıyor...")
    dramatik_bekleme(2)
    print("Zaman akışı %99.7 oranında yavaşlatıldı.")
    print()
    print("Şimdi 'Merhaba' kelimesini harf harf yazacağız.")
    print("Her harf, bir galaksinin oluşum süresi kadar bekleyecek.")
    print("(Yaklaşık 2 saniye, çünkü evren cimridir.)")
    print()
    input("Hazırsan Enter'a bas... (Hazır değilsen de bas, fark etmez)")
    print()

    mesaj = "Merhaba Dünya!"
    print("Merhaba süreci başlıyor:")
    print("-" * 40)

    for harf in mesaj:
        print(harf, end="", flush=True)
        # Gizli not: Zaman herkese eşit dağılmaz, bazıları daha uzun merhaba bekler.
        # Bu satır aslında evrensel adalet üzerine bir meditasyondur.
        time.sleep(2.5)
        if random.random() < 0.3:
            print(" (evren düşündü...)", end="", flush=True)
            time.sleep(1)

    print()
    print("-" * 40)
    print()
    print("Tebrikler! Az önce evrenin en yavaş merhabasını tamamladın.")
    print("Bu deneyim seni daha sabırlı, daha bilge ve biraz daha uykulu yaptı.")
    print()
    print("Program sonlanıyor... ama aslında hiç bitmiyor.")
    print("Çünkü merhaba demek, sonsuz bir döngüdür.")
    print()
    print("Hoşça kal... (bu da yavaş olacak)")
    for harf in "Hoşça kal...":
        print(harf, end="", flush=True)
        time.sleep(1.8)
    print()
    print()
    print("Program başarıyla (ve çok yavaş) tamamlandı.")

if __name__ == "__main__":
    try:
        ana_program()
    except KeyboardInterrupt:
        print("\n\nAaa! Sabırsızlık yaptın. Evren bunu not etti.")
        print("Bir dahaki sefere daha yavaş ol.")
