import axios from "axios";

const API_URL = "http://localhost:9999/api/token/";

export default function login(email, password) {
    return axios
        .post(API_URL,
            {
                email,
                password,
            },
        )
        .then(response => {
            return response.data;
        });
}