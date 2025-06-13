# 🎯 Face Recognition Web App (FastAPI + TensorFlow Lite)

Aplikasi ini adalah sistem **pengenalan wajah berbasis web** yang mengenali pengguna secara otomatis melalui webcam atau gambar yang diunggah. Aplikasi akan mencocokkan wajah yang terdeteksi dengan data pengguna, lalu menampilkan informasi **tiket**, **jadwal keberangkatan**, dan **sisa waktu** menuju keberangkatan.

---

## 📁 Struktur Folder Proyek

```
face-recognition-app/
├── back-end/
│   ├── main.py
│   ├── model.py
│   ├── model.tflite
│   ├── label_map.npy
│   ├── jadwal_kereta.csv
│   ├── haarcascadefrontalface_default.xml
│   ├── Procfile
│   └── requirements.txt
├── front-end/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── ML/
│   ├── rekam.py                 # Rekam wajah pengguna baru
│   ├── randomize_data.py        # Acak dataset wajah
│   ├── preprocessing.py         # Resize & normalisasi gambar
│   ├── training.py              # Training model TensorFlow
│   └── prediction.py            # Evaluasi/prediksi dengan model
├── Topologi.jpg
└── README.md
```

---

## 🧭 Arsitektur Sistem

Sistem ini terdiri dari dua bagian utama:

1. 🎨 **Frontend Web** — HTML, CSS, dan JavaScript untuk antarmuka pengguna  
2. ⚙️ **Backend API (FastAPI)** — Mengelola proses deteksi wajah dan prediksi

📌 Gambar topologi sistem:

![Topologi Sistem](Topologi.jpg)

---

## 🧠 Pipeline Pelatihan Model (ML/)

Direktori `ML/` berisi langkah-langkah untuk membangun model pengenalan wajah secara bertahap. Urutan eksekusi file adalah sebagai berikut:

1. **📷 rekam.py**  
   Rekam wajah pengguna menggunakan webcam dan simpan dalam folder dataset.

2. **🔀 randomize_data.py**  
   Mengacak dataset agar training tidak bias.

3. **🧹 preprocessing.py**  
   Resize, normalisasi, dan encode data gambar sebelum training.

4. **🧠 training.py**  
   Melatih model TensorFlow dan menyimpan hasilnya sebagai `model.tflite`.

5. **🔍 prediction.py**  
   Menguji performa model terhadap data baru.

> ⚠️ Penting: Jalankan script secara berurutan untuk memastikan data dan model konsisten.


---

## 🗂️ Dataset yang Digunakan

Model pengenalan wajah ini dilatih menggunakan **gabungan dua sumber dataset**:

1. 📦 [LFW (Labeled Faces in the Wild) Dataset](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)  
   Dataset publik berisi ribuan gambar wajah dari berbagai individu.

2. 📸 Dataset Lokal dari `rekam.py`  
   Gambar wajah pengguna direkam langsung melalui webcam dan disimpan sebagai data tambahan.

🔁 Dataset hasil rekaman akan digabungkan dan diacak (melalui `randomize_data.py`) untuk membentuk dataset akhir yang digunakan pada proses pelatihan.

> Pastikan struktur folder dataset mengikuti standar input model, dan telah melalui proses **preprocessing** sebelum training.


---

## 🚀 Cara Menjalankan Proyek Secara Lokal

### 1. Clone Repository

```bash
git clone https://github.com/username/face-recognition-app.git
cd face-recognition-app
```

### 2. Buat Virtual Environment

```bash
# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r back-end/requirements.txt
```

### 4. Jalankan Backend FastAPI

```bash
cd back-end
uvicorn main:app --reload 
```
atau menggunakan:
```bash
cd back-end
python .\main.py
```
📡 Server berjalan di: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 Cara Menggunakan Aplikasi

1. Buka browser dan akses: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
2. Izinkan akses kamera saat diminta  
3. Arahkan wajah ke kamera  
4. Sistem akan secara otomatis mengenali wajah  
5. Informasi berikut akan ditampilkan di bawah kamera:
   - 🧑 Nama
   - 🎫 Tiket
   - 🚆 Jadwal keberangkatan
   - ⏳ Sisa waktu
   - 📢 Pesan informasi tambahan

---

## ✅ Catatan Tambahan

- Pastikan webcam aktif dan browser memiliki izin kamera.
- Format CSV `jadwal_kereta.csv` harus sesuai (Nama, Tiket, Jadwal).
- Model `.tflite` dan `label_map.npy` harus sudah dilatih sebelumnya.
- Untuk training model, pastikan Anda menjalankan file di `ML/` secara berurutan.

---

## 📌 Lisensi

GNU General Public License v3.0 – [AidlF4jr1i / CC25-CR349]
