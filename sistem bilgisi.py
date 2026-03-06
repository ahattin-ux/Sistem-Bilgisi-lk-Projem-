import platform
import psutil
import socket

def bilgi_ekrani():
    bilgisayar_adi = socket.gethostname()
    isletim_sistemi = platform.system()
    surum = platform.release()
    islemci = platform.processor()
    ram_miktari = round(psutil.virtual_memory().total / (1024**3), 2)

    print("========================================")
    print("      SISTEM BILGI CANAVARI v1.0")
    print("========================================")
    print("Bilgisayar Adi  :", bilgisayar_adi)
    print("Isletim Sistemi :", isletim_sistemi, surum)
    print("Islemci         :", islemci)
    print("Toplam RAM      :", ram_miktari, "GB")
    print("========================================")
    
    input("Programi kapatmak icin Enter'a basiniz...")

if __name__ == "__main__":
    bilgi_ekrani()