import { useEffect, useState } from 'react';

function Dashboard() {
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    fetch('http://localhost:8000/dashboard/')
      .then((res) => res.json())
      .then((data) => setMetrics(data));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Total de Pedidos: {metrics.total_orders}</p>
      <p>Valor Médio: {metrics.avg_total}</p>
      <p>Receita Total: {metrics.total_revenue}</p>
    </div>
  );
}

export default Dashboard;