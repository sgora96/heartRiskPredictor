# utils/plot_utils.py

import matplotlib.pyplot as plt

def generate_plot(data, model='random_forest'):
    fig, ax = plt.subplots(figsize=(6,4))
    # Ejemplo sencillo: graficar algo distinto según modelo
    if model == 'random_forest':
        ax.bar(['Edad', 'Presión', 'Colesterol'], [data['Age'], data['RestingBP'], data['Cholesterol']])
        ax.set_title('Datos relevantes - Random Forest')
    elif model == 'logistic_regression':
        ax.plot([0, 1, 2], [data['Age'], data['RestingBP'], data['Cholesterol']], marker='o')
        ax.set_title('Datos relevantes - Regresión Logística')
    ax.set_ylabel('Valor')
    ax.grid(True)
    return fig
