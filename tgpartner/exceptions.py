class TGPartnerException(Exception):
    """Base class of exceptions."""
    pass


class EnvironmentVariableNotFound(TGPartnerException):
    """Environment Variable not found."""
    pass