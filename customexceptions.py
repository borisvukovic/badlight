class FileNotFoundError(FileExistsError):
    """Raised when log file could not be found"""


class LightIOError(IOError):
    """Raised when communication between master module and a light failed"""


class LightInitError(IOError):
    """Raised when a light could not be initialized"""


class LightStateError(IOError):
    """Raised when state is not what it should be"""