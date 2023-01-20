# Useful functions
from urllib.parse import urlparse

def flatten(l):
    """
    Flatten a list
    found here : https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    """
    return [item for sublist in l for item in sublist]


def url_to_main(url : str):
    domain = urlparse(url)
    url = domain.scheme +"://" + domain.netloc
    return(url)

def list_to_txt(url_list : list, filename : str):
    """
    found here : https://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python-with-newlines
    """
    with open(filename, 'w') as f:
        for line in url_list:
            f.write(f"{line}\n")