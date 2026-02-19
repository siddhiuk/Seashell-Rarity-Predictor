import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import os

# Load the trained model
try:
    model = tf.keras.models.load_model('seashell_classifier.h5')
    class_names = ['Common', 'Rare', 'Uncommon', 'Very_Rare'] # Matches folder names
except:
    messagebox.showerror("Error", "Model 'seashell_classifier.h5' not found. Please run train_cnn.py first.")
    exit()

def predict_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    
    if not file_path:
        return

    try:
        # Load and display image
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_display = ImageTk.PhotoImage(img)
        panel.configure(image=img_display)
        panel.image = img_display

        # Prepare image for model
        img_ready = img.resize((150, 150))
        img_array = tf.keras.utils.img_to_array(img_ready)
        img_array = tf.expand_dims(img_array, 0) # Create a batch

        # Predict
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        result_label = class_names[np.argmax(score)]
        confidence = 100 * np.max(score)

        label_result.config(text=f"Prediction: {result_label}\nConfidence: {confidence:.2f}%")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process image: {e}")

# Setup GUI
root = tk.Tk()
root.title("Seashell Image Classifier")
root.geometry("500x600")

tk.Label(root, text="Seashell Rarity Predictor (Image)", font=("Arial", 16, "bold")).pack(pady=20)

btn_upload = tk.Button(root, text="Upload Seashell Image", command=predict_image, bg="#2196F3", fg="white", font=("Arial", 12))
btn_upload.pack(pady=10)

panel = tk.Label(root) # To display the uploaded image
panel.pack(pady=20)

label_result = tk.Label(root, text="Prediction: None", font=("Arial", 14))
label_result.pack(pady=20)

root.mainloop()
