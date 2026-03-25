# Cricket-Match-Outcome-Predictor
Use historical IPL/ODI data to build a simple prediction model. Very engaging and datasets.
# 🏏 Cricket Match Outcome Predictor

A machine learning web application that predicts the outcome of IPL cricket matches based on historical match data. Built with Python, Scikit-learn, and Flask.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Model Details](#model-details)
- [Results](#results)
- [Challenges & Learnings](#challenges--learnings)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## About the Project

Cricket match prediction is a challenging problem because outcomes depend on many factors — team composition, venue, toss decision, and historical performance. This project attempts to predict which team will win an IPL match using a **Random Forest Classifier** trained on real IPL match data (2008–2019).

The model is served through a **Flask web app** where a user can input match details and instantly get a predicted winner along with a win probability score.

This project was built as part of a Python & Data Structures course capstone (BYOP) to apply concepts of data preprocessing, machine learning, and web development in a real-world context.

---

## Demo

> Enter two teams, the venue, and the toss details → Get an instant win prediction.

```
Team 1:        Mumbai Indians
Team 2:        Chennai Super Kings
Venue:         Wankhede Stadium
Toss Winner:   Mumbai Indians
Toss Decision: Bat

→ Predicted Winner: Mumbai Indians (67.3% win probability)
```

---

## Tech Stack

| Layer         | Technology                        |
|---------------|-----------------------------------|
| Language      | Python 3.10+                      |
| Data handling | Pandas, NumPy                     |
| ML Model      | Scikit-learn (Random Forest)      |
| Model saving  | Joblib / Pickle                   |
| Web framework | Flask                             |
| Frontend      | HTML, CSS (Bootstrap 5)           |


---


## Features

- Predicts the winning team for any IPL match combination
- Displays win probability as a percentage
- Clean web interface — no technical knowledge needed to use
- Shows feature importance (which factors matter most)
- Trained on 12 years of real IPL data

---

## Project Structure

```
cricket-predictor/
│
├── data/
│   └── matches.csv                  # Raw IPL dataset (download from Kaggle)
│
├── notebooks/
│   └── eda_and_training.ipynb       # Data exploration + model training
│
├── model/
│   └── predictor.pkl                # Saved trained model (generated after training)
│
├── app/
│   ├── app.py                       # Flask application
│   ├── templates/
│   │   ├── index.html               # Input form page
│   │   └── result.html              # Prediction result page
│   └── static/
│       └── style.css                # Custom styles
│
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cricket-predictor.git
cd cricket-predictor
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


---

## How to Use

1. Open the web app in your browser
2. Select **Team 1** and **Team 2** from the dropdown menus
3. Select the **Venue** (stadium)
4. Choose the **Toss Winner** and their **decision** (Bat or Field)
5. Click **Predict**
6. The app will display the predicted winner and win probability

---

## Model Details

| Parameter        | Value                          |
|------------------|-------------------------------|
| Algorithm        | Random Forest Classifier       |
| Train/Test split | 80% / 20%                      |
| Encoding         | Label Encoding (categorical features) |
| Key features     | Team, venue, toss winner, toss decision, season |
| Model accuracy   | ~68–72% on test set            |

**Feature Importance (approximate ranking):**
1. Team strength (historical win rate)
2. Venue advantage
3. Toss decision
4. Season / year
5. Toss winner

---

## Results

- **Test Accuracy:** ~70%
- The model correctly identifies stronger teams in home venues
- Toss decision (bat vs field) has moderate influence
- Accuracy is realistic — even expert analysts cannot predict cricket outcomes with high certainty

---

## Challenges & Learnings

- **Categorical encoding:** Teams and venues needed label encoding before being fed to the model
- **Class imbalance:** Some teams appear far more often than others in the dataset; handled using balanced class weights
- **Feature selection:** Dropping irrelevant columns (umpire names, DL applied) improved model focus
- **Flask integration:** Loading a `.pkl` model in Flask and passing form inputs as a NumPy array for prediction

---

## Future Improvements

- Add player-level statistics (top scorer, bowling average)
- Include live match data via CricAPI
- Improve UI with a live win probability gauge
- Extend to ODI and T20 World Cup data
- Deploy on Render or Railway for public access

---

## Author

**Asmita Dekaphukan**
- Email: asmita.25boe10102@vitbhopal.ac.in
- Course: Introduction to Problem Solving and Programming — BYOP Capstone Project

---

## License

This project is open source and available under the [MIT License](LICENSE).
