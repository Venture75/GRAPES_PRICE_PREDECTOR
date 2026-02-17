# 🍇 Grapes Price Predictor

> A Machine Learning web application that predicts grape prices (TZS/kg) in the Tanzanian market.

---

## 📌 Project Overview

This project was developed as part of the **Machine Learning Course (TEST2)** assignment. It trains and compares two ML models — **Linear Regression** and **Decision Tree** — on a Tanzanian grapes market dataset, deploys the best-performing model, and wraps it in an interactive **Streamlit** web application.

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `ml_project.ipynb` | Jupyter Notebook — full ML pipeline |
| `app.py` | Streamlit web application |
| `grapes_model.pkl` | Saved best-performing model (Linear Regression) |
| `grapes_encoders.pkl` | Label encoders for categorical features |
| `grapes_scaler.pkl` | StandardScaler for numerical features |
| `grapes_dataset.csv` | Generated Tanzanian grapes dataset (500 records) |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

---

## 🗂️ Dataset Description

- **Records:** 500 simulated Tanzanian grapes market entries
- **Features (9):**

| Feature | Type | Description |
|---------|------|-------------|
| Region | Categorical | Dodoma, Arusha, Morogoro, Mbeya, Singida |
| Grape_Type | Categorical | Red Globe, Thompson Seedless, Muscat, Flame Seedless |
| Season | Categorical | Dry Season / Wet Season |
| Quality_Grade | Categorical | Grade A, Grade B, Grade C |
| Weight_kg | Numerical | Batch weight (0.5 – 10.0 kg) |
| Sugar_Content_Brix | Numerical | Sweetness level (10 – 25 Brix %) |
| Farm_Size_ha | Numerical | Farm area (0.5 – 20 ha) |
| Distance_to_Market_km | Numerical | Distance from farm to market (5 – 300 km) |
| Rainfall_mm | Numerical | Annual rainfall (400 – 1200 mm) |

- **Target:** `Price_TZS_per_kg` — grape price in Tanzanian Shillings per kilogram (1,000 – 12,000 TZS)

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Label Encoding for categorical variables
- StandardScaler applied to numerical features
- 80/20 train-test split (random_state=42)

### 2. Models Trained
| Model | MAE (TZS) | RMSE (TZS) | R² Score |
|-------|-----------|------------|----------|
| Linear Regression | 301.64 | 375.68 | **0.7641** ✔ Best |
| Decision Tree | 514.04 | 633.80 | 0.3286 |

### 3. Best Model
**Linear Regression** was selected based on the highest R² score (0.7641) and lowest error metrics.

---

## 🚀 How to Run Locally

### Prerequisites
```bash
pip install -r requirements.txt
```

### Step 1 — Run the Jupyter Notebook
```bash
jupyter notebook ml_project.ipynb
```
Run all cells to generate `grapes_model.pkl`, `grapes_encoders.pkl`, and `grapes_scaler.pkl`.

### Step 2 — Launch the Streamlit App
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`

---

## ☁️ Deploy on Streamlit Cloud

1. Push all files to a **GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** → Connect your GitHub repo
4. Set **Main file path** to `app.py`
5. Click **Deploy** — your app will be live in minutes!

---

## 🖥️ App Features

- 🟣 **Purple grape-themed UI** with gradient design
- 📍 Dropdowns for Region, Grape Type, Season, and Quality Grade
- 📊 Sliders for all numerical inputs
- 💰 Instant price prediction in **TZS per kg**
- 📦 Total batch value calculation
- 🌡️ Sugar content quality indicator

---

## 👥 Team

> Each group member contributed to: data generation, preprocessing, model training, evaluation, visualization, app development, and deployment.

---

## 📅 Submission Details

| Item | Detail |
|------|--------|
| Course | Machine Learning |
| Task | TEST2 — Project Work |
| Deadline | 16th February 2026 |
| Presentation | 18th February 2026 |
| Country Context | Tanzania 🇹🇿 |

---

*🍇 Grapes Price Predictor · Tanzania Machine Learning Project · 2026*
