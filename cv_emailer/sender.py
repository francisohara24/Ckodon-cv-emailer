from email.message import EmailMessage
from smtplib import SMTP
import json


def create_client():
    """Returns an SMTP client object with The Ckodon Foundation's credentials.

    Returns
    =======
    smtplib.SMTP
        An SMTP client instance with the Ckodon Foundation's sender credentials.
    """
    # define SMTP server credentials
    credentials = json.load(open("../data/credentials.json"))
    server = credentials["server"]
    port = credentials["port"]
    username = credentials["username"]
    password = credentials["password"]

    # connect to SMTP server
    smtp = SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()

    # login to account on server
    smtp.login(username, password)

    return smtp


def send_cv(recipient, path_to_cv, client):
    """Send email containing CV as attachment to `recipient`.

    Parameters
    ==========
    recipient: str
        The email address to which the CV is to be sent.
    path_to_cv: str
        The path to the Word document containing the CV to be sent.
    client: smtplib.SMTP
        The instantiated SMTP client for sending the email.

    Returns
    =======
    bool
        True if send was successful. False if send was unsuccessful.
    """

    # construct email message
    subject = "Your Updated CV"
    body = """Dear Ckodon Mentee,

Your CV has been reviewed and commented on by our mentors.
Find attached a copy of your reviewed CV.

Thank you.

Best,
The Ckodon Foundation Team.
"""

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "ckodontech@gmail.com"
    msg["To"] = recipient
    msg.set_content(body)

    cv_name = path_to_cv.split("/")[-1]
    cv_data = open(path_to_cv, "rb").read()
    msg.add_attachment(cv_data, filename=cv_name, maintype="application", subtype="msword")

    # send email message
    try:
        client.send_message(msg)
        print("SENT")
        return True
    except:
        print("Error at:", path_to_cv)
        return False
