# BRAND NU U - React E-commerce Store<<<<<<< HEAD

# React E-commerce Store

A modern BRAND NU U e-commerce application built with React 18, featuring a comprehensive product catalog, advanced shopping cart with custom text functionality, and real-time hoodie customization.

A modern e-commerce application built with React, Redux Toolkit, and React Query, featuring a product catalog, shopping cart, and checkout functionality.

## 🚀 Features

## 🚀 Features

### BRAND NU U Store Features

- **Custom Text Hoodies**: Real-time custom text preview on hoodie products### Product Catalog

- **Advanced Product Catalog**: Complete product listing with size/color selection- **Product Listing**: Display all products from the FakeStore API with title, price, category, description, rating, and image

- **Professional Branding**: BRAND NU U branded interface and styling- **Category Navigation**: Dynamic dropdown filter to view products by category

- **Interactive Shopping Cart**: Cart with custom text support and wishlist- **Image Fallback**: Graceful handling of broken image URLs with placeholder images

- **Real-time Image Generation**: Dynamic hoodie images with custom text using placehold.co API- **Add to Cart**: One-click add to cart functionality from the product listing



### Product Catalog### Shopping Cart

- **Product Listing**: Display all products with title, price, category, description, rating, and image- **State Management**: Redux Toolkit for cart state management

- **Category Navigation**: Dynamic dropdown filter to view products by category- **Session Persistence**: Cart data persists across browser sessions using sessionStorage

- **Size & Color Selection**: Interactive size and color options for products- **Cart Management**: Add, remove, and update product quantities

- **Search & Filter**: Real-time product search and category filtering- **Real-time Totals**: Dynamic calculation of total items and total price

- **Sort Options**: Sort by price, name, or rating- **Checkout**: Simulated checkout process that clears the cart



### Shopping Cart & Wishlist### Technical Features

- **Advanced Cart Management**: Add, remove, and update product quantities with size/color tracking- **React Query**: Efficient data fetching with caching and background updates

- **Custom Text Support**: Save and manage custom text for personalized products- **Redux Toolkit**: Modern Redux state management

- **Wishlist Functionality**: Add products to wishlist for later purchase- **Responsive Design**: Mobile-friendly responsive layout

- **Session Persistence**: Cart and wishlist data persists across browser sessions- **Error Handling**: Graceful error handling for API failures

- **Real-time Totals**: Dynamic calculation of total items and total price- **Loading States**: Loading indicators for better user experience



### Custom Text Hoodie Designer## 🛠️ Technologies Used

- **Live Preview**: Real-time preview of custom text on hoodie images

- **Text Input**: Interactive text input with immediate visual feedback- **React 18**: Modern React with hooks

- **Image Integration**: Seamless integration with placehold.co for dynamic image generation- **Redux Toolkit**: State management

- **Cart Integration**: Custom text products properly tracked in cart- **React Query (TanStack Query)**: Server state management

- **React Router**: Navigation and routing

## 🛠️ Technologies Used- **FakeStore API**: Product data source

- **CSS3**: Styling and responsive design

- **React 18**: Modern React with hooks (useState, useReducer, useContext, useEffect)

- **React Router DOM**: Navigation and routing## 📦 Installation and Setup

- **Custom State Management**: Advanced cart and wishlist state management

- **Placehold.co API**: Real-time image generation for custom text### Prerequisites

- **CSS3**: Modern styling with flexbox and responsive design- Node.js (v14 or higher)

- **VS Code Integration**: Optimized for VS Code development environment- npm or yarn package manager



## 📦 Installation and Setup### Installation Steps



### Prerequisites1. **Clone the repository**

- Node.js (v14 or higher)   ```bash

- npm package manager   git clone <your-repository-url>

- VS Code (recommended)   cd react-ecommerce

   ```

### Installation Steps

2. **Install dependencies**

1. **Navigate to the project directory**   ```bash

   ```bash   npm install

   cd "C:\Users\customer\OneDrive\React Ecommerce"   ```

   ```

3. **Start the development server**

2. **Install dependencies**   ```bash

   ```bash   npm start

   npm install   ```

   ```

4. **Open your browser**

3. **Start the development server**   Navigate to `http://localhost:3000` to view the application

   ```bash

   npm start## 🎯 Available Scripts

   ```

- `npm start`: Runs the app in development mode

4. **Open your browser**- `npm build`: Builds the app for production

   Navigate to `http://localhost:3001` to view the BRAND NU U application- `npm test`: Launches the test runner

- `npm eject`: Ejects from Create React App (not recommended)

## 📁 Project Structure

## 📁 Project Structure

```

React Ecommerce/```

├── .gitignore              # Git ignore filesrc/

├── package.json            # Project dependencies and scripts├── components/           # React components

├── README.md              # Project documentation│   ├── Cart.js          # Shopping cart component

