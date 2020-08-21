export default function authHeader() {
    const user = JSON.parse(localStorage.getItem('user'));
    if (user && user.access) {
        return {Authorization: 'Bearer ' + user.access, 'Content-Type': 'application/json'};
    } else {
        return {'Content-Type': 'application/json'};
    }
}
