import pickle
import numpy as np
import pandas as pd
from typing import List, Dict, Optional, Tuple
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
import os

MODEL_PATH = "models/rf_predictor.pkl"
N_DAYS_AHEAD = 7
THRESHOLD = 0.6
FEATURE_COLUMNS = [
    'cycle_day', 'avg_pain_last_3', 'had_pain_yesterday',
    'had_inflammation_2d', 'avg_duration_prev', 'age',
    'regular_cilante', 'avg_sleep'
]


class MenstrualPredictor:
    def __init__(self, model_path: str = MODEL_PATH):
        self.feature_names = FEATURE_COLUMNS
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        """Carga el modelo o lo entrena con datos sintéticos si no existe."""
        if os.path.exists(self.model_path):
            with open(self.model_path, 'rb') as f:
                return pickle.load(f)
        else:
            print("Modelo no encontrado. Entrenando con datos sintéticos...")
            return self._train_synthetic_model()

    def _generate_synthetic_data(self, n_samples: int = 600) -> Tuple[pd.DataFrame, np.ndarray]:
        """Genera datos sintéticos realistas para entrenamiento inicial."""
        np.random.seed(42)
        data = []
        targets = []

        for _ in range(n_samples):
            cycle_day = np.random.randint(1, 29)
            age = np.random.randint(18, 45)
            avg_pain_last_3 = np.random.uniform(0, 10)
            had_pain_yesterday = 1 if avg_pain_last_3 > 5.5 else 0
            had_inflammation_2d = np.random.choice([0, 1], p=[0.65, 0.35])
            avg_duration_prev = np.random.uniform(2.5, 5.5)
            regular_cilante = np.random.choice([0, 1], p=[0.7, 0.3])
            avg_sleep = np.random.uniform(5.5, 8.5)

            base_prob = 0.08
            if 19 <= cycle_day <= 28:
                base_prob = 0.68 + (avg_pain_last_3 / 15)
            elif 12 <= cycle_day <= 18:
                base_prob = 0.35

            if had_pain_yesterday:
                base_prob *= 1.4
            if regular_cilante:
                base_prob *= 0.65
            base_prob = np.clip(base_prob, 0.05, 0.97)
            
            target = []
            for d in range(1, 8):
                future_day = ((cycle_day + d - 1) % 28) + 1
                day_factor = 1.4 if 22 <= future_day <= 27 else 0.85
                prob = base_prob * day_factor
                target.append(1 if np.random.random() < prob else 0)

            data.append([
                cycle_day, avg_pain_last_3, had_pain_yesterday,
                had_inflammation_2d, avg_duration_prev, age,
                regular_cilante, avg_sleep
            ])
            targets.append(target)

        X = pd.DataFrame(data, columns=self.feature_names)
        y = np.array(targets)
        return X, y

    def _train_synthetic_model(self):
        """Entrena y guarda el modelo con datos sintéticos."""
        X, y = self._generate_synthetic_data()
        
        rf = RandomForestClassifier(
            n_estimators=120,
            max_depth=9,
            min_samples_split=8,
            min_samples_leaf=4,
            class_weight='balanced',
            random_state=42,
            n_jobs=-1
        )
        model = MultiOutputClassifier(rf)
        model.fit(X, y)

        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        with open(self.model_path, 'wb') as f:
            pickle.dump(model, f)

        print(f"Modelo entrenado y guardado en {self.model_path}")
        return model

    def predict_from_features(self, features: List[float]) -> Dict[str, any]:
        """Realiza predicción a partir de features ya calculadas."""
        if len(features) != len(self.feature_names):
            raise ValueError(f"Se esperan {len(self.feature_names)} features, se recibieron {len(features)}")

        X = np.array([features])
        probas = self.model.predict_proba(X)
        probabilities = [float(p[0, 1]) for p in probas]

        high_risk_days = [i + 1 for i, p in enumerate(probabilities) if p >= THRESHOLD]
        start_day = high_risk_days[0] if high_risk_days else None
        start_recommend = start_day - 1 if start_day else None

        return {
            'probabilities': probabilities,
            'high_risk_days_ahead': high_risk_days,
            'start_cilante_day_ahead': start_recommend,
            'recommendation_text': self._build_recommendation(high_risk_days, start_recommend),
            'confidence': round(max(probabilities) if probabilities else 0, 3)
        }

    def _build_recommendation(self, risk_days: List[int], start_day: Optional[int]) -> str:
        """Genera texto natural de recomendación."""
        if not risk_days:
            return "No se predicen cólicos intensos en los próximos 7 días. ¡Mantén tu rutina saludable!"

        days_str = ", ".join([f"+{d}" for d in risk_days])
        start_str = f"+{start_day}" if start_day is not None else "hoy"
        return (
            f"Se prevén cólicos intensos en los días {days_str}. "
            f"Empieza a tomar **Cilanté desde el día {start_str}** (1 sobre al día) "
            f"para reducir la inflamación antes del pico."
        )

    def retrain_with_real_data(self, X: pd.DataFrame, y: np.ndarray):
        """Reentrena el modelo con datos reales recolectados."""
        rf = RandomForestClassifier(
            n_estimators=150,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            class_weight='balanced',
            random_state=42,
            n_jobs=-1
        )
        model = MultiOutputClassifier(rf)
        model.fit(X, y)

        with open(self.model_path, 'wb') as f:
            pickle.dump(model, f)
        
        self.model = model
        print("Modelo reentrenado con datos reales.")

predictor = MenstrualPredictor()

def get_prediction(features: List[float]) -> Dict:
    return predictor.predict_from_features(features)
