import ProductForm from '../src/components/ProductForm';

export default {
  title: 'ProductForm',
  component: ProductForm,
};

const Template = (args) => <ProductForm {...args} />;

export const Default = Template.bind({});
Default.args = {
  onSubmit: (data) => console.log(data),
};