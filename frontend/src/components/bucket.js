import React, {Component} from 'react';
import axios from "axios";
import authHeader from "../services/auth.header";
import DeleteButton from "./deleteButton";
import ClearButton from "./clearButton";
import UpdateBucket from "./updateButton";


class Bucket extends Component {

    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            amount: 0,
            params: ''
        };
         this.handleRequest = this.handleRequest.bind(this);

    }

    handleRequest(params) {
        const url = 'http://localhost:9999/api/bucket/'+params;
        axios.get(url, {headers: authHeader()})
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result.data.products,
                        amount: result.data.amount
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
        this.handleRequest('')
    }
    componentDidUpdate(prevProps, prevState, snapshot) {
        prevState.params !== this.state.params && this.handleRequest(this.state.params)
    }

    render() {
        const {error, isLoaded, items, amount} = this.state;
        if (error) {
            return <div className="col-12">Ошибка: {error.message}</div>;
        } else if (!isLoaded) {
            return <div className="col-12">Загрузка...</div>;
        } else {
            return (
                <div className="col-12">
                    <h5>{amount.total}</h5>
                    <p><ClearButton/></p>
                    {items.map(item => (
                        <div key={item.id} className="card m-3">
                            <div className="card-body">
                                <h5 className="card-title">{item.product_name}</h5>
                                <h6 className="card-subtitle mb-2 text-muted">{item.product_price}</h6>
                                {item.product_category_name_list.map(category_name=>(
                                    <p>{category_name}</p>
                                ))}
                                <UpdateBucket product_id={item.product} product_count={item.count}/>
                                <DeleteButton product_id={item.id} />
                            </div>
                        </div>
                    ))}
                </div>
            );
        }
    }
}

export default Bucket;
