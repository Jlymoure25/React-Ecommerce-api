# BRAND NU U - Full-Stack E-commerce Application

A comprehensive BRAND NU U e-commerce application featuring a **React 18 frontend** with **Flask API backend** and **MySQL database**. Includes advanced product catalog, custom text hoodie designer, shopping cart with wishlist, and complete RESTful API with CRUD operations.

## 🏗️ **Full-Stack Architecture**

- **Frontend**: React 18 with custom state management
- **Backend**: Flask RESTful API with SQLAlchemy ORM
- **Database**: MySQL with relational design
- **API Testing**: Comprehensive Postman collection
- **CORS Enabled**: Frontend-backend integration ready

## 🚀 Features



## 🚀 **Frontend Features (React)**### BRAND NU U Store Features



### BRAND NU U Store Features- **Custom Text Hoodies**: Real-time custom text preview on hoodie products### Product Catalog

- **Custom Text Hoodies**: Real-time custom text preview on hoodie products

- **Advanced Product Catalog**: Complete product listing with size/color selection- **Advanced Product Catalog**: Complete product listing with size/color selection- **Product Listing**: Display all products from the FakeStore API with title, price, category, description, rating, and image

- **Professional Branding**: BRAND NU U branded interface and styling

- **Interactive Shopping Cart**: Cart with custom text support and wishlist- **Professional Branding**: BRAND NU U branded interface and styling- **Category Navigation**: Dynamic dropdown filter to view products by category

- **Real-time Image Generation**: Dynamic hoodie images with custom text using placehold.co API

- **Interactive Shopping Cart**: Cart with custom text support and wishlist- **Image Fallback**: Graceful handling of broken image URLs with placeholder images

### Product Catalog

- **Product Listing**: Display all products with title, price, category, description, rating, and image- **Real-time Image Generation**: Dynamic hoodie images with custom text using placehold.co API- **Add to Cart**: One-click add to cart functionality from the product listing

- **Category Navigation**: Dynamic dropdown filter to view products by category

- **Size & Color Selection**: Interactive size and color options for products

- **Search & Filter**: Real-time product search and category filtering

- **Sort Options**: Sort by price, name, or rating### Product Catalog### Shopping Cart



### Shopping Cart & Wishlist- **Product Listing**: Display all products with title, price, category, description, rating, and image- **State Management**: Redux Toolkit for cart state management

- **Advanced Cart Management**: Add, remove, and update product quantities with size/color tracking

- **Custom Text Support**: Save and manage custom text for personalized products- **Category Navigation**: Dynamic dropdown filter to view products by category- **Session Persistence**: Cart data persists across browser sessions using sessionStorage

- **Wishlist Functionality**: Add products to wishlist for later purchase

- **Session Persistence**: Cart and wishlist data persists across browser sessions- **Size & Color Selection**: Interactive size and color options for products- **Cart Management**: Add, remove, and update product quantities

- **Real-time Totals**: Dynamic calculation of total items and total price

- **Search & Filter**: Real-time product search and category filtering- **Real-time Totals**: Dynamic calculation of total items and total price

### Custom Text Hoodie Designer

- **Live Preview**: Real-time preview of custom text on hoodie images- **Sort Options**: Sort by price, name, or rating- **Checkout**: Simulated checkout process that clears the cart

- **Text Input**: Interactive text input with immediate visual feedback

- **Image Integration**: Seamless integration with placehold.co for dynamic image generation

- **Cart Integration**: Custom text products properly tracked in cart

### Shopping Cart & Wishlist### Technical Features

## 🔧 **Backend Features (Flask API)**

- **Advanced Cart Management**: Add, remove, and update product quantities with size/color tracking- **React Query**: Efficient data fetching with caching and background updates

### Database Models

- **User Model**: Customer information with unique email validation- **Custom Text Support**: Save and manage custom text for personalized products- **Redux Toolkit**: Modern Redux state management

- **Product Model**: E-commerce catalog with categories and pricing

- **Order Model**: Customer purchase tracking with timestamps- **Wishlist Functionality**: Add products to wishlist for later purchase- **Responsive Design**: Mobile-friendly responsive layout

