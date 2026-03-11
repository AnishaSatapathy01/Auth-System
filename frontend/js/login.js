async function login(){

const email =
document.getElementById("email").value

const password =
document.getElementById("password").value


const response = await fetch(
"http://127.0.0.1:8000/auth/login",
{
method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
email: email,
password: password
})

})


const data = await response.json()


if(data.error){

document.getElementById("error").innerText =
"Invalid email or password"

return

}


/* store JWT token */

localStorage.setItem(
"token",
data.access_token
)


/* store role */

localStorage.setItem(
"role",
data.role
)


/* redirect */

window.location.href =
  "dashboard.html"



}