import { useEffect, useState } from 'react';
import ProductTable from '../components/ProductTable';
import ProductForm from '../components/ProductForm';

function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/products/')
      .then((res) => res.json())
      .then((data) => setProducts(data));
  }, []);

  const addProduct = (product) => {
    fetch('http://localhost:8000/products/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(product),
    }).then(() => setProducts([...products, product]));
  };

  return (
    <div>
      <h1>Produtos</h1>
      <ProductForm onSubmit={addProduct} />
      <ProductTable products={products} />
    </div>
  );
}

export default Products;