# 🚄 SmartBoard: Face Recognition System for KCIC High-Speed Train Boarding

This application is a **web-based face recognition system** that automatically identifies passengers through a webcam or uploaded image. The system matches the detected face with existing data to display the **ticket**, **departure schedule**, and **remaining time** before boarding.

---

## 📁 Project Folder Structure

```
face-recognition-app/
├── back-end/
│   ├── main.py
│   ├── model.py
│   ├── model.tflite
│   ├── label_map.npy
│   ├── jadwal_kereta.csv
│   ├── haarcascade_frontalface_default.xml
│   ├── Procfile
│   └── requirements.txt
├── front-end/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── ML/
│   ├── rekam.py                 # Capture new user face data
│   ├── randomize_data.py        # Shuffle face dataset
│   ├── preprocessing.py         # Resize & normalize images
│   ├── training.py              # Train TensorFlow model
│   └── prediction.py            # Evaluate/predict with the model
├── Topologi.jpg
└── README.md
```

---

## 🧭 System Architecture

The system consists of two main components:

1. 🎨 **Frontend Web** — HTML, CSS, and JavaScript for the user interface  
2. ⚙️ **Backend API (FastAPI)** — Handles face detection and identity prediction

📌 System topology image:

![System Topology](Topologi.jpg)

---

## 🧠 Model Training Pipeline (ML/)

The `ML/` directory contains steps to build the face recognition model. The steps are as follows:

1. **📷 rekam.py**  
   Capture passenger faces via webcam and store them in the dataset.

2. **🔀 randomize_data.py**  
   Shuffle the dataset to prevent training bias.

3. **🧹 preprocessing.py**  
   Resize, normalize, and encode the image data.

4. **🧠 training.py**  
   Train the TensorFlow model and save it as `model.tflite`.

5. **🔍 prediction.py**  
   Test the model’s performance on new data.

> ⚠️ Important: Execute scripts in order to ensure data and model consistency.

---

## 🗂️ Dataset Used

The model is trained using a combination of two facial image sources:

1. 📦 [LFW (Labeled Faces in the Wild) Dataset](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset)  
2. 📸 Local dataset from `rekam.py`

🔁 Datasets are merged and shuffled before training.

> Ensure the dataset folder structure matches the model input format and has been processed using `preprocessing.py`.

---

## 🚀 Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/username/face-recognition-app.git
cd face-recognition-app
```

### 2. Create Virtual Environment

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

### 4. Run FastAPI Backend

```bash
cd back-end
uvicorn main:app --reload 
```
or:

```bash
cd back-end
python .\main.py
```

📡 Server running at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 How to Use the Application

1. Open browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
2. Allow camera access when prompted  
3. Face the camera directly  
4. The system will automatically recognize the face  
5. The following information will be shown:
   - 🧑 Name
   - 🎫 Ticket
   - 🚆 Departure schedule
   - ⏳ Time remaining before boarding
   - 📢 Additional information

---

## ✅ Additional Notes

- Ensure your webcam is active and browser has camera permissions.
- The `jadwal_kereta.csv` file must follow the format (Name, Ticket, Schedule).
- Make sure `model.tflite` and `label_map.npy` are already trained and available.
- Run the files in `ML/` sequentially for best results.

---

## 📌 License

GNU General Public License v3.0 – [AidlF4jr1i / CC25-CR349]
