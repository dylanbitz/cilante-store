# Cilanté Store

Cilanté Store is a web application built with Flask that offers a unique product designed for women's wellness. The application provides users with information about the product, facilitates purchases, and offers personalized recommendations through an AI assistant.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd cilante_store
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:

     ```Powershell
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the environment variables in the `.env` file.

6. Run the application:

   ```bash
   python app.py
   ```

## Usage

- Access the application in your web browser at `http://127.0.0.1:5000`.
- Explore the product information, make purchases, and interact with the AI assistant for personalized recommendations.

## Project Structure

```
cilante_store/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── instance/
│   └── cilante.db
├── cilante/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── shop/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── admin/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── assistant/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── ml_model.py
│   │   └── utils.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── assistant.html
│   └── static/
│       ├── css/
│       │   └── main.css
│       ├── js/
│       │   └── main.js
│       └── img/
├── migrations/
│   └── versions/
└── README.md
```

## Technologies Used

- Flask (Python)
- SQLite (Database)
- SQLAlchemy (ORM)
- HTML5, CSS3, JavaScript (Frontend)
- Bootstrap/Tailwind CSS (Responsive Design)
