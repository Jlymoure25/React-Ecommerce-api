"""
BRAND NU U E-commerce API
Flask backend API for React E-commerce application with MySQL database
Features: User management, Product catalog, Order processing with association tables
Author: BRAND NU U Development Team
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from datetime import datetime
from sqlalchemy import UniqueConstraint

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Database Configuration
# UPDATE THIS WITH YOUR MYSQL PASSWORD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/ecommerce_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)

# =============================================================================
# DATABASE MODELS
# =============================================================================

class User(db.Model):
    """User model for customer information"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Relationship to orders
    orders = db.relationship('Order', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.name}>'

class Product(db.Model):
    """Product model for e-commerce catalog"""
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f'<Product {self.product_name}>'

class Order(db.Model):
    """Order model for customer purchases"""
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(50), default='pending')
    
    # Relationship to order_products
    order_products = db.relationship('OrderProduct', backref='order', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Order {self.id} - User {self.user_id}>'

class OrderProduct(db.Model):
    """Association table for Order-Product many-to-many relationship"""
    __tablename__ = 'order_products'
    
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer, default=1, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    
    # Unique constraint to prevent duplicate products in same order
    __table_args__ = (UniqueConstraint('order_id', 'product_id', name='unique_order_product'),)
    
    # Relationships
    product = db.relationship('Product', backref='order_products')
    
    def __repr__(self):
        return f'<OrderProduct Order:{self.order_id} Product:{self.product_id}>'

# =============================================================================
# MARSHMALLOW SCHEMAS
# =============================================================================

class UserSchema(ma.SQLAlchemyAutoSchema):
    """Schema for User serialization and validation"""
    class Meta:
        model = User
        include_fk = True
        load_instance = True
    
    # Validation
    email = ma.Email(required=True)
    name = ma.Str(required=True, validate=ma.validate.Length(min=1, max=100))
    address = ma.Str(required=True, validate=ma.validate.Length(min=1, max=255))

class ProductSchema(ma.SQLAlchemyAutoSchema):
    """Schema for Product serialization and validation"""
    class Meta:
        model = Product
        include_fk = True
        load_instance = True
    
    # Validation
    product_name = ma.Str(required=True, validate=ma.validate.Length(min=1, max=100))
    price = ma.Float(required=True, validate=ma.validate.Range(min=0))

class OrderProductSchema(ma.SQLAlchemyAutoSchema):
    """Schema for OrderProduct serialization"""
    class Meta:
        model = OrderProduct
        include_fk = True
        load_instance = True
    
    # Include product details
    product = ma.Nested(ProductSchema, exclude=['order_products'])

class OrderSchema(ma.SQLAlchemyAutoSchema):
    """Schema for Order serialization and validation"""
    class Meta:
        model = Order
        include_fk = True
        load_instance = True
    
    # Include user and products
    user = ma.Nested(UserSchema, exclude=['orders'])
    order_products = ma.Nested(OrderProductSchema, many=True, exclude=['order'])

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
order_product_schema = OrderProductSchema()

# =============================================================================
# USER ENDPOINTS
# =============================================================================

@app.route('/users', methods=['GET'])
def get_all_users():
    """GET /users: Retrieve all users"""
    try:
        users = User.query.all()
        return users_schema.jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """GET /users/<id>: Retrieve a user by ID"""
    try:
        user = User.query.get_or_404(user_id)
        return user_schema.jsonify(user), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/users', methods=['POST'])
def create_user():
    """POST /users: Create a new user"""
    try:
        # Validate and deserialize input
        user_data = user_schema.load(request.json)
        
        # Check if email already exists
        existing_user = User.query.filter_by(email=user_data.email).first()
        if existing_user:
            return jsonify({'error': 'Email already exists'}), 400
        
        # Create new user
        new_user = User(
            name=user_data.name,
            address=user_data.address,
            email=user_data.email
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return user_schema.jsonify(new_user), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """PUT /users/<id>: Update a user by ID"""
    try:
        user = User.query.get_or_404(user_id)
        user_data = user_schema.load(request.json, partial=True)
        
        # Update fields
        if hasattr(user_data, 'name'):
            user.name = user_data.name
        if hasattr(user_data, 'address'):
            user.address = user_data.address
        if hasattr(user_data, 'email'):
            # Check if new email already exists (excluding current user)
            existing_user = User.query.filter(User.email == user_data.email, User.id != user_id).first()
            if existing_user:
                return jsonify({'error': 'Email already exists'}), 400
            user.email = user_data.email
        
        db.session.commit()
        return user_schema.jsonify(user), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """DELETE /users/<id>: Delete a user by ID"""
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'User {user_id} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# =============================================================================
# PRODUCT ENDPOINTS
# =============================================================================

@app.route('/products', methods=['GET'])
def get_all_products():
    """GET /products: Retrieve all products"""
    try:
        products = Product.query.all()
        return products_schema.jsonify(products), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """GET /products/<id>: Retrieve a product by ID"""
    try:
        product = Product.query.get_or_404(product_id)
        return product_schema.jsonify(product), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/products', methods=['POST'])
def create_product():
    """POST /products: Create a new product"""
    try:
        product_data = product_schema.load(request.json)
        
        new_product = Product(
            product_name=product_data.product_name,
            price=product_data.price,
            category=getattr(product_data, 'category', None),
            description=getattr(product_data, 'description', None),
            image_url=getattr(product_data, 'image_url', None)
        )
        
        db.session.add(new_product)
        db.session.commit()
        
        return product_schema.jsonify(new_product), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """PUT /products/<id>: Update a product by ID"""
    try:
        product = Product.query.get_or_404(product_id)
        product_data = product_schema.load(request.json, partial=True)
        
        # Update fields
        if hasattr(product_data, 'product_name'):
            product.product_name = product_data.product_name
        if hasattr(product_data, 'price'):
            product.price = product_data.price
        if hasattr(product_data, 'category'):
            product.category = product_data.category
        if hasattr(product_data, 'description'):
            product.description = product_data.description
        if hasattr(product_data, 'image_url'):
            product.image_url = product_data.image_url
        
        db.session.commit()
        return product_schema.jsonify(product), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """DELETE /products/<id>: Delete a product by ID"""
    try:
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': f'Product {product_id} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# =============================================================================
# ORDER ENDPOINTS
# =============================================================================

@app.route('/orders', methods=['POST'])
def create_order():
    """POST /orders: Create a new order (requires user ID and order date)"""
    try:
        data = request.json
        user_id = data.get('user_id')
        order_date = data.get('order_date')
        
        if not user_id:
            return jsonify({'error': 'user_id is required'}), 400
        
        # Verify user exists
        user = User.query.get_or_404(user_id)
        
        # Parse order_date if provided, otherwise use current time
        if order_date:
            order_date = datetime.fromisoformat(order_date.replace('Z', '+00:00'))
        else:
            order_date = datetime.utcnow()
        
        new_order = Order(
            user_id=user_id,
            order_date=order_date,
            status=data.get('status', 'pending')
        )
        
        db.session.add(new_order)
        db.session.commit()
        
        return order_schema.jsonify(new_order), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product_to_order(order_id, product_id):
    """PUT /orders/<order_id>/add_product/<product_id>: Add a product to an order (prevent duplicates)"""
    try:
        # Verify order and product exist
        order = Order.query.get_or_404(order_id)
        product = Product.query.get_or_404(product_id)
        
        # Check if product already exists in order
        existing_order_product = OrderProduct.query.filter_by(
            order_id=order_id, 
            product_id=product_id
        ).first()
        
        if existing_order_product:
            return jsonify({'error': 'Product already exists in this order'}), 400
        
        # Get quantity from request body
        data = request.json or {}
        quantity = data.get('quantity', 1)
        
        if quantity <= 0:
            return jsonify({'error': 'Quantity must be greater than 0'}), 400
        
        # Create new order-product association
        order_product = OrderProduct(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            unit_price=product.price
        )
        
        db.session.add(order_product)
        
        # Update order total
        order.total_amount = (order.total_amount or 0) + (product.price * quantity)
        
        db.session.commit()
        
        return order_product_schema.jsonify(order_product), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    """DELETE /orders/<order_id>/remove_product/<product_id>: Remove a product from an order"""
    try:
        # Find the order-product association
        order_product = OrderProduct.query.filter_by(
            order_id=order_id, 
            product_id=product_id
        ).first_or_404()
        
        # Update order total
        order = Order.query.get(order_id)
        order.total_amount = (order.total_amount or 0) - (order_product.unit_price * order_product.quantity)
        
        # Remove the association
        db.session.delete(order_product)
        db.session.commit()
        
        return jsonify({'message': f'Product {product_id} removed from order {order_id}'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id):
    """GET /orders/user/<user_id>: Get all orders for a user"""
    try:
        # Verify user exists
        user = User.query.get_or_404(user_id)
        
        # Get all orders for the user
        orders = Order.query.filter_by(user_id=user_id).all()
        
        return orders_schema.jsonify(orders), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/orders/<int:order_id>/products', methods=['GET'])
def get_products_by_order(order_id):
    """GET /orders/<order_id>/products: Get all products for an order"""
    try:
        # Verify order exists
        order = Order.query.get_or_404(order_id)
        
        # Get all products for the order
        order_products = OrderProduct.query.filter_by(order_id=order_id).all()
        
        return jsonify([{
            'product_id': op.product_id,
            'product_name': op.product.product_name,
            'quantity': op.quantity,
            'unit_price': op.unit_price,
            'total_price': op.unit_price * op.quantity
        } for op in order_products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# =============================================================================
# DATABASE INITIALIZATION
# =============================================================================

def init_db():
    """Initialize database and create all tables"""
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully!")

def seed_sample_data():
    """Add sample data for testing"""
    with app.app_context():
        # Check if data already exists
        if User.query.first():
            print("📦 Sample data already exists, skipping seed...")
            return
        
        # Create sample users
        users = [
            User(name="John Doe", address="123 Main St, Anytown, USA", email="john.doe@email.com"),
            User(name="Jane Smith", address="456 Oak Ave, Springfield, USA", email="jane.smith@email.com"),
            User(name="Mike Johnson", address="789 Pine St, Riverside, USA", email="mike.johnson@email.com")
        ]
        
        # Create sample products
        products = [
            Product(product_name="Custom Text Hoodie", price=59.99, category="Clothing", 
                   description="High-quality hoodie with custom text printing"),
            Product(product_name="BRAND NU U T-Shirt", price=29.99, category="Clothing", 
                   description="Premium cotton t-shirt with BRAND NU U logo"),
            Product(product_name="Designer Cap", price=24.99, category="Accessories", 
                   description="Stylish cap with embroidered logo"),
            Product(product_name="Athletic Shorts", price=34.99, category="Clothing", 
                   description="Comfortable athletic shorts for active lifestyle")
        ]
        
        # Add to database
        for user in users:
            db.session.add(user)
        for product in products:
            db.session.add(product)
        
        db.session.commit()
        print("🌱 Sample data seeded successfully!")

# =============================================================================
# API INFO ENDPOINT
# =============================================================================

@app.route('/', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        'message': 'BRAND NU U E-commerce API',
        'version': '1.0.0',
        'endpoints': {
            'users': '/users (GET, POST)',
            'user_detail': '/users/<id> (GET, PUT, DELETE)',
            'products': '/products (GET, POST)',
            'product_detail': '/products/<id> (GET, PUT, DELETE)',
            'create_order': '/orders (POST)',
            'add_product_to_order': '/orders/<order_id>/add_product/<product_id> (PUT)',
            'remove_product_from_order': '/orders/<order_id>/remove_product/<product_id> (DELETE)',
            'user_orders': '/orders/user/<user_id> (GET)',
            'order_products': '/orders/<order_id>/products (GET)'
        }
    }), 200

# =============================================================================
# APPLICATION RUNNER
# =============================================================================

if __name__ == '__main__':
    # Initialize database
    init_db()
    
    # Seed sample data
    seed_sample_data()
    
    # Run the Flask application
    print("🚀 Starting BRAND NU U E-commerce API...")
    print("📱 API running at: http://localhost:5000")
    print("📋 API endpoints available at: http://localhost:5000/")
    
    app.run(debug=True, host='0.0.0.0', port=5000)