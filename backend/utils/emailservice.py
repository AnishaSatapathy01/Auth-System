import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_ADDRESS = "anishasatapathy23@gmail.com"
EMAIL_PASSWORD = "dgjz jvny fdqp wgax"


def send_otp_email(receiver_email, otp):

    subject = "Password Reset OTP"

    body = f"""
Your OTP for password reset is: {otp}

This OTP will expire shortly.
"""

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        server.sendmail(
            EMAIL_ADDRESS,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print("OTP email sent successfully")

    except Exception as e:
        print("SMTP Error:", str(e))