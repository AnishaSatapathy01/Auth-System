import random

otp_store = {}


def generate_otp():

    return str(random.randint(100000, 999999))


def save_otp(email, otp):

    otp_store[email] = otp