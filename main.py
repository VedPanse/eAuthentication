from random import randint
import smtplib
otp = 0
game_on = True


def send_otp():
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=given_id,
                            msg=f"Subject:One-Time Verification\n\nHi there, here is your OTP: {otp}")
        connection.close()


def generate_otp():
    global otp
    otp = randint(1000, 9999)


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


my_email = "<my_email@email.com>"
password = "<my_password>"


print(f"{Color.PURPLE}LOG IN{Color.END}")
given_id = input("Please enter your email ID to log in: ")

if "@" in given_id and "." in given_id:
    generate_otp()
    send_otp()
    given_otp = input(f"An OTP was sent to {given_id}. Please enter the OTP here: ")

    try:
        given_otp = int(given_otp)
        if otp == given_otp:
            print(f"{Color.GREEN}Log In Successful.{Color.END}")
        else:
            print(f"{Color.RED}Sorry, the OTP you entered was incorrect.{Color.BOLD}A new OTP is on its way.{Color.END}")
    except ValueError:
        print(f"{Color.RED}Please enter a valid OTP. OTP Verification failed. {Color.BOLD}A new OTP is on its way.{Color.END}")

else:
    print(f"{Color.RED}Please enter a valid email address.{Color.END}")
