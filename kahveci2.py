import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd

kahveler = {
    "Americano": {"fiyat": 40, "adet": 0},
    "Filtre Kahve": {"fiyat": 11, "adet": 0},
    "White Chocolate Mocha": {"fiyat": 99, "adet": 0},
}

toplam_gelir = 0
orders = []

def kahve_siparisi(kahve_adi):
    global toplam_gelir, orders
    kahve = kahveler[kahve_adi]
    kahve["adet"] += 1
    toplam_gelir += kahve["fiyat"]
    orders.append({"Kahve Adı": kahve_adi, "Fiyat": kahve["fiyat"]})
    messagebox.showinfo("Sipariş Bilgisi", f"Borcunuz {kahve['fiyat']} TL'dir.")

def satis_raporu():
    rapor = "Satış Raporu:\n\n"
    for kahve_adi, bilgiler in kahveler.items():
        rapor += f"{kahve_adi}: {bilgiler['adet']} adet satıldı\n"
    rapor += f"\nToplam Gelir: {toplam_gelir} TL"
    messagebox.showinfo("Satış Raporu", rapor)

def finish_day():
    global orders
    if not orders:
        messagebox.showinfo("Bilgi", "Bugün için herhangi bir satış yapılmadı.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    if not file_path:
        return

    df = pd.DataFrame(orders)
    df.to_excel(file_path, index=False)

    total_revenue = sum(order["Fiyat"] for order in orders)
    messagebox.showinfo("Gün Sonu", f"Satışlar kaydedildi. Toplam Ciro: {total_revenue} TL")
    orders = []  # Sipariş listesini sıfırlar

pencere = tk.Tk()
pencere.title("Boran Kafe")
pencere.geometry("400x400")

baslik = tk.Label(pencere, text="Kahve Seçiniz", font=("Arial", 17))
baslik.pack(pady=10)

for kahve_adi, bilgiler in kahveler.items():
    kahve_frame = tk.Frame(pencere)
    kahve_frame.pack(pady=5)

    kahve_label = tk.Label(kahve_frame, text=f"{kahve_adi} - {bilgiler['fiyat']} TL", font=("Arial", 12))
    kahve_label.pack(side=tk.LEFT, padx=10)

    kahve_button = tk.Button(kahve_frame, text="Seç", command=lambda kahve_adi=kahve_adi: kahve_siparisi(kahve_adi))
    kahve_button.pack(side=tk.RIGHT)

rapor_button = tk.Button(pencere, text="Satış Raporu Göster", command=satis_raporu, bg="blue", fg="white")
rapor_button.pack(pady=20)

gun_sonu_button = tk.Button(pencere, text="Gün Sonu Kaydı", command=finish_day, bg="green", fg="white")
gun_sonu_button.pack(pady=10)

pencere.mainloop()
