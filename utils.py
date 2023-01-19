# Useful functions

def flatten(l):
    """
    Flatten a list
    found here : https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    """
    return [item for sublist in l for item in sublist]