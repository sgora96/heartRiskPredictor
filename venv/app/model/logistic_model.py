import pandas as pd
from sklearn.linear_model import LogisticRegression

def preprocess_input(data):
    mapping = {
        "Sex": {"F": 0, "M": 1},
        "ChestPainType": {"ASY": 0, "ATA": 1, "NAP": 2, "TA": 3},
        "RestingECG": {"Normal": 0, "ST": 1, "LVH": 2},
        "ExerciseAngina": {"N": 0, "Y": 1},
        "ST_Slope": {"Up": 0, "Flat": 1, "Down": 2}
    }

    for key in mapping:
        value = data.get(key)
        if value in mapping[key]:  # Validar existencia
            data[key] = mapping[key][value]
        else:
            raise ValueError(f"Valor no esperado '{value}' para el campo '{key}'")
    
    return pd.DataFrame([data])

def predict_with_logistic_regression(data):
    df = preprocess_input(data)
    y = [1]  # Dummy
    model = LogisticRegression()
    model.fit(df, y)

    return model.predict(df)[0]
