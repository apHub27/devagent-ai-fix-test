
import { useState } from "react";

export default function Cart() {
  const [total, setTotal] = useState(0);
  const [message, setMessage] = useState("");

  async function calculateTotal() {
    try {
      const response = await fetch("/api/cart", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          items: [
            { product_id: 1, quantity: 2 },
            { product_id: 2, quantity: 3 },
          ],
        }),
      });

      const data = await response.json();
      setTotal(data.total);
      setMessage("Cart calculated successfully");
    } catch {
      setMessage("Unable to calculate cart");
    }
  }

  return (
    <div>
      <h2>Shopping Cart</h2>
      <button onClick={calculateTotal}>Calculate Total</button>
      <p>Total: ₹{total}</p>
      <p>{message}</p>
    </div>
  );
}
