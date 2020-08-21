export const userLoginFetch = user => {
  return dispatch => {
    return fetch("http://localhost:8500/api/token/", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        Accept: 'application/json',
      },
      body: JSON.stringify({user})
    })
      .then(resp => resp.json())
      .then(data => {
        if (data.message) {
         //тут ваша логика
        } else {
          localStorage.setItem("token", data.access)
          dispatch(loginUser(data.user))
        }
      })
  }
}

const loginUser = userObj => ({
    type: 'LOGIN_USER',
    payload: userObj
})