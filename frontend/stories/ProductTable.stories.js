import ProductTable from '../src/components/ProductTable';

export default {
  title: 'ProductTable',
  component: ProductTable,
};

const Template = (args) => <ProductTable {...args} />;

export const Default = Template.bind({});
Default.args = {
  products: [{ id: '1', name: 'Celular', price: 999.99 }],
};