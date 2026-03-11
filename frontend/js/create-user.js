/* password eye toggle */

const togglePassword =
document.getElementById("togglePassword")

const password =
document.getElementById("password")

togglePassword.addEventListener("click", function(){

if(password.type === "password"){

password.type = "text"
this.classList.replace("fa-eye","fa-eye-slash")

}
else{

password.type = "password"
this.classList.replace("fa-eye-slash","fa-eye")

}

})



async function createUser(){

const username =
document.getElementById("username").value

const email =
document.getElementById("email").value

const passwordValue =
document.getElementById("password").value




const response = await fetch(
"http://127.0.0.1:8000/auth/register",
{
method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
username:username,
email:email,
password:passwordValue,

})
})

const data = await response.json()


if (!response.ok) {

document.getElementById("message").innerText =
("Error!! password too short !")

return

}

document.getElementById("message").innerText =
"Account created successfully"

}