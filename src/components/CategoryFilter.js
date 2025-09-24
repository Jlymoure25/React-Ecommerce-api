import React from 'react';

const CategoryFilter = ({ categories, selectedCategory, onCategoryChange, isLoading }) => {
  if (isLoading) {
    return <div className="loading">Loading categories...</div>;
  }

  return (
    <div className="category-filter">
      <label htmlFor="category-select">Filter by Category: </label>
      <select
        id="category-select"
        className="category-select"
        value={selectedCategory}
        onChange={(e) => onCategoryChange(e.target.value)}
      >
        <option value="all">All Categories</option>
        {categories?.map((category) => (
          <option key={category} value={category}>
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </option>
        ))}
      </select>
    </div>
  );
};

export default CategoryFilter;