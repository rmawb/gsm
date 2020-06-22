#module for custom errors

class CustomException(Exception):
    pass

class ExtraTraitError(CustomException):
    "Error when there is an unexpected or undefined trait."
    pass