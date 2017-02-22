class HTMLParseError(Exception):
    """
    A generic HTML parsing errors validators can throw.
    """
    message: str

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return "Parse Error: {}".format(self.message)
