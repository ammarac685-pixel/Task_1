class PortalError(Exception):
    pass


class FileLoadError(PortalError):
    pass


class ValidationError(PortalError):
    pass
