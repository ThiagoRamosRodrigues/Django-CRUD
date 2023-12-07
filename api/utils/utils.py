import joblib
from django.conf import settings
import os

def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'cad', 'api', 'utils', 'modelo_rede_neural_bebedor.pkl')
    model = joblib.load(model_path)
    return model

