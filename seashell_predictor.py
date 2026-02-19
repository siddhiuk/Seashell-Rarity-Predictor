import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import messagebox

# 1. Load the dataset
try:
    df = pd.read_csv('seashells_dataset.csv')
except FileNotFoundError:
    # Create dummy data if file doesn't exist for demonstration
    data = {
        'length': [45, 60, 100, 120, 30, 50, 90, 110],
        'width': [30, 40, 70, 80, 20, 35, 60, 75],
        'thickness': [10, 15, 30, 40, 5, 12, 25, 35],
        'weight': [20, 40, 100, 150, 10, 30, 80, 120],
        'pattern': [1, 2, 3, 4, 1, 2, 3, 4],
        'location': [1, 1, 2, 2, 1, 1, 2, 2],
        'rarity': ['Common', 'Common', 'Rare', 'Very Rare', 'Common', 'Uncommon', 'Rare', 'Very Rare']
    }
    df = pd.DataFrame(data)
    df.to_csv('seashells_dataset.csv', index=False)
    print("Created dummy dataset 'seashells_dataset.csv'")

# 2. Prepare data
X = df[['length', 'width', 'thickness', 'weight', 'pattern', 'location']]
y = df['rarity']

# 3. Encode target
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 4. Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y_encoded)

# 5. GUI Application
def predict_rarity():
    try:
        # Get inputs
        length = float(entry_length.get())
        width = float(entry_width.get())
        thickness = float(entry_thickness.get())
        weight = float(entry_weight.get())
        pattern = int(var_pattern.get())
        location = int(var_location.get())

        # Predict
        features = [[length, width, thickness, weight, pattern, location]]
        prediction_index = clf.predict(features)[0]
        prediction_label = le.inverse_transform([prediction_index])[0]

        # Show result
        messagebox.showinfo("Prediction Result", f"The predicted rarity is: {prediction_label}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Setup Tkinter
root = tk.Tk()
root.title("Seashell Rarity Predictor")
root.geometry("400x500")

# Labels and Entries
labels = ["Length (mm):", "Width (mm):", "Thickness (mm):", "Weight (g):"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(pady=5)
    entries.append(entry)

entry_length, entry_width, entry_thickness, entry_weight = entries

# Pattern Dropdown
tk.Label(root, text="Pattern (1-4):").pack(pady=5)
var_pattern = tk.StringVar(value="1")
tk.OptionMenu(root, var_pattern, "1", "2", "3", "4").pack(pady=5)

# Location Dropdown
tk.Label(root, text="Location:").pack(pady=5)
var_location = tk.StringVar(value="1")
tk.Radiobutton(root, text="Beach (1)", variable=var_location, value="1").pack()
tk.Radiobutton(root, text="Deep Sea (2)", variable=var_location, value="2").pack()

# Predict Button
tk.Button(root, text="Predict Rarity", command=predict_rarity, bg="lightblue", font=("Arial", 12, "bold")).pack(pady=20)

# Run
root.mainloop()
