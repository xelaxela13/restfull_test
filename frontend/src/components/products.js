import React, {Component} from 'react';
import axios from "axios";


class Products extends Component {

    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
        };
    }

    componentDidMount() {
        const url = 'http://localhost:8500/products/'
        axios.get(url,
            {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Access-Control-Allow-Origin': '*',
                    'Authorization': 'Bearer '
                }
            })
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result,
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

    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <div>Ошибка: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Загрузка...</div>;
        } else {
            return (
                <div className="col-12">
                    <ul>
                        {items.map(item => (
                            <li key={item.name}>
                                {item.name} {item.price}
                            </li>
                        ))}
                    </ul>
                </div>
            );
        }
    }
}

export default Products;
