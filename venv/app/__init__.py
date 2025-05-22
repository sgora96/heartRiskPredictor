import os
from flask import Flask

def create_app():
    # Defino la ruta absoluta a la carpeta templates, que está 1 nivel arriba de app/
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

    app = Flask(__name__, template_folder=template_dir)

    from .routes import main
    app.register_blueprint(main)
    
    return app
