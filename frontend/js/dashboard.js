const role = localStorage.getItem("role")

document.getElementById("userRole").innerText =
"Role: " + role



if(role === "employee"){

document.getElementById("postJobBtn").style.display="none"
document.getElementById("editJobBtn").style.display="none"
document.getElementById("deleteJobBtn").style.display="none"
document.getElementById("roleSection").style.display="none"

}

if(role === "manager"){

document.getElementById("editJobBtn").style.display="none"
document.getElementById("roleSection").style.display="none"

}

if(role === "admin"){

document.getElementById("applyJobBtn").style.display="none"

}


async function assignRole(){

const email =
document.getElementById("roleEmail").value

const role =
document.getElementById("newRole").value


await fetch(
"http://127.0.0.1:8000/auth/assign-role",
{
method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
email:email,
role:role
})
})

alert("Role updated")

}