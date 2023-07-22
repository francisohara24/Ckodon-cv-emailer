import sender
import extractor
from os import listdir


# instantiate SMTP client
client = sender.create_client()

for cv in listdir("../data"):
    path_to_cv = "../data/" + cv
    recipient = extractor.extract_address(path_to_cv)
    sender.send_cv(recipient, path_to_cv, client)

