import axios from "axios";

const API_URL = "http://localhost:9999/api/token/";

class AuthService {
    login(email, password) {
        return axios
            .post(API_URL,
                {
                    email,
                    password,
                },
                {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Access-Control-Allow-Origin': '*'
                    }
                }
            )
            .then(response => {
                debugger
                if (response.data.accessToken) {
                    localStorage.setItem("user", JSON.stringify(response.data));
                }

                return response.data;
            });
    }

    logout() {
        localStorage.removeItem("user");
    }

    getCurrentUser() {
        return JSON.parse(localStorage.getItem('user'));
    }
}

export default new AuthService();