- **OrderProduct Association**: Many-to-many relationship with quantity tracking

- **Session Persistence**: Cart and wishlist data persists across browser sessions- **Error Handling**: Graceful error handling for API failures

### RESTful API Endpoints

- **User CRUD**: Complete user management (GET, POST, PUT, DELETE)- **Real-time Totals**: Dynamic calculation of total items and total price- **Loading States**: Loading indicators for better user experience

- **Product CRUD**: Full product catalog management

- **Order Management**: Order creation, product addition/removal, order tracking

- **Data Validation**: Marshmallow schemas for input validation and serialization

- **Error Handling**: Comprehensive error responses and validation### Custom Text Hoodie Designer## 🛠️ Technologies Used



### Advanced Features- **Live Preview**: Real-time preview of custom text on hoodie images

- **Foreign Key Relationships**: Properly linked database tables

- **Duplicate Prevention**: Unique constraints for order-product associations- **Text Input**: Interactive text input with immediate visual feedback- **React 18**: Modern React with hooks

- **Automatic Totals**: Real-time order total calculations

- **Sample Data Seeding**: Pre-populated test data for development- **Image Integration**: Seamless integration with placehold.co for dynamic image generation- **Redux Toolkit**: State management



## 🛠️ **Technologies Used**- **Cart Integration**: Custom text products properly tracked in cart- **React Query (TanStack Query)**: Server state management



### Frontend Stack- **React Router**: Navigation and routing

- **React 18**: Modern React with hooks (useState, useReducer, useContext, useEffect)

- **React Router DOM**: Navigation and routing## 🛠️ Technologies Used- **FakeStore API**: Product data source

- **Custom State Management**: Advanced cart and wishlist state management

- **Placehold.co API**: Real-time image generation for custom text- **CSS3**: Styling and responsive design

- **CSS3**: Modern styling with flexbox and responsive design

- **React 18**: Modern React with hooks (useState, useReducer, useContext, useEffect)

### Backend Stack

- **Flask**: Lightweight Python web framework- **React Router DOM**: Navigation and routing## 📦 Installation and Setup

- **SQLAlchemy**: Python SQL toolkit and ORM

- **Flask-Marshmallow**: Object serialization/deserialization- **Custom State Management**: Advanced cart and wishlist state management

- **MySQL**: Relational database management system

- **Flask-CORS**: Cross-origin resource sharing support- **Placehold.co API**: Real-time image generation for custom text### Prerequisites



## 📦 **Installation and Setup**- **CSS3**: Modern styling with flexbox and responsive design- Node.js (v14 or higher)



### Prerequisites- **VS Code Integration**: Optimized for VS Code development environment- npm or yarn package manager

- Node.js (v14 or higher)

- Python 3.8+

- MySQL Server

- MySQL Workbench (recommended)## 📦 Installation and Setup### Installation Steps

- VS Code (recommended)



### Frontend Setup

### Prerequisites1. **Clone the repository**

1. **Navigate to the project directory**

   ```bash- Node.js (v14 or higher)   ```bash

   cd "C:\Users\customer\OneDrive\React Ecommerce"

   ```- npm package manager   git clone <your-repository-url>



2. **Install React dependencies**- VS Code (recommended)   cd react-ecommerce

   ```bash

   npm install   ```

   ```

### Installation Steps

3. **Start the React development server**

   ```bash2. **Install dependencies**

   npm start

   ```1. **Navigate to the project directory**   ```bash



4. **Open your browser**   ```bash   npm install

   Navigate to `http://localhost:3001` to view the BRAND NU U application

   cd "C:\Users\customer\OneDrive\React Ecommerce"   ```

### Backend Setup

   ```

1. **Database Setup**

   ```sql3. **Start the development server**

   CREATE DATABASE ecommerce_api;

   USE ecommerce_api;2. **Install dependencies**   ```bash

   ```

   ```bash   npm start

2. **Update MySQL connection in app.py**

   ```python   npm install   ```

   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/ecommerce_api'

   ```   ```



