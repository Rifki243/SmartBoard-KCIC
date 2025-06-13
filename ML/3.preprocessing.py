import os
import numpy as np
import cv2

def load_dataset(dataset_path='Dataset'):
    label_map = {}
    images = []
    labels = []
    label_id = 0

    for folder_name in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder_name)
        if not os.path.isdir(folder_path):
            continue

        if folder_name not in label_map:
            label_map[folder_name] = label_id
            label_id += 1

        for img_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (100, 100))
            images.append(img)
            labels.append(label_map[folder_name])  # gunakan integer label, bukan nama

    return np.array(images), np.array(labels), label_map