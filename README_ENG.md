# 🎯 Face Recognition Web App (FastAPI + TensorFlow Lite)

This is a **web-based face recognition system** that automatically identifies users via webcam or uploaded images. The app matches detected faces against stored user data and displays related **ticket info**, **departure schedule**, and **remaining time**.

---

## 📁 Project Folder Structure

```
face-recognition-app/
├── back-end/
│   ├── main.py
│   ├── model.py
│   ├── model.tflite
│   ├── labelmap.npy
│   ├── jadwal_kereta.csv
│   ├── haarcascadefrontalface_default.xml
│   ├── Procfile
│   └── requirements.txt
├── front-end/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── ML/
│   ├── rekam.py                 # Record new user face images
│   ├── randomize_data.py        # Shuffle dataset
│   ├── preprocessing.py         # Resize & normalize images
│   ├── training.py              # Train TensorFlow model
│   └── prediction.py            # Evaluate/predict using model
├── Topologi.jpg
└── README.md
```

---

## 🧭 System Architecture

The system is composed of two main components:

1. 🎨 **Frontend Web Interface** — Built with HTML, CSS, and JavaScript  
2. ⚙️ **Backend API (FastAPI)** — Handles face detection and prediction processes

📌 System topology illustration:

![System Topology](Topologi.jpg)

---

## 🧠 ML Model Training Pipeline (ML/)

The `ML/` directory contains the scripts for building the face recognition model step by step. Execute them in the following order:

1. **📷 rekam.py**  
   Capture face images of users via webcam and save to dataset folder.

2. **🔀 randomize_data.py**  
   Shuffle image dataset to avoid training bias.

3. **🧹 preprocessing.py**  
   Resize, normalize, and encode images for training.

4. **🧠 training.py**  
   Train a TensorFlow model and export it as `model.tflite`.

5. **🔍 prediction.py**  
   Test model performance with new input data.

> ⚠️ Important: Execute the scripts in the correct order to ensure dataset and model consistency.

---

## 🗂️ Dataset Information

The face recognition model is trained using a **combined dataset**:

1. 📦 [LFW (Labeled Faces in the Wild) Dataset](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)  
   A public dataset containing thousands of labeled face images.

2. 📸 Locally Recorded Faces via `rekam.py`  
   Custom user images captured using webcam.

🔁 The generated dataset is merged and randomized using `randomize_data.py` to form the final dataset for training.

> Ensure that dataset structure follows model input standards and has been properly **preprocessed** before training.

---

## 🚀 Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/username/face-recognition-app.git
cd face-recognition-app
```

### 2. Create a Virtual Environment

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

### 4. Start the FastAPI Backend

```bash
cd back-end
uvicorn main:app --reload
```

📡 Server runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 How to Use the App

1. Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
2. Allow webcam access when prompted  
3. Face the webcam  
4. The system will automatically recognize your face  
5. The following information will be displayed:
   - 🧑 Name
   - 🎫 Ticket Info
   - 🚆 Departure Schedule
   - ⏳ Time Remaining
   - 📢 Additional Messages

---

## ✅ Notes

- Make sure your webcam is active and browser has camera permission.
- CSV format in `jadwal_kereta.csv` should follow: Name, Ticket, Schedule.
- The `.tflite` model and `labelmap.npy` must be pre-trained.
- Run ML scripts in the `ML/` directory in the correct order for successful model creation.

---

## 📌 License

GNU General Public License v3.0 – [AidlF4jr1i / CC25-CR349]
