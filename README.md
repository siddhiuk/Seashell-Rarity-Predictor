# Seashell-Rarity-Predictor
This repository contains a Python-based machine learning system for seashell rarity classification. It uses scikit-learn’s RandomForestClassifier trained on a structured dataset and deploys the model via a lightweight Tkinter desktop interface.
# 🐚 Seashell Rarity Predictor

The **Seashell Rarity Predictor** is a machine learning–based desktop application that predicts the rarity of seashells using physical and environmental features. The system uses a **Random Forest classifier** trained on a synthetic dataset and provides predictions through a simple **Tkinter GUI**.

This project demonstrates the practical application of **supervised learning**, **data preprocessing**, and **model deployment** using Python.

---

## 📌 Features

- Machine learning–based rarity prediction  
- Random Forest classification model  
- Synthetic dataset with 1200+ records  
- User-friendly desktop GUI (Tkinter)  
- Real-time prediction output  
- Beginner-friendly and well-structured code  

---

## 🧠 Dataset Description

The dataset (`seashells_dataset.csv`) contains the following features:

| Column | Description |
|------|------------|
| length | Shell length (cm) |
| width | Shell width (cm) |
| thickness | Shell thickness (mm) |
| weight | Shell weight (grams) |
| pattern | Pattern complexity (1 = Low, 4 = Very High) |
| location | 1 = Beach, 2 = Deep Sea |
| rarity | Target class (Common, Uncommon, Rare, Very Rare) |

> Note: A synthetic dataset is used due to the unavailability of real-world labeled seashell rarity data.

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Tkinter  
- Random Forest Classifier  

---