3. **Start the Flask API server**4. **Open your browser**

   ```bash

   "C:/Users/customer/OneDrive/React Ecommerce/.venv/Scripts/python.exe" app.py3. **Start the development server**   Navigate to `http://localhost:3000` to view the application

   ```

   ```bash

4. **Verify API is running**

   Navigate to `http://localhost:5000/` to see API information   npm start## 🎯 Available Scripts



## 📁 **Project Structure**   ```



```- `npm start`: Runs the app in development mode

React Ecommerce/

├── .gitignore                              # Git ignore file4. **Open your browser**- `npm build`: Builds the app for production

├── .venv/                                  # Python virtual environment

├── package.json                            # React dependencies and scripts   Navigate to `http://localhost:3001` to view the BRAND NU U application- `npm test`: Launches the test runner

├── requirements.txt                        # Python dependencies

├── README.md                              # Project documentation- `npm eject`: Ejects from Create React App (not recommended)

├── API_SETUP_INSTRUCTIONS.md             # Detailed API setup guide

├── config_template.py                     # Database configuration template## 📁 Project Structure

├── app.py                                 # Flask API application (500+ lines)

├── BRAND_NU_U_Ecommerce_API.postman_collection.json  # API testing collection## 📁 Project Structure

├── public/

│   └── index.html                         # HTML template with BRAND NU U branding```

└── src/

    ├── App.js                             # React app componentReact Ecommerce/```

    ├── index.css                          # Global styles

    ├── index.js                           # Main React application (1100+ lines)├── .gitignore              # Git ignore filesrc/

    ├── components/

    │   ├── Cart.js                        # Shopping cart component├── package.json            # Project dependencies and scripts├── components/           # React components

    │   ├── CategoryFilter.js              # Category filtering

    │   ├── Header.js                      # BRAND NU U header├── README.md              # Project documentation│   ├── Cart.js          # Shopping cart component

    │   ├── Home.js                        # Home page with product catalog

    │   └── ProductCard.js                 # Product display with custom text├── public/│   ├── CategoryFilter.js # Category dropdown filter

    ├── hooks/

    │   └── useProducts.js                 # Custom React hooks│   └── index.html         # HTML template with BRAND NU U branding│   ├── Header.js        # Navigation header

    ├── services/

    │   └── api.js                         # API service functions└── src/│   ├── Home.js          # Main product listing page

    └── store/

        ├── cartSlice.js                   # Cart state management    ├── App.js             # React app component│   └── ProductCard.js   # Individual product display

        └── store.js                       # Store configuration

```    ├── index.css          # Global styles├── hooks/               # Custom React hooks



## 🗃️ **Database Schema**    ├── index.js           # Main application file (1100+ lines)│   └── useProducts.js   # React Query hooks for API calls



### Users Table    ├── components/├── services/            # API service functions

- `id` (INT, Primary Key, Auto Increment)

- `name` (VARCHAR(100), Not Null)    │   ├── Cart.js        # Shopping cart component│   └── api.js          # FakeStore API integration

- `address` (VARCHAR(255), Not Null)  

- `email` (VARCHAR(120), Unique, Not Null)    │   ├── CategoryFilter.js # Category filtering├── store/              # Redux store configuration



### Products Table    │   ├── Header.js      # BRAND NU U header│   ├── cartSlice.js    # Cart state management

- `id` (INT, Primary Key, Auto Increment)

- `product_name` (VARCHAR(100), Not Null)    │   ├── Home.js        # Home page with product catalog│   └── store.js        # Redux store setup

- `price` (FLOAT, Not Null)

- `category` (VARCHAR(50))    │   └── ProductCard.js # Product display with custom text├── App.js              # Main app component

- `description` (TEXT)

- `image_url` (VARCHAR(255))    ├── hooks/├── index.js            # App entry point



### Orders Table    │   └── useProducts.js # Custom React hooks└── index.css           # Global styles

- `id` (INT, Primary Key, Auto Increment)

- `order_date` (DATETIME, Not Null)    ├── services/```

- `user_id` (INT, Foreign Key → users.id)

