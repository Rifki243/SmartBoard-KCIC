import numpy as np
import tensorflow as tf
import os
import cv2  # Pastikan untuk mengimpor cv2

class TFLiteModel:
    def __init__(self, model_path, label_map_path):
        # Memuat model TensorFlow Lite
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        # Mendapatkan informasi tensor input dan output
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        
        # Memuat label map
        self.label_map = np.load(label_map_path, allow_pickle=True).item()

    def predict(self, image, input_type):
        # Memproses gambar agar sesuai dengan input model
        image = cv2.resize(image, (100, 100))  # Mengubah ukuran gambar
        image = np.expand_dims(image, axis=0)  # Menambahkan dimensi batch
        image = image / 255.0  # Normalisasi

        # Melakukan prediksi
        self.interpreter.set_tensor(self.input_details[0]['index'], image)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        
        # Mendapatkan kelas dengan probabilitas tertinggi
        predicted_class = np.argmax(output_data, axis=1)[0]
        class_name = self.label_map[predicted_class]  # Mengambil nama kelas dari label map

        # Mengembalikan hasil
        return class_name, "Tiket Capture", "Jadwal Capture", "Gambar sudah diproses dari kamera."

def load_model():
    # Menentukan jalur untuk model dan label map
    model_path = os.path.join('model_tf.lite', 'model.tflite')  # Jalur model
    label_map_path = os.path.join('model_tf.lite', 'label_map.npy')  # Jalur label map
    return TFLiteModel(model_path, label_map_path)

def predict_face(image, model, input_type):
    # Menggunakan model untuk mendapatkan hasil
    name, ticket, schedule, message = model.predict(image, input_type)
    return name, ticket, schedule, message
