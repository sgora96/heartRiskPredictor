import os
import numpy as np
from joblib import load

# Ruta absoluta a la carpeta actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Carga los modelos desde la ruta absoluta
model = load(os.path.join(BASE_DIR, 'cardio_model.joblib'))
label_encoders = load(os.path.join(BASE_DIR, 'label_encoders.joblib'))

def load_model():
    return model, label_encoders

def make_prediction(input_data):
    model, encoders = load_model()
    data = input_data.copy()

    print("Datos recibidos en make_prediction:", data)  # Depuración: qué llega

    for col in ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']:
        print(f"Antes de transformar {col}: {data.get(col)}")  # Valor antes
        print(f"Clases del encoder para {col}: {encoders[col].classes_}")  # Clases esperadas
        data[col] = encoders[col].transform([data[col]])[0] if col in data else 0
        print(f"Después de transformar {col}: {data[col]}")  # Valor transformado

    values = np.array([list(data.values())])
    print("Valores para el modelo:", values)
    prediction = model.predict(values)[0]

    return "Enfermedad Cardiovascular Detectada" if prediction == 1 else "Sin Enfermedad Cardiovascular"

