# 1. Requerimientos de la tienda de cilanté

## Información del producto

El sistema debe mostrar la información completa del producto Cilanté, incluyendo:

- Descripción general

- Ingredientes (cilantro cimarrón, canela, miel de abeja)

- Beneficios y propiedades

- Precio y presentación

- Imagen del producto

## Compra y contacto

- El sistema debe incluir un botón de compra visible en la página principal que redirija al chat de WhatsApp Web de la empresa con un mensaje predefinido, por ejemplo:

ej: “Hola, estoy interesada en comprar Cilanté 🌿”

- El sistema debe permitir consultar la información de contacto (correo, redes sociales, ubicación o número de WhatsApp).

- El sistema debe incluir un formulario de contacto para consultas o sugerencias, que envíe el mensaje a un correo definido o lo guarde en la base de datos.

## Usuarios y autenticación

- El sistema debe permitir el registro e inicio de sesión de usuarios, para que puedan dejar comentarios o seguir actualizaciones del producto.

- El usuario podrá actualizar sus datos personales (nombre, correo, contraseña).

## Contenido y presencia digital

- La página debe incluir una sección informativa o blog con artículos relacionados con bienestar femenino, autocuidado o beneficios del té natural.

- El sistema debe mostrar testimonios o reseñas de usuarias satisfechas con el producto.

- El sitio debe incluir enlaces directos a redes sociales oficiales (Instagram, TikTok, Facebook, etc.).

# 2. Aspectos Técnicos (Flask + SQLite)

| **Componente**        | **Descripción** |
|------------------------|-----------------|
| **Backend**            | Desarrollado con **Flask (Python 3.10+)**, usando una estructura modular basada en **Blueprints** (`auth`, `shop`, `admin`). |
| **Base de datos**      | **SQLite** durante la fase de desarrollo, utilizando **SQLAlchemy** como ORM para facilitar migraciones a otras bases de datos (MySQL o PostgreSQL). |
| **Frontend**           | Construido con **HTML5**, **CSS3** y **JavaScript**. Se utiliza el framework de **Tailwind CSS** para el diseño responsivo. |
| **Autenticación**      | Implementada con **Flask-Login** para el manejo de sesiones de usuario y autenticación segura. |
| **ORM**                | **SQLAlchemy**, para abstraer la lógica de acceso a datos y permitir compatibilidad entre diferentes motores de base de datos. |
| **Formularios**        | Gestión mediante **Flask-WTF**, con validación tanto en cliente como en servidor. |
| **Archivos estáticos** | Ubicados en `/static/` con subcarpetas para `css/`, `js/` e `img/`. |
| **Templates**          | Sistema de plantillas **Jinja2**, utilizando herencia de plantillas base (`base.html`). |
| **Entorno**            | Configurado mediante archivo `.env` para almacenar variables sensibles (clave secreta, rutas credenciales, etc.). |

# 3. Estructura de Carpetas del Proyecto

```
cilante_store/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── instance/
│   └── cilante.db
├── migrations/
│   └── versions/
├── README.md
│
├── cilante/
│   ├── \__init__.py
│   ├── auth/          # Módulo de autenticación (registro e inicio de sesión)
│   ├── shop/          # Lógica del producto y vistas principales
│   ├── admin/         # Panel de administración
│   ├── assistant/        ← módulo para el modelo ML + chatbot
│   │   ├── \__init__.py
│   │   ├── routes.py     ← rutas Flask del chatbot
│   │   ├── ml_model.py   ← modelo ML (RandomForest + NLP simple)
│   │   ├── utils.py      ← funciones de apoyo (procesar texto, guardar datos)
│   │   ├── templates/
│   │   │   └── assistant.html  ← interfaz del chatbot
│   │   └── static/
│   │       └── js/chatbot.js   ← comportamiento del chat en la web
│   ├── models.py      # Modelos de base de datos
│   ├── templates/     # Plantillas HTML (Jinja2)
│   └── static/        # Archivos estáticos (CSS, JS, imágenes)
│       ├── css/
│       ├── js/
│       └── img/
```

app.py → Punto de entrada principal de la aplicación Flask.

config.py → Archivo de configuración (clave secreta, conexión a base de datos, etc.).

requirements.txt → Lista de dependencias para instalación rápida (pip install -r requirements.txt).

instance/ → Carpeta que contiene la base de datos SQLite (cilante.db).

cilante/ → Directorio principal de la aplicación, con módulos, plantillas y recursos estáticos.

auth/ → Módulo para registro e inicio de sesión.

shop/ → Módulo con la lógica del producto y vistas públicas.

admin/ → Panel de administración del contenido.

