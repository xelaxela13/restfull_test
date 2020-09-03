import React, {Component} from 'react';
import {Switch, Route, Link} from 'react-router-dom';
import {instanceOf} from 'prop-types';
import {withCookies, Cookies} from 'react-cookie';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from "./components/login";
import Products from "./components/products";
import Product from "./components/product";
import Bucket from "./components/bucket";
import Home from "./components/home";


class App extends Component {
    static propTypes = {
        cookies: instanceOf(Cookies).isRequired
    };

    constructor(props) {
        super(props);
        this.logOut = this.logOut.bind(this);
        this.state = {
            userToken: undefined
        };
    }

    componentDidMount() {
        let { cookies } = this.props;
        let usertoken = cookies.get('usertoken')
        if (usertoken) {
            this.setState({
                userToken: usertoken,
            });
        }
    }

    logOut() {
        let { cookies } = this.props;
        cookies.remove('usertoken')
    }

    render() {
        const {userToken} = this.state;

        return (
            <div>
                <nav className="navbar navbar-expand navbar-dark bg-dark">
                    <div className="navbar-nav mr-auto">
                        <li className="nav-item">
                            <Link to={"/"} className="nav-link">
                                Home
                            </Link>
                        </li>

                        {userToken && (
                            <li className="nav-item">
                                <Link to={"/products"} className="nav-link">
                                    Products
                                </Link>
                            </li>
                        )}
                        {userToken && (
                            <li className="nav-item">
                                <Link to={"/bucket"} className="nav-link">
                                    Bucket
                                </Link>
                            </li>
                        )}
                    </div>

                    {userToken ? (
                        <div className="navbar-nav ml-auto">
                            <li className="nav-item">
                                <a href="/login" className="nav-link" onClick={this.logOut}>
                                    LogOut
                                </a>
                            </li>
                        </div>
                    ) : (
                        <div className="navbar-nav ml-auto">
                            <li className="nav-item">
                                <Link to={"/login"} className="nav-link">
                                    Login
                                </Link>
                            </li>

                        </div>
                    )}
                </nav>
                <div className="container">
                    <div className="row py-5">
                        <Switch>
                            <Route exact path="/" component={Home}/>
                            <Route exact path="/login" component={Login}/>
                            <Route exact path="/products" component={Products}/>
                            <Route path="/product/:id" component={Product}/>
                            <Route exact path="/bucket" component={Bucket}/>
                        </Switch>
                    </div>
                </div>
            </div>
        );
    }
}

export default withCookies(App);
