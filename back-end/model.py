# import cv2
# import numpy as np

# def load_model():
#     # Muat model pre-trained Anda di sini
#     # Contoh: model = cv2.face.LBPHFaceRecognizer_create()
#     return model

# def predict_face(image, model):
#     # Deteksi wajah dan kembalikan nama, tiket, dan jadwal
#     # Misal:
#     # return "Nama Penumpang", "Nomor Tiket", "Jadwal Keberangkatan"
#     return "John Doe", "12345", "2025-06-03 12:00"

"""
dummy model
"""

import numpy as np

class DummyModel:
    def predict(self, image, input_type):
        # Menentukan output berdasarkan jenis input
        if input_type == "upload":
            # Jika gambar diupload
            return "Nama Upload", "Tiket Upload", "Jadwal Upload", "Gambar sudah diproses dari upload."
        elif input_type == "capture":
            # Jika gambar diambil dari kamera
            return "Nama Capture", "Tiket Capture", "Jadwal Capture", "Gambar sudah diproses dari kamera."
        else:
            return None, None, None, "Jenis input tidak dikenali."

def load_model():
    # Mengembalikan instance dari DummyModel
    return DummyModel()

def predict_face(image, model, input_type):
    # Menggunakan model dummy untuk mendapatkan hasil
    name, ticket, schedule, message = model.predict(image, input_type)
    return name, ticket, schedule, message

