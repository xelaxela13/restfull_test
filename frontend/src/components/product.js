import React, {Component} from 'react';
import axios from "axios";
import authHeader from "../services/auth.header";
import AddToBucket from "./addButton";


class Product extends Component {

    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            ...props.location.state
        };
        this.handleRequest = this.handleRequest.bind(this);
    }

    handleRequest(id) {
        const url = `http://localhost:9999/api/products/${id}`;
        axios.get(url, {headers: authHeader()})
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result.data,
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    componentDidMount() {
        this.handleRequest(this.state.product_id)
    }

    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <div className="col-12">Ошибка: {error.message}</div>;
        } else if (!isLoaded) {
            return <div className="col-12">Загрузка...</div>;
        } else {
            return (
                <div className="col-12">
                    <div className="card m-3">
                        <div className="card-body">
                            <h5 className="card-title">{items.name}</h5>
                            <h6 className="card-subtitle mb-2 text-muted">{items.price}</h6>
                            <p className="card-text">{items.description}</p>
                            {items.category_name_list.map(category_name => (
                                <p>{category_name}</p>
                            ))}
                            <AddToBucket product_id={items.id}/>
                        </div>
                    </div>
                </div>
            );
        }
    }
}

export default Product;