templates/ → Plantillas HTML renderizadas con Jinja2.

static/ → Archivos estáticos (CSS, JavaScript, imágenes).

# 4. IA: Entrenamiento de dos modelos de machine learning

Asistente de bienestar hormonal personalizado, con Random Forest para la predicción y NLP para procesamiento del mensaje del usuario

## Concepto

Un asistente que aprenda del ciclo menstrual, hábitos y síntomas de cada usuaria para ofrecer recomendaciones adaptadas: cuándo consumir Cilanté, qué cantidad y qué otros hábitos pueden acompañarlo.

## Datos a usar

- Fechas de ciclo menstrual

- Intensidad de síntomas (dolor, hinchazón, irritabilidad, etc.)

- Preferencias de sabor, temperatura o momento del día

## objetivo que predicirá el modelo

Clasificación multiclase: ¿Cuándo empezar? (3 días antes / 2 días antes / 1 día antes / el mismo día / no necesario)
Regresión: ¿Qué cantidad (ml/sachets) o frecuencia (tazas/día) recomendar?

1. Definición clara de las etiquetas

Clasificación multiclase: Define las clases con lógica de negocio (ej. 3 días antes, 2 días antes, 1 día antes, día de inicio, no necesario).
Regresión: Define la variable continua (ej. cantidad en ml o número de tazas/día).
Evita solapamiento: si una clase implica “no tomar”, la cantidad debe ser 0.

2. Preparación de datos

Features comunes para ambos modelos:

Día del ciclo, fase (folicular, ovulatoria, lútea).
Historial de síntomas (dolor, hinchazón, irritabilidad).
Tendencias (promedio móvil, picos previos).
Preferencias (momento del día, temperatura).
Señales NLP (intención, entidades, sentimiento, embeddings reducidos).


Normalización temporal: evita fuga de información (usa datos previos, no futuros).
Imputación: síntomas faltantes → KNNImputer o medianas por usuaria.
Codificación: variables categóricas → one-hot; embeddings → PCA/UMAP.

3. Entrenamiento

Dos modelos separados:

RF_clasificacion para cuándo empezar.
RF_regresion para cantidad.


Hiperparámetros clave:

n_estimators: 200–500.
max_depth: controla sobreajuste (8–20).
min_samples_leaf: sube si hay ruido.
class_weight='balanced' para clasificación si hay desbalance.


Validación:

Usa GroupKFold por usuaria o TimeSeriesSplit para respetar temporalidad.
No mezcles ciclos futuros en entrenamiento.

4. Evaluación

Clasificación: F1 por clase, balanced accuracy, matriz de confusión.
Regresión: MAE y RMSE por usuaria y por fase del ciclo.
Métricas de negocio: reducción de dolor reportado, adherencia.

5. Interpretabilidad

Usa Permutation Importance o SHAP para explicar recomendaciones.
Ejemplo: “Te recomiendo 2 días antes porque tus ciclos son regulares (29±2 días) y tus picos de dolor ocurren cerca del día -1.”

## Ingeniería de variables (features) para el RF

Combina datos estructurados del ciclo + features derivadas + señales del lenguaje (NLP):
A. Del ciclo menstrual

Día del ciclo (días desde el último periodo).
Longitud media de ciclo de la usuaria (y su desviación).
Variabilidad de ciclos (p. ej., std de los últimos 6).
Fase estimada (folicular, ovulatoria, lútea) como variable categórica.
Días faltantes para el próximo periodo (predicción basada en patrón histórico).
Estacionalidad: día de la semana, hora del día (para hábitos de consumo).

B. De síntomas (histórico y recientes)

Intensidad normalizada de dolor, hinchazón, irritabilidad, fatiga (0–10).
Tendencia (promedio móvil de 3–5 días, pendiente).
Hitos personales (picos de dolor previos y su distancia en días).

C. Preferencias y contexto

Preferencia de sabor/temperatura (one-hot).
Momento preferido de consumo (mañana/tarde/noche).
Adherencia: % días que siguió la recomendación anterior.
Sensibilidad personal a Cilanté (response to treatment): ¿bajó el dolor tras consumir? (∆ dolor 24–48 h).

D. Features de NLP (ver sección 4)

Intención (p.ej., “quiero prevenir cólicos”, “me siento hinchada”) → dummies.
Entidades extraídas: intensidad (“dolor 7/10”), tiempo (“desde ayer”), síntomas.
Sentimiento/afectivo (negativo/positivo, score).
Embeddings reducidos (p.ej., 5–20 componentes PCA).

## Preparación de datos (calidad y split temporal)

