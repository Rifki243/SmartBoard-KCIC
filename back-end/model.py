import numpy as np
import tensorflow as tf
import cv2
import pandas as pd
from datetime import datetime

class TFLiteModel:
    def __init__(self, modelpath="model.tflite", labelmappath="label_map.npy", schedulepath="jadwal_kereta.csv"):
        self.interpreter = tf.lite.Interpreter(model_path=modelpath)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.label_map = np.load(labelmappath, allow_pickle=True).item()
        self.inv_label_map = {v: k for k, v in self.label_map.items()}

        self.schedule_df = pd.read_csv(schedulepath)

    def preprocess(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            return None, None, "Wajah tidak terdeteksi."

        x, y, w, h = faces[0]
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (100, 100))
        face = face.astype(np.float32) / 255.0
        face = face.reshape(1, 100, 100, 1)
        return face, [int(x), int(y), int(w), int(h)], None

    def predict(self, image, input_type):
        input_data, box, error = self.preprocess(image)
        if error:
            return "Unknown", "-", "-", f"{input_type}: {error}", None, "-"

        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])

        predicted_class = np.argmax(output_data)
        confidence = np.max(output_data)

        if confidence < 0.7:
            return "Unknown", "-", "-", f"{input_type}: Confidence rendah ({confidence:.2f})", box, "-"

        nama = self.inv_label_map.get(predicted_class, "Unknown")
        info = self.schedule_df[self.schedule_df['Nama'] == nama]

        if not info.empty:
            row = info.iloc[0]
            ticket = row['No. Tiket']
            schedule = row['Jadwal']
            stasiun = row['Stasiun']

            # Hitung sisa waktu keberangkatan
            try:
                jadwal_waktu = datetime.strptime(schedule, "%Y-%m-%d %H:%M")
                waktu_sekarang = datetime.now()
                selisih = jadwal_waktu - waktu_sekarang

                if selisih.total_seconds() > 0:
                    jam, sisa_detik = divmod(selisih.total_seconds(), 3600)
                    menit = sisa_detik // 60
                    sisa_waktu = f"{int(jam)} jam {int(menit)} menit"
                else:
                    sisa_waktu = "Sudah berangkat"
            except:
                sisa_waktu = "Format jadwal tidak valid"

            message = (
                f"{input_type}: Nama dikenali sebagai '{nama}' "
                f"(confidence: {confidence:.2f}), Tujuan: {stasiun}"
            )
        else:
            ticket = "-"
            schedule = "-"
            message = f"{input_type}: '{nama}' dikenali, tapi data tiket tidak ditemukan."
            sisa_waktu = "-"

        return nama, ticket, schedule, message, box, sisa_waktu

def load_model():
    return TFLiteModel()

def predictface(image, model, input_type):
    return model.predict(image, input_type)
