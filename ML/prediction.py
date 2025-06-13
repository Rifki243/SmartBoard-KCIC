import numpy as np
import cv2
import pandas as pd
import tensorflow as tf
from datetime import datetime, timedelta

# === Load TFLite model ===
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# === Load label map ===
label_map = np.load('label_map.npy', allow_pickle=True).item()
inv_label_map = {v: k for k, v in label_map.items()}

# === Load data jadwal ===
df_jadwal = pd.read_csv('jadwal_kereta.csv')

# === Inisialisasi kamera dan detektor wajah ===
cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Variabel kontrol tampilan
last_text = ""
show_once = False
last_seen_time = None
timeout_seconds = 2  # waktu jeda untuk reset tampilan

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        # Tidak ada wajah → reset setelah timeout
        if show_once and last_seen_time:
            if (datetime.now() - last_seen_time).total_seconds() > timeout_seconds:
                show_once = False
                last_text = ""
                last_seen_time = None

    for (x, y, w, h) in faces:
        wajah = gray[y:y+h, x:x+w]
        wajah = cv2.resize(wajah, (100, 100))
        wajah = wajah / 255.0
        wajah = wajah.astype(np.float32)
        wajah = np.expand_dims(wajah, axis=(0, -1))

        # Prediksi dengan model TFLite
        interpreter.set_tensor(input_details[0]['index'], wajah)
        interpreter.invoke()
        output = interpreter.get_tensor(output_details[0]['index'])

        label_id = np.argmax(output)
        confidence = np.max(output)

        nama = inv_label_map[label_id] if confidence > 0.7 else "Unknown"

        # Deteksi wajah yang valid dan belum ditampilkan
        if nama != "Unknown" and not show_once:
            info = df_jadwal[df_jadwal['Nama'] == nama]
            if not info.empty:
                jadwal_str = info.iloc[0]['Jadwal']
                jadwal_dt = datetime.strptime(jadwal_str, '%Y-%m-%d %H:%M')
                now = datetime.now()
                sisa_waktu = jadwal_dt - now
                sisa_text = "Sudah Berangkat" if sisa_waktu.total_seconds() < 0 else str(sisa_waktu).split('.')[0]

                no_tiket = info.iloc[0]['No. Tiket']
                stasiun = info.iloc[0]['Stasiun']
                peron = info.iloc[0]['Peron']

                last_text = (
                    f"Nama : {nama}\n"
                    f"No. Tiket : {no_tiket}\n"
                    f"Stasiun Tujuan : {stasiun}\n"
                    f"Jadwal : {jadwal_str}\n"
                    f"Peron : {peron}\n"
                    f"Sisa Waktu : {sisa_text}"
                )
            else:
                last_text = f"{nama} - Data Tidak Ditemukan"

            show_once = True
            last_seen_time = datetime.now()

        elif nama == "Unknown" and not show_once:
            last_text = "Unknown"
            show_once = True
            last_seen_time = datetime.now()

        # Gambar kotak wajah
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Tampilkan informasi jika tersedia
    if show_once and last_text:
        y0, dy = 30, 30
        for i, line in enumerate(last_text.split('\n')):
            y_text = y0 + i * dy
            cv2.putText(frame, line, (10, y_text), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    # Tampilkan video
    cv2.imshow("Face Recognition TFLite", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
