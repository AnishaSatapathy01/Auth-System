async function sendOTP() {

    const email =
        document.getElementById("email").value

    const response = await fetch(
        "http://127.0.0.1:8000/auth/send-otp",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: email })
        })

    const data = await response.json()

    if (!response.ok) {

        document.getElementById("message").innerText =
            data.detail

        return
    }

    document.getElementById("message").innerText =
        "OTP sent to your email"

    document.getElementById("otpSection").style.display =
        "block"

}



async function verifyOTP() {

    const email =
        document.getElementById("email").value

    const otp =
        document.getElementById("otp").value


    const response = await fetch(
        "http://127.0.0.1:8000/auth/verify-otp",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                otp: otp
            })
        })

    const data = await response.json()

    if (!response.ok) {

        document.getElementById("message").innerText =
            data.detail

        return
    }

    document.getElementById("message").innerText =
        "OTP verified"

    document.getElementById("passwordSection").style.display =
        "block"

}



async function resetPassword() {

    const email =
        document.getElementById("email").value

    const newPassword =
        document.getElementById("newPassword").value


    const response = await fetch(
        "http://127.0.0.1:8000/auth/reset-password",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                new_password: newPassword
            })
        })

    const data = await response.json()

    if (!response.ok) {

        document.getElementById("message").innerText =
            data.detail

        return
    }

    document.getElementById("message").innerText =
        "Password reset successfully"

}