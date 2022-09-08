# Third-party Libraries
from pathlib import Path

# Own's Libraries
from filemanagerutil.errors import InvalidFileNameError
from filemanagerutil.errors import InvalidPasswordError


class File(object):

    def __init__(self, _name, _path=None):
        self._name = _name
        self._path = _path

    def __checkUserValue(self, _value):
        if _value is None:
            raise InvalidFileNameError("File name cannot be None")

        if isinstance(_value, str) is False:
            raise InvalidFileNameError("File name must be a string")

    def __checkPasswordValue(self, _value):
        if _value is None:
            raise InvalidPasswordError("Password cannot be None")

        if isinstance(_value, str) is False:
            raise InvalidPasswordError("Password must be a string")

        return

    @property
    def abspath(self):
        if self._path is None:
            return Path().absolute()

        path_obj = Path(self._path)
        return str(path_obj.joinpath(self._name))

    @property
    def name(self):
        return self.name

    def __repr__(self):
        return f"File: {self.name}"

    def __str__(self):
        return f"File: {self.name}"

    def move(self, _destination_path, _raplace=True):
        pass