- `total_amount` (FLOAT, Default 0.0)    │   └── api.js         # API service functions

- `status` (VARCHAR(50), Default 'pending')

    └── store/## 🔗 API Integration

### Order_Products Association Table

- `order_id` (INT, Foreign Key → orders.id, Primary Key)        ├── cartSlice.js   # Cart state management

- `product_id` (INT, Foreign Key → products.id, Primary Key)

- `quantity` (INT, Not Null, Default 1)        └── store.js       # Store configurationThis application uses the [FakeStore API](https://fakestoreapi.com/) for product data:

- `unit_price` (FLOAT, Not Null)

- **Unique Constraint**: Prevents duplicate products in same order```



## 📋 **API Endpoints**- **All Products**: `GET /products`



### User Management## 💡 Key Features Explained- **Categories**: `GET /products/categories`

- `GET /users` - Retrieve all users

- `GET /users/<id>` - Retrieve user by ID- **Products by Category**: `GET /products/category/{category}`

- `POST /users` - Create new user

- `PUT /users/<id>` - Update user by ID### Custom Text Hoodie System

- `DELETE /users/<id>` - Delete user by ID

- **Real-time Preview**: Instant visual feedback as users type custom text## 💡 Key Features Explained

### Product Management  

- `GET /products` - Retrieve all products- **Dynamic Images**: Integration with placehold.co for generating custom hoodie images

- `GET /products/<id>` - Retrieve product by ID

- `POST /products` - Create new product- **Cart Integration**: Custom text properly saved and displayed in cart### Redux Cart Management

- `PUT /products/<id>` - Update product by ID

- `DELETE /products/<id>` - Delete product by ID- **Size/Color Tracking**: Custom products tracked with size and color selections- **Add to Cart**: Products are added with quantity tracking



### Order Management- **Remove Items**: Complete removal of products from cart

- `POST /orders` - Create new order

- `PUT /orders/<order_id>/add_product/<product_id>` - Add product to order### Advanced Cart Management- **Update Quantities**: Modify item quantities with validation

- `DELETE /orders/<order_id>/remove_product/<product_id>` - Remove product from order

- `GET /orders/user/<user_id>` - Get all orders for a user- **Multi-attribute Tracking**: Products tracked by ID, size, color, and custom text- **Session Persistence**: Cart data survives browser refreshes

- `GET /orders/<order_id>/products` - Get all products for an order

- **Wishlist Integration**: Separate wishlist functionality alongside cart

## 🧪 **Testing**

- **Session Persistence**: Data persists across browser sessions### React Query Data Fetching

### Postman Collection

- **Import**: `BRAND_NU_U_Ecommerce_API.postman_collection.json`- **Complex State Logic**: Handles multiple product variations and custom text- **Caching**: Automatic caching of API responses

- **50+ Test Cases**: Complete API endpoint testing

- **Error Testing**: Validation and error handling verification- **Background Updates**: Fresh data fetching in the background

- **Integration Tests**: Full workflow testing

### BRAND NU U Branding- **Error Handling**: Robust error handling for network issues

### Test Categories

1. **User CRUD Operations** - All user management functions- **Professional Header**: Centered BRAND NU U title with proper spacing- **Loading States**: Proper loading indicators during data fetching

2. **Product CRUD Operations** - All product management functions  

3. **Order Management** - Order creation and product handling- **Branded Metadata**: HTML meta tags optimized for BRAND NU U

4. **Error Handling** - Validation and edge cases

5. **Integration Workflows** - Complete user journey testing- **Consistent Styling**: Brand-consistent color scheme and layout### Image Fallback System



## 💡 **Key Features Explained**- **Mobile Responsive**: Optimized for all device sizesDue to occasional 404 errors from the FakeStore API images, the application includes:



### Custom Text Hoodie System- Automatic detection of broken images

- **Real-time Preview**: Instant visual feedback as users type custom text

- **Dynamic Images**: Integration with placehold.co for generating custom hoodie images## 🎨 Styling & Design- Fallback to placeholder images

- **Cart Integration**: Custom text properly saved and displayed in cart

- **Size/Color Tracking**: Custom products tracked with size and color selections- Consistent UI experience regardless of image availability



### Advanced Cart ManagementThe application features:

- **Multi-attribute Tracking**: Products tracked by ID, size, color, and custom text

- **Wishlist Integration**: Separate wishlist functionality alongside cart- **BRAND NU U Branding**: Professional branded interface## 🎨 Styling

- **Session Persistence**: Data persists across browser sessions

- **Complex State Logic**: Handles multiple product variations and custom text- **Modern Layout**: Clean, responsive design with flexbox



### Database Relations- **Interactive Elements**: Hover effects and visual feedbackThe application features:

- **Foreign Keys**: Proper relationships between users, orders, and products

- **Association Tables**: Many-to-many relationships with additional attributes- **Mobile-First**: Responsive design that works on all devices- **Modern Design**: Clean, professional appearance

- **Cascade Operations**: Automatic cleanup of related records

- **Unique Constraints**: Data integrity enforcement- **Custom Components**: Styled React components for consistent UI- **Responsive Layout**: Works on desktop, tablet, and mobile



## 🎨 **Styling & Design**- **CSS Grid**: Product grid layout that adapts to screen size



### Frontend Design## 🚀 GitHub Repository- **Interactive Elements**: Hover effects and visual feedback

- **BRAND NU U Branding**: Professional branded interface

- **Modern Layout**: Clean, responsive design with flexbox

- **Interactive Elements**: Hover effects and visual feedback

- **Mobile-First**: Responsive design that works on all devicesThis project is ready for GitHub deployment:## 🚀 Deployment



### API Design- **Clean Structure**: Organized file structure with proper .gitignore

- **RESTful Architecture**: Standard HTTP methods and status codes

- **JSON Responses**: Consistent data format- **Documentation**: Comprehensive README with setup instructionsTo deploy this application:

- **Error Handling**: Descriptive error messages

- **Data Validation**: Input validation and sanitization- **Version Control**: Git-ready with proper commit history



## 🚀 **Full-Stack Integration**- **Dependencies**: All dependencies properly listed in package.json1. **Build the production version**



### Frontend-Backend Connection   ```bash

