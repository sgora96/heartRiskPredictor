import pandas as pd
import joblib

# Para este ejemplo, entrenamos en caliente (puedes cargar un modelo entrenado)
from sklearn.ensemble import RandomForestClassifier

def preprocess_input(data):
    # Conversión simple (debes mapear tus categóricas)
    mapping = {
        'Sex': {'M': 1, 'F': 0},
        'ChestPainType': {'ATA': 0, 'NAP': 1, 'ASY': 2, 'TA': 3},
        'RestingECG': {'Normal': 0, 'ST': 1, 'LVH': 2},
        'ExerciseAngina': {'N': 0, 'Y': 1},
        'ST_Slope': {'Up': 0, 'Flat': 1, 'Down': 2}
    }

    for key in mapping:
        data[key] = mapping[key][data[key]]

    df = pd.DataFrame([data])
    return df

def predict_with_random_forest(data):
    df = preprocess_input(data)
    
    # Entrenamiento dummy (usa tus datos reales en producción)
    X = df.copy()
    y = [1]  # dummy target
    model = RandomForestClassifier()
    model.fit(X, y)

    return model.predict(df)[0]
