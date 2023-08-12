import sender
import extractor
from os import listdir


# instantiate SMTP client
client = sender.create_client()

for cv in listdir("../data/current"):
    path_to_cv = "../data/current/" + cv
    recipient = extractor.extract_address(path_to_cv)
    sender.send_cv(recipient, path_to_cv, client)
