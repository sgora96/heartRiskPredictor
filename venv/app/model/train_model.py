import pandas as pd
import pyodbc
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from joblib import dump

# Conexión a la base de datos en Somee
conn_str = (
    "Driver={SQL Server};"
    "Server=DataSetMLProject.mssql.somee.com;"
    "Database=DataSetMLProject;"
    "Uid=sgoraml96_SQLLogin_1;"
    "Pwd=6lywiwdr67;"
    "TrustServerCertificate=yes;"
)

# Cargar datos
query = """
SELECT Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS,
       RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, HeartDisease
FROM dataSet
"""
df = pd.read_sql(query, pyodbc.connect(conn_str))

# Preprocesamiento: aplicar LabelEncoder y guardar cada uno
label_encoders = {}
for col in ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Guardamos el encoder por columna

# Separar características y etiquetas
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Construir rutas para guardar los modelos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'cardio_model.joblib')
ENCODER_PATH = os.path.join(BASE_DIR, 'label_encoders.joblib')

# Crear el directorio si no existe
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

# Guardar el modelo y los encoders
dump(clf, MODEL_PATH)
dump(label_encoders, ENCODER_PATH)

print(f"Modelo guardado exitosamente en {MODEL_PATH}")
print(f"Encoders guardados exitosamente en {ENCODER_PATH}")
