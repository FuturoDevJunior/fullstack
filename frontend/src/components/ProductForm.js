import { TextField, Button } from '@mui/material';
import { useState } from 'react';

function ProductForm({ onSubmit }) {
  const [name, setName] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = () => {
    onSubmit({ name, price: parseFloat(price) });
    setName('');
    setPrice('');
  };

  return (
    <div>
      <TextField label="Nome" value={name} onChange={(e) => setName(e.target.value)} />
      <TextField label="Preço" value={price} onChange={(e) => setPrice(e.target.value)} />
      <Button onClick={handleSubmit}>Salvar</Button>
    </div>
  );
}

export default ProductForm;