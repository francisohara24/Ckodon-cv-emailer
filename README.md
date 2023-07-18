# Ckodon-cv-emailer
This is a Python program I wrote to automate the process of submitting reviewed CVs via email to students at [the Ckodon Foundation](https://www.ckodon.com/ckodon-foundation).

 - The `docx2txt` library is used to extract the content of the Word document as text, and regular expressions are 
   used to identify the recipient's email from the extracted text.
 - The `email` and `smtplib` libraries are used to send emails to students with the CV document as attachment.
