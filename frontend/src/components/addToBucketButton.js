import React, {Component} from 'react';
import axios from "axios";
import authHeader from "../services/auth.header";


class AddToBucket extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            added: false,
            product_count: null,
            product_id: props.product_id
        };
        this.handleRequest = this.handleRequest.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleRequest() {
        const url = 'http://localhost:9999/api/bucket/';
        axios.post(url, {'product': this.state.product_id, 'count': this.state.product_count}, {headers: authHeader()})
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result.data,
                        added: true,
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

    handleChange(event) {
        this.setState({product_count: event.target.value});
    }

    handleSubmit(event) {
        this.handleRequest()
    }

    render() {
        const {error} = this.state;
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="input-group my-3">
                    <input type="text" className="form-control" placeholder="Qty"
                           aria-label="qty" aria-describedby={"product_" + this.state.product_id}
                           value={this.state.product_count} onChange={this.handleChange}
                    />
                    <div className="input-group-append">
                        <button className="btn btn-primary" type="submit" id={"product_" + this.state.product_id}>
                            Search
                        </button>
                    </div>
                    {error && (
                        <div className="form-group">
                            <div className="alert alert-danger" role="alert">
                                {error}
                            </div>
                        </div>
                    )}
                </div>
            </form>
        );
    }
}

export default AddToBucket;
