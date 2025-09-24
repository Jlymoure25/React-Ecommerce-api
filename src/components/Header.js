import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

const Header = () => {
  const { itemCount } = useSelector((state) => state.cart);

  return (
    <header className="header">
      <nav className="nav">
        <Link to="/" className="logo">E-Commerce Store</Link>
        <Link to="/cart">
          <button className="cart-button">
            Cart ({itemCount})
          </button>
        </Link>
      </nav>
    </header>
  );
};

export default Header;