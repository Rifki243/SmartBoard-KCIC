import numpy as np
import tensorflow as tf
from preprocessing import load_dataset

# Load and preprocess dataset
images, labels, label_map = load_dataset()
images = images / 255.0  # Normalize
images = images.reshape(-1, 100, 100, 1)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(100,100,1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(len(label_map), activation='softmax')
])

# Compile and train model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(images, labels, epochs=10)

# Save model and label map
model.save('model_face_tf.keras')
np.save('label_map.npy', label_map)

# Simpan model ke format SavedModel (bukan .keras)
model.save('model_face_tf')  # akan membuat folder 'model_face_tf'

# Konversi ke TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_saved_model('model_face_tf')
tflite_model = converter.convert()

# Simpan file .tflite
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)