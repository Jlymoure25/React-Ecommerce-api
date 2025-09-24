# React E-commerce Store

A modern e-commerce application built with React, Redux Toolkit, and React Query, featuring a product catalog, shopping cart, and checkout functionality.

## 🚀 Features

### Product Catalog
- **Product Listing**: Display all products from the FakeStore API with title, price, category, description, rating, and image
- **Category Navigation**: Dynamic dropdown filter to view products by category
- **Image Fallback**: Graceful handling of broken image URLs with placeholder images
- **Add to Cart**: One-click add to cart functionality from the product listing

### Shopping Cart
- **State Management**: Redux Toolkit for cart state management
- **Session Persistence**: Cart data persists across browser sessions using sessionStorage
- **Cart Management**: Add, remove, and update product quantities
- **Real-time Totals**: Dynamic calculation of total items and total price
- **Checkout**: Simulated checkout process that clears the cart

### Technical Features
- **React Query**: Efficient data fetching with caching and background updates
- **Redux Toolkit**: Modern Redux state management
- **Responsive Design**: Mobile-friendly responsive layout
- **Error Handling**: Graceful error handling for API failures
- **Loading States**: Loading indicators for better user experience

## 🛠️ Technologies Used

- **React 18**: Modern React with hooks
- **Redux Toolkit**: State management
- **React Query (TanStack Query)**: Server state management
- **React Router**: Navigation and routing
- **FakeStore API**: Product data source
- **CSS3**: Styling and responsive design

## 📦 Installation and Setup

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd react-ecommerce
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm start
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000` to view the application

## 🎯 Available Scripts

- `npm start`: Runs the app in development mode
- `npm build`: Builds the app for production
- `npm test`: Launches the test runner
- `npm eject`: Ejects from Create React App (not recommended)

## 📁 Project Structure

```
src/
├── components/           # React components
│   ├── Cart.js          # Shopping cart component
│   ├── CategoryFilter.js # Category dropdown filter
│   ├── Header.js        # Navigation header
│   ├── Home.js          # Main product listing page
│   └── ProductCard.js   # Individual product display
├── hooks/               # Custom React hooks
│   └── useProducts.js   # React Query hooks for API calls
├── services/            # API service functions
│   └── api.js          # FakeStore API integration
├── store/              # Redux store configuration
│   ├── cartSlice.js    # Cart state management
│   └── store.js        # Redux store setup
├── App.js              # Main app component
├── index.js            # App entry point
└── index.css           # Global styles
```

## 🔗 API Integration

This application uses the [FakeStore API](https://fakestoreapi.com/) for product data:

- **All Products**: `GET /products`
- **Categories**: `GET /products/categories`
- **Products by Category**: `GET /products/category/{category}`

## 💡 Key Features Explained

### Redux Cart Management
- **Add to Cart**: Products are added with quantity tracking
- **Remove Items**: Complete removal of products from cart
- **Update Quantities**: Modify item quantities with validation
- **Session Persistence**: Cart data survives browser refreshes

### React Query Data Fetching
- **Caching**: Automatic caching of API responses
- **Background Updates**: Fresh data fetching in the background
- **Error Handling**: Robust error handling for network issues
- **Loading States**: Proper loading indicators during data fetching

### Image Fallback System
Due to occasional 404 errors from the FakeStore API images, the application includes:
- Automatic detection of broken images
- Fallback to placeholder images
- Consistent UI experience regardless of image availability

## 🎨 Styling

The application features:
- **Modern Design**: Clean, professional appearance
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **CSS Grid**: Product grid layout that adapts to screen size
- **Interactive Elements**: Hover effects and visual feedback

## 🚀 Deployment

To deploy this application:

1. **Build the production version**
   ```bash
   npm run build
   ```

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