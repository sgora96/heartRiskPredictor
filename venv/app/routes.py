from flask import Blueprint, render_template, request
from app.model.random_forest_model import predict_with_random_forest
from app.model.logistic_model import predict_with_logistic_regression
from utils.plot_utils import generate_plot
import base64
from io import BytesIO

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot_url = None

    if request.method == 'POST':
        data = {
            "Age": int(request.form['Age']),
            "Sex": request.form['Sex'],
            "ChestPainType": request.form['ChestPainType'],
            "RestingBP": int(request.form['RestingBP']),
            "Cholesterol": int(request.form['Cholesterol']),
            "FastingBS": int(request.form['FastingBS']),
            "RestingECG": request.form['RestingECG'],
            "MaxHR": int(request.form['MaxHR']),
            "ExerciseAngina": request.form['ExerciseAngina'],
            "Oldpeak": float(request.form['Oldpeak']),
            "ST_Slope": request.form['ST_Slope'],
        }

        prediction = predict_with_random_forest(data)
        result = "Presencia de enfermedad cardiovascular" if prediction == 1 else "No hay presencia de enfermedad"

        fig = generate_plot(data)
        img = BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html', result=result, plot_url=plot_url)
