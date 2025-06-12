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

