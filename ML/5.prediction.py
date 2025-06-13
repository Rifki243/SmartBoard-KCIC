import numpy as np
import cv2
import pandas as pd
from tensorflow.keras.models import load_model

# Load model dan label map
model = load_model('model_face_tf.keras')
label_map = np.load('label_map.npy', allow_pickle=True).item()

# Load data jadwal kereta
df_jadwal = pd.read_csv('jadwal_kereta.csv')

# Kamera dan deteksi wajah
cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

inv_label_map = {v: k for k, v in label_map.items()}

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        wajah = gray[y:y+h, x:x+w]
        wajah = cv2.resize(wajah, (100, 100))
        wajah = wajah / 255.0
        wajah = wajah.reshape(1, 100, 100, 1)

        pred = model.predict(wajah, verbose=0)
        label_id = np.argmax(pred)
        confidence = np.max(pred)
        nama = inv_label_map[label_id] if confidence > 0.7 else "Unknown"

        if nama != "Unknown":
            info = df_jadwal[df_jadwal['Nama'] == nama]
            if not info.empty:
                jadwal = info.iloc[0]['Jadwal']
                peron = info.iloc[0]['Peron']
                no_tiket = info.iloc[0]['No. Tiket']
                stasiun = info.iloc[0]['Stasiun']
                text = (f"Nama : {nama}\n"
                    f"No. Tiket : {no_tiket}\n"
                    f"Stasiun Tujuan : {stasiun}\n"
                    f"Jadwal : {jadwal}\n"
                    f"Peron : {peron}\n"
                    # f"Sisa Waktu : {sisa_waktu}"
                    )
            else:
                text = f"{nama} - Data Tidak Ditemukan"
        else:
            text = "Unknown"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        y0, dy = 30, 30
        for i, line in enumerate(text.split('\n')):
            y_text = y0 + i * dy
            cv2.putText(frame, line, (10, y_text), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


    cv2.imshow("Face Recognition TensorFlow", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()