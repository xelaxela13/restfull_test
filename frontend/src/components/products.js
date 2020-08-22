import React, {Component} from 'react';
import axios from "axios";
import authHeader from "../services/auth.header";
import AddToBucket from "./addToBucketButton";


class Products extends Component {

    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            params: ''
        };
         this.handleRequest = this.handleRequest.bind(this);
         this.updateOrdering = this.updateOrdering.bind(this);
         this.updateSearch = this.updateSearch.bind(this);
         this.order = React.createRef();
         this.search = React.createRef()
    }

    updateOrdering(){
        this.setState({params: '?ordering='+this.order.current.value})
    }
    updateSearch(){
        this.setState({params: '?search='+this.search.current.value})
    }
    handleRequest(params) {
        const url = 'http://localhost:9999/api/products/'+params;
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
        this.handleRequest('')
    }
    componentDidUpdate(prevProps, prevState, snapshot) {
        prevState.params !== this.state.params && this.handleRequest(this.state.params)
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
                    <p>Filters just for example, without multiple values and validations</p>
                    <div>
                        <select className="custom-select" id="order" ref={this.order} onChange={this.updateOrdering}>
                            <option selected>Sort by price...</option>
                            <option value="price">Ascending</option>
                            <option value="-price">Descending</option>
                        </select>
                    </div>
                    <div className="input-group my-3">
                        <input type="text" className="form-control" placeholder="Search text"
                               aria-label="Search text" aria-describedby="button-addon2" ref={this.search}/>
                            <div className="input-group-append">
                                <button className="btn btn-primary" type="button" id="button-addon2" onClick={this.updateSearch}>
                                    Search
                                </button>
                            </div>
                    </div>
                    {items.map(item => (
                        <div key={item.id} className="card m-3">
                            <div className="card-body">
                                <h5 className="card-title">{item.name}</h5>
                                <h6 className="card-subtitle mb-2 text-muted">{item.price}</h6>
                                <p className="card-text">{item.description}</p>
                                <AddToBucket key={item.id} product_id={item.id}/>
                            </div>
                        </div>
                    ))}
                </div>
            );
        }
    }
}

export default Products;
