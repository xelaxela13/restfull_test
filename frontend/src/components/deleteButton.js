import React, {Component} from 'react';
import axios from "axios";
import authHeader from "../services/auth.header";


class DeleteButton extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            delete: false,
            product_id: props.product_id
        };
        this.handleRequest = this.handleRequest.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleRequest() {
        const url = 'http://localhost:9999/api/bucket/' + this.state.product_id;
        axios.delete(url, {headers: authHeader()})
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
        this.setState({delete: true});
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        this.state.delete && this.handleRequest()
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button className="btn btn-danger" type="submit">
                    Delete
                </button>
            </form>
        );
    }
}

export default DeleteButton;
