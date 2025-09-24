import React, { useState } from 'react';

const ProductCard = ({ product, onAddToCart }) => {
  const [imageError, setImageError] = useState(false);
  
  const handleImageError = () => {
    setImageError(true);
  };

  const getPlaceholderImage = () => {
    return `https://via.placeholder.com/200x200/f0f0f0/666666?text=Product+Image`;
  };

  return (
    <div className="product-card">
      <img
        src={imageError ? getPlaceholderImage() : product.image}
        alt={product.title}
        className="product-image"
        onError={handleImageError}
      />
      <div className="product-title">{product.title}</div>
      <div className="product-price">${product.price.toFixed(2)}</div>
      <div className="product-category">{product.category}</div>
      <div className="product-rating">
        ⭐ {product.rating.rate} ({product.rating.count} reviews)
      </div>
      <div className="product-description">
        {product.description.length > 100 
          ? `${product.description.substring(0, 100)}...` 
          : product.description}
      </div>
      <button
        className="add-to-cart-btn"
        onClick={() => onAddToCart(product)}
      >
        Add to Cart
      </button>
    </div>
  );
};

export default ProductCard;