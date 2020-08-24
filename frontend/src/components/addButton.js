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
            add: false,
            product_id: props.product_id
        };
        this.handleRequest = this.handleRequest.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleRequest() {
        const url = 'http://localhost:9999/api/bucket/';
        axios.post(url, {'product': this.state.product_id}, {headers: authHeader()})
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

    handleSubmit() {
        this.setState({add: true});
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        this.state.add && this.handleRequest()
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button className="btn btn-primary" type="submit" id={"product_" + this.state.product_id}>
                    Add
                </button>
            </form>
        );
    }
}

export default AddToBucket;
