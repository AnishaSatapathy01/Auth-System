import mailtrap as mt

MAILTRAP_TOKEN = "446f21dbe9b05ca9b254b8180f0af433"


def send_otp_email(receiver_email, otp):

    mail = mt.Mail(
        sender=mt.Address(email="hello@demomailtrap.co", name="Mailtrap Test"),
        to=[mt.Address(email=receiver_email)],
        subject="Password Reset OTP",
        text=f"Your OTP is {otp}",
        category="Integration Test",
    )

    client = mt.MailtrapClient(token=MAILTRAP_TOKEN)

    response = client.send(mail)

    print(response)