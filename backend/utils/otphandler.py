import random

otp_store = {}


def generate_otp():

    return str(random.randint(100000, 999999))


def save_otp(email, otp):

    otp_store[email] = otp

def verify_otp(email, otp):

    if email not in otp_store:
        return False

    if otp_store[email] != otp:
        return False

    return True


def delete_otp(email):

    if email in otp_store:
        del otp_store[email]