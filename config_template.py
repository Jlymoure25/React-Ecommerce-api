# BRAND NU U E-commerce API Configuration
# Copy this file to config.py and update with your MySQL credentials

# Database Configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_MYSQL_PASSWORD_HERE',  # Update this with your MySQL password
    'database': 'ecommerce_api'
}

# Flask Configuration
FLASK_CONFIG = {
    'SECRET_KEY': 'brand-nu-u-secret-key-change-in-production',
    'DEBUG': True,
    'HOST': '0.0.0.0',
    'PORT': 5000
}

# CORS Configuration (for React frontend)
CORS_CONFIG = {
    'origins': ['http://localhost:3000', 'http://localhost:3001'],
    'methods': ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    'allow_headers': ['Content-Type', 'Authorization']
}