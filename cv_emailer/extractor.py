import docx2txt
import re


def extract_address(path_to_cv: str) -> str:
    """Return first email address extracted from the Word document whose path is specified by `docpath`.

    Parameters
    ----------
    docpath : str
        The path to the Word document from which the email is to be extracted.

    Returns
    -------
    str
        The extracted email address.
    """

    # convert word document to txt file
    # search for substring in txt file that matches the pattern for a regular expression.

    text = docx2txt.process(path_to_cv)
    email_pattern = r"[a-zA-Z0-9.+\-_]+@[a-zA-Z0-9-+]+\.[a-zA-Z]{2,}"

    match = re.search(email_pattern, text)

    if match:
        return match[0]
    else:
        print(path_to_cv)
        raise Exception
