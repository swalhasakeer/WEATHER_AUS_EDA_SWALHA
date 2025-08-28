# **Project Report: Rain Prediction Using Machine Learning**

---

## **Project Title:**
Rainfall Prediction Using Machine Learning Classifiers

## 🔍 **Problem Statement**

- The goal of this project is to predict whether it will rain tomorrow in a given Australian location based on historical weather data. The target variable is RainTomorrow, a binary classification problem where:

- 1 → It will rain tomorrow

- 0 → It will not rain tomorrow

- This problem has real-world implications for sectors like agriculture, transportation, and public safety.

## 🎯 **Objective / Goal**

- Explore and clean the weather dataset.

- Perform Exploratory Data Analysis (EDA).

- Build and evaluate multiple classification models to predict rainfall for the next day.

- Handle class imbalance using SMOTE (Synthetic Minority Oversampling Technique).

- Compare model performance and save the best model for deployment.

## 📦 **Dataset Description**

- The dataset used is the weatherAUS.csv file which contains daily weather observations from various locations in Australia.

- Key features include:

   - Date: Observation date

   - Location: Site of the weather station

   - MinTemp, MaxTemp, Rainfall, WindSpeed9am, WindSpeed3pm

   - Humidity9am, Humidity3pm, Pressure9am, Pressure3pm

   - RainToday, RainTomorrow (target variable)

## 📊 **Exploratory Data Analysis (EDA)**

## 🧱 **Class Distribution**

- RainTomorrow = 0: ~77.6%

- RainTomorrow = 1: ~22.4%

- The dataset is imbalanced, requiring balancing techniques like SMOTE.

## 📈 **Inference from Visualizations**

- Barplot: Average rainfall is significantly higher on days before it rains tomorrow (RainTomorrow=1) compared to when it does not.

- Pie Chart: Shows the class imbalance of the target variable, highlighting the need for resampling.

## ⚙️ **Machine Learning Models Applied**

- The following classifiers were trained and tested:

- Logistic Regression

- Decision Tree Classifier

- Random Forest Classifier

- K-Nearest Neighbors (K=11)

- Support Vector Machine (Linear Kernel)

- Extra Trees Classifier

- All models were evaluated using:

- Accuracy Score

- Classification Report (Precision, Recall, F1-Score)

- Confusion Matrix

- Final Comparison Bar Plot

## ⚖️ **Handling Imbalanced Data**

- Technique Used: SMOTE (Synthetic Minority Oversampling Technique)

- Oversampling was applied to the training set.

- Model was retrained (Logistic Regression shown here) and compared against the original.

## 🧠 **Best Performing Model**

- The models were evaluated based on accuracy and classification reports. The top-performing model was selected and saved using pickle for future use. DecisionTreeClassifier is the best model in this project.

## 🧪 **After SMOTE**

- Accuracy decreased after applying SMOTE

## 📉 **Performance Visualization**

- Final model performance was visualized using a seaborn bar plot comparing all model's accuracies.

- Confusion matrices were plotted for each model to show prediction distribution across classes.

## 🖥️ **Flask Web Application** 🌐

A simple Flask web app allows users to input weather details and get instant predictions on whether it will rain tomorrow.

![image](https://github.com/user-attachments/assets/98c9c620-205a-4b51-885b-83ef4fb60025)


### 🏃 How to Run the App Locally

```
git clone https://github.com/swalhasakeer/WEATHER_AUS_EDA_SWALHA.git
cd Rain\ Prediction
pip install -r requirements.txt
python app.py
```

Then open your browser and go to:
📍 http://127.0.0.1:5000/

## 📁 **Project Structure**
```
├── WEATHER_AUS_EDA_SWALHA.ipynb
├── flask_app.py                  # Flask app
├── Scaler.pkl              # Standard Scaler
├── templates/
│   └── index.html           # HTML form for user input
├── requirements.txt
└── README.md
```

## 📌 **Conclusion**

- Weather prediction using classification models is feasible with historical data.

- Handling imbalanced data is crucial for improving performance, especially recall.

- Decision Trees and Random Forests performed well. Random Forest have the highest accuracy, but after SMOTE, this model's accuracy was decreased . So, the selected model is  **RandomForestClassifier** without resampling (SMOTE) .


  ![ChatGPT Image Apr 24, 2025, 01_00_21 PM](https://github.com/user-attachments/assets/53aa628b-9d67-4164-98a2-fcb8b8af7857)
  

## ✅ **Future Work**

- Hyperparameter tuning for all models.

- Try ensemble techniques like XGBoost or LightGBM.

- Use time-based train-test split for temporal consistency.


---
**Prepared by:**
Swalha Sakeer
