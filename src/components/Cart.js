import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { removeFromCart, updateQuantity, clearCart } from '../store/cartSlice';
import { Link } from 'react-router-dom';

const Cart = () => {
  const { items, total, itemCount } = useSelector((state) => state.cart);
  const dispatch = useDispatch();
  const [isCheckingOut, setIsCheckingOut] = useState(false);
  const [checkoutSuccess, setCheckoutSuccess] = useState(false);

  const handleRemoveFromCart = (productId) => {
    dispatch(removeFromCart(productId));
  };

  const handleQuantityChange = (id, newQuantity) => {
    if (newQuantity > 0) {
      dispatch(updateQuantity({ id, quantity: newQuantity }));
    }
  };

  const handleCheckout = async () => {
    setIsCheckingOut(true);
    
    // Simulate checkout process
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    dispatch(clearCart());
    setCheckoutSuccess(true);
    setIsCheckingOut(false);
    
    // Clear success message after 3 seconds
    setTimeout(() => setCheckoutSuccess(false), 3000);
  };

  if (items.length === 0 && !checkoutSuccess) {
    return (
      <div className="cart-page">
        <h1>Shopping Cart</h1>
        <div className="error">Your cart is empty.</div>
        <Link to="/">
          <button className="checkout-btn">Continue Shopping</button>
        </Link>
      </div>
    );
  }

  return (
    <div className="cart-page">
      <h1>Shopping Cart</h1>
      
      {checkoutSuccess && (
        <div className="success-message">
          🎉 Checkout successful! Your order has been processed and your cart has been cleared.
        </div>
      )}

      {items.length > 0 && (
        <>
          <div className="cart-items">
            {items.map((item) => (
              <div key={item.id} className="cart-item">
                <img
                  src={item.image}
                  alt={item.title}
                  className="cart-item-image"
                  onError={(e) => {
                    e.target.src = `https://via.placeholder.com/80x80/f0f0f0/666666?text=Product`;
                  }}
                />
                <div className="cart-item-details">
                  <div className="cart-item-title">{item.title}</div>
                  <div className="cart-item-price">${item.price.toFixed(2)} each</div>
                  <div className="cart-item-quantity">
                    <label>Quantity: </label>
                    <input
                      type="number"
                      min="1"
                      value={item.quantity}
                      onChange={(e) => handleQuantityChange(item.id, parseInt(e.target.value))}
                      style={{ width: '60px', padding: '5px', marginLeft: '10px' }}
                    />
                  </div>
                  <div className="cart-item-subtotal">
                    Subtotal: ${(item.price * item.quantity).toFixed(2)}
                  </div>
                </div>
                <button
                  className="remove-btn"
                  onClick={() => handleRemoveFromCart(item.id)}
                >
                  Remove
                </button>
              </div>
            ))}
          </div>

          <div className="cart-summary">
            <h2>Cart Summary</h2>
            <div style={{ marginBottom: '10px' }}>
              <strong>Total Items: {itemCount}</strong>
            </div>
            <div style={{ marginBottom: '20px', fontSize: '1.2rem' }}>
              <strong>Total Price: ${total.toFixed(2)}</strong>
            </div>
            <button
              className="checkout-btn"
              onClick={handleCheckout}
              disabled={isCheckingOut || items.length === 0}
            >
              {isCheckingOut ? 'Processing...' : 'Checkout'}
            </button>
          </div>
        </>
      )}

      <Link to="/">
        <button className="cart-button" style={{ marginTop: '20px' }}>
          Continue Shopping
        </button>
      </Link>
    </div>
  );
};

export default Cart;