Series temporales por usuaria: evita fuga de información. Haz train/validation/test con división temporal (por ejemplo, últimos 2 ciclos como test).
Agrupación por usuaria: no mezcles registros de la misma usuaria entre train y test si quieres evaluar generalización a usuarias nuevas (GroupKFold).
Desbalance de clases: si pocos días requieren recomendación, usa class_weight='balanced', submuestreo o focal loss (si migras a otro modelo).
Imputación: KNNImputer/medianas por usuaria para síntomas faltantes; marca columnas con “faltante” como banderas binarias.
Normalización: RF no lo necesita, pero sí para embeddings si los combinas con otros modelos.

## Entrenamiento y evaluación del Random Forest
Hiperparámetros clave

n_estimators: 200–600 (más árboles = más robusto).
max_depth: controla sobreajuste (p. ej. 8–20).
min_samples_leaf: 1–10 (sube si hay ruido).
max_features: sqrt o log2.
class_weight: balanced si hay desbalance.

Buenas prácticas de validación

TimeSeriesSplit por usuaria o GroupKFold (usuario como grupo) + respeto del tiempo.
Métricas:

Clasificación: F1 por clase, balanced accuracy, AUROC (si binaria).
Regresión: MAE por usuaria y MAE estratificada por fase.
Métricas de negocio: reducción de dolor reportado, adherencia, satisfacción.



Interpretabilidad

Importancias de características (Gini/Permutation).
SHAP por usuaria para explicar: “La recomendación fue 2 días antes porque…”
Usa esto para retroalimentación en el chatbot (“Te recomiendo empezar en 2 días porque tus últimos ciclos de 29±2 días y tus picos de dolor ocurren el día -1 a +1.”).

## Resultado

Una chatbot que diga cosas como:

“Según tus últimos ciclos, te recomiendo empezar a tomar Cilanté dos días antes del inicio de tu menstruación para reducir los cólicos.”

## Mini NLP con scikit-learn

Si quieres dar un paso más adelante, puedes usar un clasificador de texto para detectar la intención del mensaje.

Flujo:

Tienes frases de entrenamiento etiquetadas:

texto	etiqueta
“me duele el vientre”	malestar
“estoy bien hoy”	normal
“tengo cólicos fuertes”	malestar

Entrenas un modelo simple con TF-IDF + Naive Bayes o Logistic Regression:

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

vectorizer = TfidfVectorizer()
model = MultinomialNB()

nlp_model = make_pipeline(vectorizer, model)
nlp_model.fit(frases, etiquetas)


Luego predices:

respuesta = nlp_model.predict(["me duele el abdomen"])


Esto te permite manejar frases más variadas sin depender de keywords exactas.

# 5. Diseño base de datos

tabla: usuarios

- user_id -> PK, int, autoincrement, not null

- username -> string 20, unique, not null

- email -> string 50, unique, not null,

- password_hash -> string 128, not null

tabla: comentarios

- coment_id -> PK, int, autoincrement, not null

- contenido -> String 255, not null

- user_id -> FK, int, not null

tabla: contactos

- contacto_id -> PK, int, autoincrement, not null

- user_id -> FK, int, not null

- nombre -> string 20, not null

- apellido -> string 50, not null

- telefono -> string 13, not null, unique

tabla: ChatLogs

- chatLog_id -> int, PK, not null, autoincrement

- mensaje_usuario -> string 100

- respuesta_bot -> string 255

- created_at -> DateTime

## ejemplo

En tu archivo models.py, agrega una tabla simple para registrar las interacciones:

```python
#Y en routes.py, después de generar la respuesta:

from ..models import ChatLog
from cilante import db

# dentro del endpoint /chaty 

log = ChatLog(user_message=user_input, bot_response=respuesta)
db.session.add(log)
db.session.commit()
```

## TODO-list de avances y pendientes

### Logrado

- Estructura base del proyecto con Flask y Blueprints
- Configuración de base de datos SQLite y modelos principales (`Usuarios`, `Comentarios`, `Contactos`, `ChatLogs`)
- Registro e inicio de sesión de usuarios con Flask-Login y Flask-WTF
- Validación de formularios y manejo de sesiones
- Plantillas base con Jinja2 y navbar dinámico según autenticación
- Rutas principales para registro, login, logout y vistas públicas
- Integración de archivos estáticos (CSS, JS, imágenes)
- Configuración de variables sensibles con `.env`
- Migraciones con Flask-Migrate
- Esquema para guardar logs de chat en la base de datos

### Pendiente

- Estructura completa del chat (frontend y backend)
- Implementar NLP para procesar el mensaje del usuario
- Entrenar e integrar el modelo de Random Forest para recomendaciones
- Mejorar la presentación y diseño final del sitio (UI/UX)
