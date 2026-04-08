# ❤️ Heart Disease Prediction using Machine Learning

##  Overview

This notebook explores the use of **Python-based Machine Learning and Data Science libraries** to build a model capable of predicting whether a patient has heart disease based on clinical attributes.

---

##  Approach

We follow a structured ML pipeline:

1. Problem Definition
2. Data Collection
3. Evaluation Metrics
4. Feature Understanding
5. Model Building
6. Experimentation

---

## 1. Problem Definition

> Given clinical parameters about a patient, can we predict whether or not they have heart disease?

---

##  2. Data

The dataset used comes from:

* **UCI Machine Learning Repository (Cleveland dataset)**
  https://archive.ics.uci.edu/dataset/45/heart+disease

* **Kaggle version**
  https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data

---

##  3. Evaluation

> If we can achieve **95% accuracy** in predicting heart disease during the proof of concept, we will consider the model successful.

---

##  4. Features (Data Dictionary)

### 🔹 Patient Information

* **age** — Age in years
* **sex** — (1 = male, 0 = female)

### 🔹 Medical Attributes

* **cp (chest pain type)**

  * 0: Typical angina
  * 1: Atypical angina
  * 2: Non-anginal pain
  * 3: Asymptomatic

* **trestbps** — Resting blood pressure (mm Hg)

  > Above 130–140 is a concern

* **chol** — Serum cholesterol (mg/dl)

  > Above 200 is a concern

* **fbs** — Fasting blood sugar > 120 mg/dl

  * 1 = true, 0 = false

  > > 126 mg/dL may indicate diabetes

* **restecg** — Resting ECG results

  * 0: Normal
  * 1: ST-T wave abnormality
  * 2: Left ventricular hypertrophy

* **thalach** — Maximum heart rate achieved

* **exang** — Exercise-induced angina

  * 1 = yes, 0 = no

* **oldpeak** — ST depression (stress indicator)

  > Higher value = more heart stress

* **slope** — Slope of peak exercise ST segment

  * 0: Upsloping
  * 1: Flat
  * 2: Downsloping

* **ca** — Number of major vessels (0–3)

  > More blood flow = healthier

* **thal** — Thallium stress test

  * 1, 3: Normal
  * 6: Fixed defect
  * 7: Reversible defect

---

##  Target Variable

* **target** — Heart disease presence

  * 1 = Yes
  * 0 = No

---

##  5. Modelling

Machine Learning models are trained on the dataset to learn patterns and predict heart disease.

---

##  6. Experimentation

Different models and techniques are tested to improve performance and achieve the desired accuracy.

---

## Future Improvements

* Add multiple model comparison
* Improve evaluation metrics (Precision, Recall, F1-score)
* Deploy the model as a web application
* Enhance UI/UX

---

##  Author

**Shivendra Pawaiya**

* GitHub: https://github.com/Shivendra-20

---
