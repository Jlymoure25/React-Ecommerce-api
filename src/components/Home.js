import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useProducts, useProductsByCategory, useCategories } from '../hooks/useProducts';
import { addToCart } from '../store/cartSlice';
import ProductCard from '../components/ProductCard';
import CategoryFilter from '../components/CategoryFilter';

const Home = () => {
  const [selectedCategory, setSelectedCategory] = useState('all');
  const dispatch = useDispatch();

  // Fetch data using React Query hooks
  const { data: allProducts, isLoading: productsLoading, error: productsError } = useProducts();
  const { data: categoryProducts, isLoading: categoryLoading } = useProductsByCategory(selectedCategory);
  const { data: categories, isLoading: categoriesLoading } = useCategories();

  // Determine which products to display
  const productsToDisplay = selectedCategory === 'all' ? allProducts : categoryProducts;
  const isLoading = selectedCategory === 'all' ? productsLoading : categoryLoading;

  const handleAddToCart = (product) => {
    dispatch(addToCart(product));
  };

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
  };

  if (productsError) {
    return <div className="error">Error loading products: {productsError.message}</div>;
  }

  return (
    <div className="container">
      <h1>Product Catalog</h1>
      
      <CategoryFilter
        categories={categories}
        selectedCategory={selectedCategory}
        onCategoryChange={handleCategoryChange}
        isLoading={categoriesLoading}
      />

      {isLoading ? (
        <div className="loading">Loading products...</div>
      ) : (
        <div className="products-grid">
          {productsToDisplay?.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onAddToCart={handleAddToCart}
            />
          ))}
        </div>
      )}

      {productsToDisplay?.length === 0 && !isLoading && (
        <div className="error">No products found for this category.</div>
      )}
    </div>
  );
};

export default Home;