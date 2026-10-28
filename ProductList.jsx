
import { useEffect, useState } from "react";

export default function ProductList() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("/api/products")
      .then((response) => response.json())
      .then((data) => setProducts(data))
      .catch(() => setError("Unable to load products"));
  }, []);

  return (
    <div>
      <h2>Products</h2>

      {error && <p>{error}</p>}

      {products.map((product) => (
        <div key={product.id}>
          <span>{product.name}</span>
          <span> ₹{product.price.toFixed(2)}</span>
          <span> Stock: {product.stock}</span>
        </div>
      ))}
    </div>
  );
}
