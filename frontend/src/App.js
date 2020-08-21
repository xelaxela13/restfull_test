import React from 'react';
import { Switch, Route } from 'react-router-dom';
import './App.css';
import Products from "./components/products";
import Login from "./components/login";


function App() {
    return (
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <Route path="/login" component={Login}/>
                    <Login/>
                    <Products/>
                </div>
            </div>
        </div>
    );
}

export default App;
