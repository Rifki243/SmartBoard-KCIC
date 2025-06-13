import pandas as pd
import os
import random
from datetime import datetime, timedelta

# Path
csv_path = 'jadwal_kereta.csv'
dataset_path = 'Dataset'

# Daftar stasiun (boleh kamu ubah)
stasiun_list = [
    "Gambir", "Bandung", "Yogyakarta", "Surabaya", "Malang",
    "Semarang", "Purwokerto", "Solo Balapan", "Cirebon", "Blitar"
]

# Fungsi bantu: buat jadwal acak
def random_jadwal():
    hari_ini = datetime.today()
    jam_random = random.randint(5, 22)  # Antara jam 5 pagi - 10 malam
    menit_random = random.choice([0, 15, 30, 45])
    jadwal = hari_ini.replace(hour=jam_random, minute=menit_random, second=0, microsecond=0)
    return jadwal.strftime('%Y-%m-%d %H:%M')

# Load nama folder
folder_names = sorted([f for f in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, f))])
jumlah_folder = len(folder_names)

# Buat dataframe baru
data = []
for i in range(jumlah_folder):
    data.append({
        "No. Tiket": f"TKT-{str(i+1).zfill(3)}",
        "Stasiun": random.choice(stasiun_list),
        "Jadwal": random_jadwal(),
        "Peron": f"Peron {random.randint(1, 10)}",
        "Nama": folder_names[i]
    })

df_final = pd.DataFrame(data)

# Simpan ke CSV
df_final.to_csv(csv_path, index=False)
print(f"✅ Berhasil buat {jumlah_folder} data dengan info tiket, jadwal, peron, dan nama folder.")