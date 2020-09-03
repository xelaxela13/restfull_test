function GetCookieValue(name) {
    let found = document.cookie.split(';').filter(c => c.trim().split("=")[0] === name);
    return found.length > 0 ? found[0].split("=")[1] : null;
}

export default function authHeader() {
    const user = JSON.parse(localStorage.getItem('user'));
    if (user && user.access) {
        return {Authorization: 'Bearer ' + GetCookieValue('usertoken'), 'Content-Type': 'application/json'};
    } else {
        return {'Content-Type': 'application/json'};
    }
}
