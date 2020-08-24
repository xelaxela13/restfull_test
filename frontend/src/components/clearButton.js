import React, {Component} from 'react';
import axios from "axios";
import authHeader from "../services/auth.header";


class ClearButton extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            clear: false,
        };
        this.handleRequest = this.handleRequest.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleRequest() {
        const url = 'http://localhost:9999/api/bucket/clear';
        axios.delete(url, {headers: authHeader()})
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
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
        this.setState({clear: true});
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        this.state.clear && this.handleRequest()
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button className="btn btn-danger" type="submit">
                    Clear bucket
                </button>
            </form>
        );
    }
}

export default ClearButton;
