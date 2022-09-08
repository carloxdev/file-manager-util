# Python's Libraries
import os
from pathlib import Path

# Own's Libraries
from file import File


class Folder(object):
    """Class that represent a folder in filesystem"""

    def __init__(self, _abspath):
        """
        :param _abspath: absolute path of the folder
        :type _abspath: str
        :param _relative: flag to indicate if the path is relative or absolute
        :type _relative: bool
        """
        self.abspath = _abspath
        self.name = Path(_abspath).parts[-1]

    def __repr__(self):
        return f"Folder: {self.name}"

    def __str__(self):
        return f"Folder: {self.name}"

    def get_Content(self, _levels=None):
        """Get a list of File objects

        :raises [ErrorType]: [ErrorDescription]
        ...
        :return: [ReturnDescription]
        :rtype: [ReturnType]
        """

        level = 0
        list_elements = []

        if os.path.exists(self.abspath) is False:
            raise

        elements = os.walk(self.abspath)
        for directory_path, list_dir_names, list_file_names in elements:
            for dir_name in list_dir_names:
                dir_abspath = os.path.join(
                    directory_path,
                    dir_name
                )
                folder_obj = Folder(dir_abspath)
                list_elements.append(folder_obj)

            for file_name in list_file_names:
                file_abspath = os.path.join(
                    directory_path,
                    file_name
                )
                file_obj = File(file_abspath)
                list_elements.append(file_obj)

            level += 1
            if _levels == level:
                break

        return list_elements

    def get_File(self):
        pass
