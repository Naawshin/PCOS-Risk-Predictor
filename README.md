# PCOS Risk Predictor

A machine learning-powered web application that predicts the risk of Polycystic Ovary Syndrome (PCOS) based on patient health and lifestyle factors. The application features a FastAPI backend for predictions and a Streamlit frontend for user interaction.

> **Project Scope:** This project is designed as a showcase portfolio demonstration to highlight expertise in **FastAPI development** and **Docker containerization**. While the application implements a functional ML prediction pipeline, the primary focus is on architectural design, API development, and deployment practices rather than medical prediction accuracy. This is a proof-of-concept intended for educational and demonstration purposes.

The dataset used to train the model can be found here: https://www.kaggle.com/datasets/ankushpanday1/pcos-prediction-datasettop-75-countries/data

## Overview

PCOS (Polycystic Ovary Syndrome) is a common hormonal disorder affecting many individuals. This application uses a trained machine learning model to assess PCOS risk based on various medical and lifestyle indicators, helping users understand their risk profile early.

## Features

- **ML-Powered Predictions**: Uses a scikit-learn trained model for accurate PCOS risk assessment
- **REST API Backend**: FastAPI-based API for handling predictions
- **Interactive Frontend**: Streamlit interface for easy user interaction
- **Health Checks**: Built-in API health monitoring
- **Docker Support**: Containerized deployment for easy scalability
- **Input Validation**: Pydantic-based validation for robust data handling
- **Comprehensive Parameters**: Analyzes 10+ medical and lifestyle factors

## Project Structure

```
PCOS-Risk-Predictor/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── Dockerfile          # Docker configuration
│   ├── requirements.txt    # Python dependencies
│   ├── model/
│   │   ├── model.pkl       # Trained ML model
│   │   └── predict.py      # Prediction logic
│   └── schema/
│       └── user_input.py   # Pydantic validation models
├── frontend/
│   ├── frontend.py         # Streamlit application
│   └── requirements.txt    # Frontend dependencies
├── LICENSE
└── README.md
```

## Installation

### Local Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/Naawshin/PCOS-Risk-Predictor.git
cd PCOS-Risk-Predictor
```

#### 2. Create Virtual Environment

```bash
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

#### 3. Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
cd ..
```

#### 4. Install Frontend Dependencies

```bash
cd frontend
pip install -r requirements.txt
cd ..
```

### Docker Setup

```bash
cd backend
docker build -t pcos-predictor-backend .
docker run -d -p 8000:8000 pcos-predictor-backend
```

## Usage

### Running the Backend (FastAPI)

```bash
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Running the Frontend (Streamlit)

```bash
cd frontend
streamlit run frontend.py
```

The frontend will open at `http://localhost:8501`

## API Endpoints

### GET `/`

Welcome message and general information.

**Response:**
```json
{
  "message": "Welcome to the PCOS Risk Prediction API. Use the /predict endpoint to get predictions."
}
```

### GET `/health`

Check API and model status.

**Response:**
```json
{
  "status": "OK",
  "model_status": "Loaded"
}
```

### POST `/predict`

Make a PCOS risk prediction.

**Request Body:**
```json
{
  "Age": 28,
  "BMI": "Normal",
  "Menstrual Regularity": "Irregular",
  "Hirsutism": "Yes",
  "Acne Severity": "Moderate",
  "Family History of PCOS": "Yes",
  "Insulin Resistance": "No",
  "Stress Levels": "Medium",
  "Urban/Rural": "Urban",
  "Socioeconomic Status": "Middle"
}
```

**Response:**
```json
{
  "prediction": "yes"
}
```
*The prediction value will be either "yes" (indicating higher PCOS risk) or "no" (indicating lower PCOS risk).*

## Input Parameters

| Parameter | Type | Values | Description |
|-----------|------|--------|-------------|
| Age | Integer | 1-120 | Patient age in years |
| BMI | String | Normal, Overweight, Underweight, Obese | Body Mass Index category |
| Menstrual Regularity | String | Regular, Irregular | Menstrual cycle regularity |
| Hirsutism | String | Yes, No | Excessive hair growth |
| Acne Severity | String | Unknown, Mild, Moderate, Severe | Severity of acne |
| Family History of PCOS | String | Yes, No | Family history of PCOS |
| Insulin Resistance | String | Yes, No | Presence of insulin resistance |
| Stress Levels | String | Low, Medium, High | Stress level |
| Urban/Rural | String | Urban, Rural | Living area type |
| Socioeconomic Status | String | Low, Middle, High | Socioeconomic status |

## Example Usage

### Using cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Age": 28,
    "BMI": "Normal",
    "Menstrual Regularity": "Irregular",
    "Hirsutism": "Yes",
    "Acne Severity": "Moderate",
    "Family History of PCOS": "Yes",
    "Insulin Resistance": "No",
    "Stress Levels": "Medium",
    "Urban/Rural": "Urban",
    "Socioeconomic Status": "Middle"
  }'
```

### Using Python Requests

```python
import requests

url = "http://localhost:8000/predict"
data = {
    "Age": 28,
    "BMI": "Normal",
    "Menstrual Regularity": "Irregular",
    "Hirsutism": "Yes",
    "Acne Severity": "Moderate",
    "Family History of PCOS": "Yes",
    "Insulin Resistance": "No",
    "Stress Levels": "Medium",
    "Urban/Rural": "Urban",
    "Socioeconomic Status": "Middle"
}

response = requests.post(url, json=data)
print(response.json())
```

## Technology Stack

**Backend:**
- FastAPI - Modern web framework for building APIs
- Uvicorn - ASGI web server
- Pydantic - Data validation and serialization
- Scikit-learn - Machine learning library
- Pandas - Data manipulation and analysis

**Frontend:**
- Streamlit - Rapid web app development framework

## Model Details

The predictive model is a trained machine learning classifier that has been serialized and saved as `backend/model/model.pkl`. It processes the input features to generate PCOS risk predictions.
You can find it here: https://drive.google.com/file/d/19ZN2cZ-D7LS3SfBvlhN-3dAyNiMwQ_Sl/view?usp=sharing

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the terms specified in the `LICENSE` file.

## Disclaimer

This application is for informational and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

## Contact

Author: Nowshin Tabasum

Email: nawshintabassum88@gmail.com

For questions or support, please open an issue in the repository.