├── public/│   ├── CategoryFilter.js # Category dropdown filter

│   └── index.html         # HTML template with BRAND NU U branding│   ├── Header.js        # Navigation header

└── src/│   ├── Home.js          # Main product listing page

    ├── App.js             # React app component│   └── ProductCard.js   # Individual product display

    ├── index.css          # Global styles├── hooks/               # Custom React hooks

    ├── index.js           # Main application file (1100+ lines)│   └── useProducts.js   # React Query hooks for API calls

    ├── components/├── services/            # API service functions

    │   ├── Cart.js        # Shopping cart component│   └── api.js          # FakeStore API integration

    │   ├── CategoryFilter.js # Category filtering├── store/              # Redux store configuration

    │   ├── Header.js      # BRAND NU U header│   ├── cartSlice.js    # Cart state management

    │   ├── Home.js        # Home page with product catalog│   └── store.js        # Redux store setup

    │   └── ProductCard.js # Product display with custom text├── App.js              # Main app component

    ├── hooks/├── index.js            # App entry point

    │   └── useProducts.js # Custom React hooks└── index.css           # Global styles

    ├── services/```

    │   └── api.js         # API service functions

    └── store/## 🔗 API Integration

        ├── cartSlice.js   # Cart state management

        └── store.js       # Store configurationThis application uses the [FakeStore API](https://fakestoreapi.com/) for product data:

```

- **All Products**: `GET /products`

## 💡 Key Features Explained- **Categories**: `GET /products/categories`

- **Products by Category**: `GET /products/category/{category}`

### Custom Text Hoodie System

- **Real-time Preview**: Instant visual feedback as users type custom text## 💡 Key Features Explained

- **Dynamic Images**: Integration with placehold.co for generating custom hoodie images

- **Cart Integration**: Custom text properly saved and displayed in cart### Redux Cart Management

- **Size/Color Tracking**: Custom products tracked with size and color selections- **Add to Cart**: Products are added with quantity tracking

- **Remove Items**: Complete removal of products from cart

### Advanced Cart Management- **Update Quantities**: Modify item quantities with validation

- **Multi-attribute Tracking**: Products tracked by ID, size, color, and custom text- **Session Persistence**: Cart data survives browser refreshes

- **Wishlist Integration**: Separate wishlist functionality alongside cart

- **Session Persistence**: Data persists across browser sessions### React Query Data Fetching

- **Complex State Logic**: Handles multiple product variations and custom text- **Caching**: Automatic caching of API responses

- **Background Updates**: Fresh data fetching in the background

### BRAND NU U Branding- **Error Handling**: Robust error handling for network issues

- **Professional Header**: Centered BRAND NU U title with proper spacing- **Loading States**: Proper loading indicators during data fetching

- **Branded Metadata**: HTML meta tags optimized for BRAND NU U

- **Consistent Styling**: Brand-consistent color scheme and layout### Image Fallback System

- **Mobile Responsive**: Optimized for all device sizesDue to occasional 404 errors from the FakeStore API images, the application includes:

- Automatic detection of broken images

## 🎨 Styling & Design- Fallback to placeholder images

- Consistent UI experience regardless of image availability

The application features:

- **BRAND NU U Branding**: Professional branded interface## 🎨 Styling

- **Modern Layout**: Clean, responsive design with flexbox

- **Interactive Elements**: Hover effects and visual feedbackThe application features:

- **Mobile-First**: Responsive design that works on all devices- **Modern Design**: Clean, professional appearance

- **Custom Components**: Styled React components for consistent UI- **Responsive Layout**: Works on desktop, tablet, and mobile

- **CSS Grid**: Product grid layout that adapts to screen size

## 🚀 GitHub Repository- **Interactive Elements**: Hover effects and visual feedback



This project is ready for GitHub deployment:## 🚀 Deployment

- **Clean Structure**: Organized file structure with proper .gitignore

- **Documentation**: Comprehensive README with setup instructionsTo deploy this application:

- **Version Control**: Git-ready with proper commit history

- **Dependencies**: All dependencies properly listed in package.json1. **Build the production version**

   ```bash

---   npm run build

   ```

**Welcome to BRAND NU U - Your Premium Online Store! 🛍️**
2. **Deploy the `build` folder** to your hosting service (Netlify, Vercel, GitHub Pages, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [FakeStore API](https://fakestoreapi.com/) for providing the product data
- [React](https://reactjs.org/) for the amazing framework
- [Redux Toolkit](https://redux-toolkit.js.org/) for state management
- [TanStack Query](https://tanstack.com/query) for data fetching

---

**Enjoy building your e-commerce store! 🛍️**
=======
# React-Ecommerce-api
ecommerce  api site
>>>>>>> b32df5415d3b2fc51d940119da6793146e1a9d0f
