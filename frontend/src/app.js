import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Products from './pages/Products';
import Categories from './pages/Categories';
import Orders from './pages/Orders';
import Dashboard from './pages/Dashboard';

function App() {
    return ( <
        Router >
        <
        Routes >
        <
        Route path = "/products"
        element = { < Products / > }
        /> <
        Route path = "/categories"
        element = { < Categories / > }
        /> <
        Route path = "/orders"
        element = { < Orders / > }
        /> <
        Route path = "/dashboard"
        element = { < Dashboard / > }
        /> <
        /Routes> <
        /Router>
    );
}

export default App;