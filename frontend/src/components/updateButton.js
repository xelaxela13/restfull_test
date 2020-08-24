import React, {Component} from 'react';
import axios from "axios";
import authHeader from "../services/auth.header";


class UpdateBucket extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            update: false,
            product_id: props.product_id,
            product_count: props.product_count
        };
        this.handleRequest = this.handleRequest.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleRequest() {
        const url = 'http://localhost:9999/api/bucket/';
        axios.post(url, {'product': this.state.product_id, 'count': this.state.product_count}, {headers: authHeader()})
            .then(
                (result) => {
                    debugger
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

    handleChange(event) {
        this.setState({product_count: event.target.value});
    }

    handleSubmit() {
        this.setState({update: true});
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        this.state.update && this.handleRequest()
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="input-group mb-3">
                    <input type="number" className="form-control" placeholder="Qty"
                           aria-label="Qty" value={this.state.product_count} aria-describedby={"product_" + this.state.product_id}
                    onChange={this.handleChange}/>
                    <div className="input-group-append">
                        <button className="btn btn-primary" type="submit" id={"product_" + this.state.product_id}>
                            Submit
                        </button>
                    </div>
                </div>
            </form>
        );
    }
}

export default UpdateBucket;
