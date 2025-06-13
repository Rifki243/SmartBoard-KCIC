import cv2
import os

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

nama = input("Masukkan Nama/ID: ")
save_path = f'Dataset/{nama}'

if not os.path.exists(save_path):
    os.makedirs(save_path)

count = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("Gagal membuka kamera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        wajah = gray[y:y+h, x:x+w]
        wajah = cv2.resize(wajah, (100, 100))
        cv2.imwrite(f"{save_path}/{count}.jpg", wajah)
        count += 1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Tambahkan info jumlah gambar
        cv2.putText(frame, f'Images: {count}/50', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Stop jika sudah 50
        if count >= 50:
            break

    cv2.imshow('Perekaman Wajah', frame)

    if cv2.waitKey(1) == ord('q') or count >= 50:
        break

cam.release()
cv2.destroyAllWindows()