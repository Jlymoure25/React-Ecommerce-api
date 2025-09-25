# BRAND NU U E-commerce API Setup Instructions

## 🗃️ Database Setup (MySQL)

### Step 1: Install MySQL
1. Download and install MySQL Server from https://dev.mysql.com/downloads/mysql/
2. Download and install MySQL Workbench from https://dev.mysql.com/downloads/workbench/

### Step 2: Create Database
1. Open MySQL Workbench
2. Connect to your MySQL server (usually `localhost:3306`)
3. Create a new database:
```sql
CREATE DATABASE ecommerce_api;
USE ecommerce_api;
```

### Step 3: Configure Database Connection
1. Copy `config_template.py` to `config.py`
2. Update the MySQL password in the `app.py` file:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/ecommerce_api'
```
Replace `YOUR_PASSWORD` with your actual MySQL root password.

## 🐍 Python Environment Setup

### Step 1: Virtual Environment (Already Created)
The virtual environment is already set up in `.venv` folder.

### Step 2: Dependencies (Already Installed)
All required packages are installed:
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- marshmallow-sqlalchemy
- mysql-connector-python
- flask-cors

## 🚀 Running the API

### Step 1: Start the Flask Application
```bash
# In PowerShell/Terminal, from the React Ecommerce directory:
"C:/Users/customer/OneDrive/React Ecommerce/.venv/Scripts/python.exe" app.py
```

### Step 2: Verify Database Tables
The application will automatically:
1. Create all database tables
2. Seed sample data (users and products)
3. Start the API server on http://localhost:5000

### Step 3: Test API Endpoints
1. Visit http://localhost:5000/ to see API information
2. Use the Postman collection: `BRAND_NU_U_Ecommerce_API.postman_collection.json`

## 📋 API Endpoints

### Users
- `GET /users` - Get all users
- `GET /users/<id>` - Get user by ID
- `POST /users` - Create new user
- `PUT /users/<id>` - Update user
- `DELETE /users/<id>` - Delete user

### Products
- `GET /products` - Get all products
- `GET /products/<id>` - Get product by ID
- `POST /products` - Create new product
- `PUT /products/<id>` - Update product
- `DELETE /products/<id>` - Delete product

### Orders
- `POST /orders` - Create new order
- `PUT /orders/<order_id>/add_product/<product_id>` - Add product to order
- `DELETE /orders/<order_id>/remove_product/<product_id>` - Remove product from order
- `GET /orders/user/<user_id>` - Get user's orders
- `GET /orders/<order_id>/products` - Get order's products

## 🧪 Testing with Postman

### Import Collection
1. Open Postman
2. Click "Import"
3. Select file: `BRAND_NU_U_Ecommerce_API.postman_collection.json`
4. The collection will be imported with all test cases

### Test Categories
1. **Basic CRUD Operations** - Test all user and product operations
2. **Order Management** - Test order creation and product management
3. **Error Handling** - Test validation and error responses
4. **Integration Tests** - Complete workflow testing

### Sample Test Flow
1. Create a user
2. Create products
3. Create an order for the user
4. Add products to the order
5. Verify order contents
6. Remove products from order
7. Clean up test data

## 📊 Database Schema

### Users Table
- `id` (INT, Primary Key, Auto Increment)
- `name` (VARCHAR(100), Not Null)
- `address` (VARCHAR(255), Not Null)
- `email` (VARCHAR(120), Unique, Not Null)

### Products Table
- `id` (INT, Primary Key, Auto Increment)
- `product_name` (VARCHAR(100), Not Null)
- `price` (FLOAT, Not Null)
- `category` (VARCHAR(50))
- `description` (TEXT)
- `image_url` (VARCHAR(255))

### Orders Table
- `id` (INT, Primary Key, Auto Increment)
- `order_date` (DATETIME, Not Null)
- `user_id` (INT, Foreign Key → users.id)
- `total_amount` (FLOAT, Default 0.0)
- `status` (VARCHAR(50), Default 'pending')

### Order_Products Association Table
- `order_id` (INT, Foreign Key → orders.id, Primary Key)
- `product_id` (INT, Foreign Key → products.id, Primary Key)
- `quantity` (INT, Not Null, Default 1)
- `unit_price` (FLOAT, Not Null)

## 🔧 Troubleshooting

### MySQL Connection Issues
1. Verify MySQL service is running
2. Check username/password in connection string
3. Ensure database `ecommerce_api` exists
4. Verify MySQL port (default: 3306)

### Import Errors
1. Ensure virtual environment is activated
2. Reinstall packages if needed:
```bash
"C:/Users/customer/OneDrive/React Ecommerce/.venv/Scripts/pip.exe" install -r requirements.txt
```

### Port Conflicts
If port 5000 is in use, change in app.py:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## 🎯 Integration with React Frontend

The API is configured with CORS to work with your React application:
- React runs on: http://localhost:3001
- API runs on: http://localhost:5000
- Cross-origin requests are enabled

### Example React API Calls
```javascript
// Get all products
const response = await fetch('http://localhost:5000/products');
const products = await response.json();

// Create new user
const userData = {
    name: "John Doe",
    address: "123 Main St",
    email: "john@example.com"
};

const response = await fetch('http://localhost:5000/users', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(userData)
});
```

## ✅ Success Verification

After setup, you should see:
1. ✅ Flask server running on http://localhost:5000
2. ✅ Database tables created in MySQL
3. ✅ Sample data populated
4. ✅ All Postman tests passing
5. ✅ API responding to requests

Your BRAND NU U E-commerce API is now ready for production use! 🚀