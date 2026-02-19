import tensorflow as tf
from tensorflow.keras import layers, models
import os

# This is a template for training. 
# In a real scenario, you've need hundreds of images per category in the 'dataset' folder.

def train_model():
    data_dir = 'dataset'
    img_height, img_width = 150, 150
    batch_size = 32

    # Load images from directory
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    )

    class_names = train_ds.class_names
    print(f"Classes found: {class_names}")

    # Build a simple CNN
    model = models.Sequential([
        layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(128, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(len(class_names), activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    # Train (using 1 epoch just to create the file structure for the user)
    # Increase epochs for actual training
    model.fit(train_ds, validation_data=val_ds, epochs=1)
    
    # Save the model
    model.save('seashell_classifier.h5')
    print("Model saved as seashell_classifier.h5")

if __name__ == "__main__":
    # Ensure dataset has at least some files to avoid errors during script run
    # In a real GitHub repo, the user would upload their images to these folders
    train_model()
