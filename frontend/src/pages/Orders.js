import { useEffect, useState } from 'react';

function Orders() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/orders/')
      .then((res) => res.json())
      .then((data) => setOrders(data));
  }, []);

  return (
    <div>
      <h1>Pedidos</h1>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>Total: {order.total}</li>
        ))}
      </ul>
    </div>
  );
}

export default Orders;