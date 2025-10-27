# Requerimientos de la tienda de cilanté

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

## ⚙️ Aspectos Técnicos (Flask + SQLite)

| **Componente**        | **Descripción** |
|------------------------|-----------------|
| **Backend**            | Desarrollado con **Flask (Python 3.10+)**, usando una estructura modular basada en **Blueprints** (`auth`, `shop`, `admin`). |
| **Base de datos**      | **SQLite** durante la fase de desarrollo, utilizando **SQLAlchemy** como ORM para facilitar migraciones a otras bases de datos (MySQL o PostgreSQL). |
| **Frontend**           | Construido con **HTML5**, **CSS3** y **JavaScript**. Se recomienda el uso de **Bootstrap** o **Tailwind CSS** para el diseño responsivo. |
| **Autenticación**      | Implementada con **Flask-Login** o **Flask-Security** para el manejo de sesiones de usuario y autenticación segura. |
| **ORM**                | **SQLAlchemy**, para abstraer la lógica de acceso a datos y permitir compatibilidad entre diferentes motores de base de datos. |
| **Formularios**        | Gestión mediante **Flask-WTF**, con validación tanto en cliente como en servidor. |
| **Archivos estáticos** | Ubicados en `/static/` con subcarpetas para `css/`, `js/` e `img/`. |
| **Templates**          | Sistema de plantillas **Jinja2**, utilizando herencia de plantillas base (`base.html`). |
| **Entorno**            | Configurado mediante archivo `.env` para almacenar variables sensibles (clave secreta, rutas credenciales, etc.). |

## 📁 Estructura de Carpetas del Proyecto

cilante_store/
│
├── app.py
├── config.py
├── requirements.txt
│
├── instance/
│   └── cilante.db
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

## Para la parte de IA

Asistente de bienestar hormonal personalizado

### Concepto

Un asistente que aprenda del ciclo menstrual, hábitos y síntomas de cada usuaria para ofrecer recomendaciones adaptadas: cuándo consumir Cilanté, qué cantidad y qué otros hábitos pueden acompañarlo.

### Datos a usar

- Fechas de ciclo menstrual

- Intensidad de síntomas (dolor, hinchazón, irritabilidad, etc.)

- Preferencias de sabor, temperatura o momento del día

### Resultado

Una chatbot que diga cosas como:

“Según tus últimos ciclos, te recomiendo empezar a tomar Cilanté dos días antes del inicio de tu menstruación para reducir los cólicos.”
