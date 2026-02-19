# Seashell Rarity Predictor (Image Classification)

This project uses Deep Learning (CNN) to classify seashell rarity from images.

## Project Structure
- `dataset/`: Contains subfolders for each rarity class. Place your training images here.
- `train_cnn.py`: Script to train the Convolutional Neural Network.
- `image_predictor.py`: Tkinter application to upload an image and get a prediction.
- `seashell_classifier.h5`: The saved model (generated after training).

## Setup
1. Install dependencies:
   ```bash
   pip install tensorflow pillow numpy
   ```
2. Prepare your dataset:
   Place images in `dataset/Common`, `dataset/Uncommon`, etc.
3. Train the model:
   ```bash
   python train_cnn.py
   ```
4. Run the predictor:
   ```bash
   python image_predictor.py
   ```
## 🔗 Project Link

👉 **Seashell Rarity Predictor**  
https://github.com/siddhiuk/seashell-rarity-predictor
