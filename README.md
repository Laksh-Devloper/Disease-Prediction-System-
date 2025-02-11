# Disease Prediction System

This project is a **machine learning-based disease prediction system** that predicts the likelihood of **diabetes, heart disease, and Parkinson’s** based on patient data. The system uses multiple models, applies Tomek Links for data balancing, and selects the best-performing model for each disease.

## Features
- Supports **three diseases**: Diabetes, Heart Disease, and Parkinson’s.
- Implements **four machine learning models**: Standard Linear Model, Decision Tree, Logistic Regression, and Random Forest.
- **Applies Tomek Links** for handling imbalanced datasets.
- **Achieves high accuracy**: 80% for Diabetes, 89% for Heart Disease, and 92% for Parkinson’s.
- **User-friendly interface** using Streamlit.

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/Laksh-Devloper/Disease-Prediction-System-
cd Disease-Prediction-System-
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

## Technologies Used
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-Learn, Streamlit, Tomek Links (imbalanced-learn)
- **Machine Learning Models**: Logistic Regression, Decision Tree, Random Forest, Standard Linear Model

## Dataset
- The dataset includes patient records with relevant features for each disease.
- Preprocessed using **Tomek Links** to reduce class imbalance.

## Model Comparison (Before & After Tomek Links)
| Model | Diabetes (Before) | Heart Disease (Before) | Parkinson's (Before) | Diabetes (After) | Heart Disease (After) | Parkinson's (After) |
|--------|------------------|-----------------------|---------------------|----------------|---------------------|-------------------|
| Standard Linear Model | 75.32% | 86.88% | 87.18% | - | **89.09%** | - |
| Decision Tree | 74.67% | 83.61% | 76.92% | - | - | - |
| Logistic Regression | 74.67% | 85.12% | 87.82% | - | - | - |
| Random Forest | 72.08% | 83.61% | 79.49% | **80.42%** | - | **92.10%** |

## Future Work
- Improve model generalization with **more advanced preprocessing techniques**.
- Expand the system to predict **more diseases**.
- Deploy the model as a **web-based API** for easier integration.

## Contributors
- **Laksh-Devloper** (Project Lead)