- **CORS Enabled**: Cross-origin requests supported

- **API Integration Points**: Ready for React service integration---   npm run build

- **Data Flow**: Seamless data exchange between frontend and backend

- **Development Servers**: React (3001) + Flask (5000)   ```



### Production Readiness**Welcome to BRAND NU U - Your Premium Online Store! 🛍️**

- **Environment Configuration**: Separate dev/prod configs2. **Deploy the `build` folder** to your hosting service (Netlify, Vercel, GitHub Pages, etc.)

- **Database Migrations**: SQLAlchemy table creation

- **Error Handling**: Comprehensive error management## 🤝 Contributing

- **Security Features**: Input validation and SQL injection prevention

1. Fork the repository

## 📈 **GitHub Repository**2. Create a feature branch (`git checkout -b feature/AmazingFeature`)

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

This complete full-stack project includes:4. Push to the branch (`git push origin feature/AmazingFeature`)

- **Clean Structure**: Organized file structure with proper .gitignore5. Open a Pull Request

- **Comprehensive Documentation**: Setup guides and API documentation  

- **Version Control**: Git-ready with proper commit history## 📝 License

- **Dependencies Management**: Package.json and requirements.txt

- **Testing Resources**: Postman collection and sample dataThis project is open source and available under the [MIT License](LICENSE).



---## 🙏 Acknowledgments



**Welcome to BRAND NU U - Your Complete Full-Stack E-commerce Solution! 🛍️🚀**- [FakeStore API](https://fakestoreapi.com/) for providing the product data

- [React](https://reactjs.org/) for the amazing framework

*Frontend: React 18 | Backend: Flask + MySQL | API: RESTful with CRUD | Testing: Postman Collection*- [Redux Toolkit](https://redux-toolkit.js.org/) for state management
- [TanStack Query](https://tanstack.com/query) for data fetching

---

**Enjoy building your e-commerce store! 🛍️**
