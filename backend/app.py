from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, model


app = FastAPI()

# Pydantic model to validate data


@app.get('/')
def home():
    return {"message": "Welcome to the PCOS Risk Prediction API. Use the /predict endpoint to get predictions."}

@app.get('/health')
def health_check():
    return {"status" : "OK",
            "model_status" : "Loaded" if model else "Not loaded"}



@app.post("/predict")
def predict_pcos(input_data: UserInput):
    
    user_input = input_data.model_dump(by_alias=True)

    # Make prediction using the loaded model
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={"prediction": prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

