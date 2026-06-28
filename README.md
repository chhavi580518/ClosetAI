# 👗 Closet AI – Smart Fashion Recommendation System

Closet AI is an AI-powered fashion assistant built using Python, Streamlit, tenserflow and Machine Learning concepts.  
It allows users to upload clothing images and get smart outfit suggestions based on occasion and style.

---

## 🚀 Features

- 📸 Upload clothing images via interactive UI  
- 🧠 AI-based outfit suggestion system (rule-based / ML-ready)  
- 👕 Recommendations for different occasions:
  - Casual  
  - Formal  
  - Party  
  - sports 
- 🎨 Clean and modern Streamlit web interface  
- ⚡ Fast and lightweight application  
- 📊 Ready for deep learning model integration (CNN/TensorFlow)

---

## 🛠️ Tech Stack

- Python 3.11.4  
- Streamlit (Frontend UI)  
- NumPy (Data processing)  
- Pandas (Dataset handling)  
- Pillow (Image processing)  
- OpenCV (Image preprocessing)  
- TensorFlow (Optional AI/ML support)

---

## 📁 Project Structure
CLOSETAI/
├── .gitignore
├── pyvenv.cfg
├── app.py
├── README.md
├── requirements.txt
├── test_prediction.py
├── ai/
│   ├── __pycache__/
│   ├── model.keras
│   ├── predict.py
│   └── train_model.py
├── assets/
│   ├── icons/
│   └── logos/
│       └── logo.png
├── database/
├── dataset/
│   ├── test/
│   │   ├── pants/
│   │   ├── shirt/
│   │   ├── shoes/
│   │   ├── shorts/
│   │   ├── sneakers/
│   │   └── t-shirt/
│   └── train/
│       ├── pants/
│       ├── shirt/
│       ├── shoes/
│       ├── shorts/
│       ├── sneakers/
│       └── t-shirt/
├── images/
│   ├── dress/
│   │   ├── black_dress.jpg
│   │   ├── floral_dress.jpg
│   │   ├── party_dress.jpg
│   │   ├── red_dress.jpg
│   │   └── white_dress.jpg
│   ├── jeans/
│   │   ├── black_jeans.jpg
│   │   ├── blue_jeans.jpg
│   │   ├── grey_jeans.jpg
│   │   ├── ripped_jeans.jpg
│   │   └── slimfit_jeans.jpg
│   ├── shirt/
│   │   ├── blue_casual_shirt.jpg
│   │   ├── checked_shirt.jpg
│   │   ├── lavender_formal_Shirt.jpg
│   │   ├── ripped_jeans.jpg
│   │   ├── striped_shirt.jpg
│   │   └── white_formal_shirt.jpg
│   ├── shoes/
│   │   ├── black_formal_shoes.jpg
│   │   ├── casual_shoes.jpg
│   │   ├── running_shoes.jpg
│   │   ├── sports_shoes.jpg
│   │   └── white_sneakers.jpg
│   └── trouser/
│       ├── black_trouser.jpg
│       ├── cargo_trouser.jpg
│       ├── formal_trouser.jpg
│       ├── grey_trouser.jpg
│       └── khaki_trouser.jpg
├── repository/
│   ├── __pycache__/
│   ├── clothing_repository.py
│   └── image_repository.py
└── venv/
    ├── etc/
    ├── Include/
    ├── Lib/
    ├── Scripts/
    └── share/
